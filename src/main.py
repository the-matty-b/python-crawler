import pygame
import sys


from game.cursor import Cursor
from game.enemy import Enemy
from game.grid import Grid, TEST_GRID_WITH_OBSTACLES
from game.grid_highlight import HighlightType
from game.gui_manager import GUIManager
from game.player import Player
from game.room import Room
from game.unit import UnitType
from game.unit_action_menu import UnitActionMenu
from game.unit_info import UnitInfo
from game.user_controller import UserController

from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from utils.hot_reload import HotReloadHandler
from utils.console import Console

from watchdog.observers import Observer

def main():
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # FTK OT FE
    pygame.display.set_caption("Crawler")
    
    console = Console()
    
    # Hot Reload Observer
    # observer = Observer()
    # handler = HotReloadHandler(observer)
    # observer.schedule(handler, path="src", recursive=True)
    # observer.start()
    
    grid = Grid(TEST_GRID_WITH_OBSTACLES)
    room = Room(grid)
    cursor = Cursor(0,0)
    
    # unit_info = UnitInfo()
    gui_manager = GUIManager()
    unit_action_menu = UnitActionMenu()
    
    
    user_controller = UserController(cursor, room, gui_manager.unit_info, unit_action_menu)
    
    # -----------------
    pathfinding_grid = room.grid
    
    player = Player(name="Player", strength=14, defense=4, hp=25, speed=4, node=pathfinding_grid.get_node(x=1, y=3), unit_type=UnitType.ALLY)
    
    enemy_1 = Enemy("EnemyStrong", strength=9, defense=3, hp=20, speed=4, node=pathfinding_grid.get_node(x=6, y=2), unit_type=UnitType.ENEMY)
    enemy_2 = Enemy("EnemyDefensive", strength=5, defense=7, hp=25, speed=3, node=pathfinding_grid.get_node(x=5, y=3), unit_type=UnitType.ENEMY)
    enemy_3 = Enemy("EnemyBulky", strength=3, defense=5, hp=30, speed=2, node=pathfinding_grid.get_node(x=6, y=4), unit_type=UnitType.ENEMY)
    # -----------------
    
    room.add_units_to_list([player, enemy_1, enemy_2, enemy_3])
    
    console.log("test1")
    console.log("test2")
    console.log("test3")
    console.log("test4")
    console.log("test5")
    console.log("test6")
    console.log("test7")
    console.log("test8")
    
    
    
    clock = pygame.time.Clock()
    
    while True:
        # Handle events
        user_controller.handle_events()

        # Update game elements
        player.update()
        enemy_1.update()
        enemy_2.update()
        enemy_3.update()
        cursor.update()
        room.update()
        # unit_info.update()

        # Draw the background
        screen.fill(BLACK)

        # Draw game elements
        console.draw(screen)
        room.draw(screen)
        enemy_1.draw(screen)
        enemy_2.draw(screen)
        enemy_3.draw(screen)
        player.draw(screen)
        grid.draw(screen)
        cursor.draw(screen)
        # unit_info.draw(screen)
        gui_manager.draw(screen)
        unit_action_menu.draw(screen)
        
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()