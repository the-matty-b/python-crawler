import pygame

from enum import Enum

from game.cursor import Cursor
from game.grid_highlight import HighlightType
from game.room import Room
from game.transform_2d import Transform2D
from game.unit_action_menu import UnitActionMenu, UnitAction
from game.unit_info import UnitInfo

class UserControlMode(Enum):
    GRID_CURSOR = 1
    MOVING_ALLY = 2
    ACTION_MENU = 3
    ATTACKING = 4

class UserController():
    def __init__(self, cursor: Cursor, room: Room, unit_info: UnitInfo, action_menu: UnitActionMenu):
        self.cursor = cursor
        self.room = room
        self.unit_info = unit_info
        self.action_menu = action_menu
        
        # might be able to remove highlight mode
        self.highlight_mode = False
        self.change_control_mode(UserControlMode.GRID_CURSOR)
        self.previous_player_node = None

    # NOTE: Pygame has issues with multiple for loops over events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
            elif event.type == pygame.KEYUP:
                self.handle_keyup(event.key)

    # TODO: Create different input modes to filter which keys are handled and for what action is the intention
    
    def handle_keydown(self, key):
        if self.control_mode == UserControlMode.GRID_CURSOR:
            self.handle_grid_cursor_mode(key)
            self.unit_info.update_unit_info(self.room.check_space_for_unit(self.cursor.transform))
        elif self.control_mode == UserControlMode.ACTION_MENU:
            self.handle_action_menu_mode(key)
        elif self.control_mode == UserControlMode.MOVING_ALLY:
            self.handle_moving_ally_mode(key)
        elif self.control_mode == UserControlMode.ATTACKING:
            self.handle_attacking_mode(key)
        
    def handle_grid_cursor_mode(self, key):
        self.handle_cursor_movement(key)
        if key == pygame.K_e:
            unit = self.unit_info.unit_ref
            if unit and unit.name == "Player":
                self.room.grid.set_highlighted_movement_nodes(self.unit_info.unit_ref, HighlightType.BLUE)
                self.change_control_mode(UserControlMode.MOVING_ALLY)
    
    def handle_action_menu_mode(self, key):
        if key == pygame.K_UP:
            self.action_menu.move(-1)
        elif key == pygame.K_DOWN:
            self.action_menu.move(1)
        elif key == pygame.K_q:
            print(self.room.grid.highlighted_nodes.__len__())
            self.action_menu.clear_menu()
            self.change_control_mode(UserControlMode.MOVING_ALLY)
            self.unit_info.unit_ref.move(self.previous_player_node)
            self.previous_player_node = None
        elif key == pygame.K_e:
            self.handle_unit_action(self.action_menu.select_item())
            # self.room.grid.clear_highlighted_nodes()
    
    def handle_unit_action(self, action: UnitAction):
        print(action.value)
        if action == UnitAction.WAIT:
            # TODO: Implement turns to make us wait
            print("Action was Wait")
            
            # TODO: temporary code below. remove when turns are implemented
            self.action_menu.clear_menu()
            self.room.grid.clear_highlighted_nodes()
            self.change_control_mode(UserControlMode.GRID_CURSOR)

        elif action == UnitAction.ATTACK:
            print("Action was Attack")
            self.room.grid.set_highlighted_attackable_nodes(self.unit_info.unit_ref, HighlightType.YELLOW)
            print(self.room.grid.attackable_nodes.__len__())
            self.change_control_mode(UserControlMode.ATTACKING)
            self.action_menu.clear_menu()
            
    
    def handle_attacking_mode(self, key):
        self.handle_cursor_movement(key)
        unit = self.unit_info.unit_ref
        if key == pygame.K_e:
            for node in self.room.grid.attackable_nodes:
                if Transform2D(node.x, node.y) == self.cursor.transform:
                    enemy = node.unit_ref
                    unit.attack(enemy)
                    # self.action_menu.clear_menu()
                    self.change_control_mode(UserControlMode.GRID_CURSOR)
                    return
            
            # self.action_menu.clear_menu()
            # self.room.grid.clear_highlighted_nodes()
            self.room.grid.clear_attackable_nodes()
            self.room.grid.find_attackable_nodes(self.unit_info.unit_ref)
            if self.room.grid.attackable_nodes.__len__() > 0:
                self.action_menu.can_attack = True
            
            self.action_menu.determine_actions(unit)
            self.change_control_mode(UserControlMode.ACTION_MENU)
        
        elif key == pygame.K_q:
            self.room.grid.clear_highlighted_nodes()
            self.room.grid.find_attackable_nodes(self.unit_info.unit_ref)
            if self.room.grid.attackable_nodes.__len__() > 0:
                self.action_menu.can_attack = True
            self.action_menu.determine_actions(unit)
            self.change_control_mode(UserControlMode.ACTION_MENU)
        
    
    def handle_moving_ally_mode(self, key):
        self.handle_cursor_movement(key)
        unit = self.unit_info.unit_ref
        if key == pygame.K_e:
            for node in self.room.grid.highlighted_nodes:
                if Transform2D(node.x, node.y) == self.cursor.transform:
                    self.previous_player_node = unit.node
                    unit.move(node)
                    # gonna have to change the attackable nodes to not be highlightable
                    self.room.grid.find_attackable_nodes(self.unit_info.unit_ref)
                    if self.room.grid.attackable_nodes.__len__() > 0:
                        self.action_menu.can_attack = True
                    
                    self.action_menu.determine_actions(unit)
                    self.change_control_mode(UserControlMode.ACTION_MENU)
                    return
            self.room.grid.clear_highlighted_nodes()
            self.change_control_mode(UserControlMode.GRID_CURSOR)
        
        elif key == pygame.K_q:
            self.room.grid.clear_highlighted_nodes()
            self.change_control_mode(UserControlMode.GRID_CURSOR)
            
    def change_control_mode(self, new_mode: UserControlMode):
        print(f"switching to the mode: {new_mode.name}")
        self.control_mode = new_mode
    
    def handle_cursor_movement(self, key):
        if key == pygame.K_LEFT:
            self.cursor.move(-1, 0)
        elif key == pygame.K_RIGHT:
            self.cursor.move(1, 0)
        elif key == pygame.K_UP:
            self.cursor.move(0, -1)
        elif key == pygame.K_DOWN:
            self.cursor.move(0, 1)

    def handle_keyup(self, key):
        if key == pygame.K_LEFT or key == pygame.K_RIGHT or key == pygame.K_UP or key == pygame.K_DOWN:
            print("keyup happened")