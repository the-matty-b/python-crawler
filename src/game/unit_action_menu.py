import pygame

from typing import List
from enum import Enum
from game.unit import Unit
from game.text import Text
from utils.constants import UNIT_INFO_BOX_HEIGHT, UNIT_INFO_BOX_WIDTH, WHITE, BLACK

# potentially need an enumerations

class UnitAction(Enum):
    WAIT = "Wait"
    ATTACK = "Attack"
    
    # TODO: define unit type elsewhere in src/game/unit.py
    def get_player_actions(can_attack) -> List:
        if (can_attack):
            return [UnitAction.WAIT, UnitAction.ATTACK]
        else:
            return [UnitAction.WAIT]
            
    

class UnitActionMenu(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((UNIT_INFO_BOX_WIDTH, UNIT_INFO_BOX_HEIGHT // 2))
        self.image.fill(BLACK)
        
        self.title = Text("ACTION MENU", size=30)
        
        self.action_text : list[Text] = []
        self.actions : list[UnitAction] = []
        self.menu_cursor_index = 0
        
        pygame.draw.rect(self.image, WHITE, (0, 0, UNIT_INFO_BOX_WIDTH, UNIT_INFO_BOX_HEIGHT // 2), 5)
        
        self.rect = self.image.get_rect()
        self.rect.x = UNIT_INFO_BOX_HEIGHT
        self.rect.y = UNIT_INFO_BOX_HEIGHT // 2
        
        self.cursor_image = ActionMenuCursor(self.rect.x + 17.5, self.rect.y + 58)
        
        self.unit_ref = None
        self.cursor_is_showing = False
        self.can_attack = False
    
    def determine_actions(self, unit: Unit):
        self.actions.clear()
        self.cursor_is_showing = True
        
        if unit.name == "Player":
            for action in UnitAction.get_player_actions(self.can_attack):
                action_text = Text(action.value)
                self.action_text.append(action_text)
                self.actions.append(action)
        
    def set_can_attack(self, can_attack: bool):
        self.can_attack = can_attack

    def clear_menu(self):
        self.cursor_is_showing = False
        for action in self.action_text:
            action.cleanup()
        
        self.action_text.clear()
    
    def select_item(self) -> UnitAction:
        for action in self.actions:
            print(action)
            
        return self.actions[self.menu_cursor_index]
    
    def move(self, direction):
        new_cursor_index = self.menu_cursor_index + direction
        
        if 0 <= new_cursor_index < self.action_text.__len__():
            self.menu_cursor_index = new_cursor_index
            self.cursor_image.update_position(self.cursor_image.rect.y + (direction * 28))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.title.render(screen, self.rect.x + 10, self.rect.y + 10)
        
        if self.cursor_is_showing:
            self.cursor_image.draw(screen)
        
        for i, action_text in enumerate(self.action_text):
            action_text.render(screen, self.rect.x + 40, self.rect.y + 50 + (i * 28))


class ActionMenuCursor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.Surface((10,10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update_position(self, y):
        self.rect.y = y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)