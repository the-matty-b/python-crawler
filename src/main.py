import pygame
import sys

from game.cursor import Cursor
from game.enemy import Enemy
from game.grid import TEST_GRID_WITH_OBSTACLES
from game.node import Node
from game.player import Player
from game.room import Room
from game.text import Text
from game.transform_2d import Transform2D
from game.unit_info import UnitInfo
from game.user_controller import UserController

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GRID_NODE_SIZE
from utils.hot_reload import HotReloadHandler

from watchdog.observers import Observer

def main():
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # FTK OT FE
    pygame.display.set_caption("Crawler")
    
    # Hot Reload Observer
    # observer = Observer()
    # handler = HotReloadHandler(observer)
    # observer.schedule(handler, path="src", recursive=True)
    # observer.start()

    room = Room(TEST_GRID_WITH_OBSTACLES)
    cursor = Cursor(0,0)
    unit_info = UnitInfo()
    user_controller = UserController(cursor, room, unit_info)
    
    
    # -----------------
    # old pathfinding stuff still included
    # TODO: Remove old 'pathfinding' library and replace with my own node.
    pathfinding_grid = room.grid
    
    player = Player(name="Player", strength=14, defense=4, hp=25, speed=4, node=pathfinding_grid.get_node(x=1, y=3))
    
    enemy_1 = Enemy("EnemyStrong", strength=9, defense=3, hp=20, speed=4, node=pathfinding_grid.get_node(x=6, y=2))
    enemy_2 = Enemy("EnemyDefensive", strength=5, defense=7, hp=25, speed=3, node=pathfinding_grid.get_node(x=5, y=3))
    enemy_3 = Enemy("EnemyBulky", strength=3, defense=5, hp=30, speed=2, node=pathfinding_grid.get_node(x=6, y=4))
    # -----------------
    
    
    room.add_units_to_list([player, enemy_1, enemy_2, enemy_3])
    
    
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
        unit_info.update()

        # Draw the background
        screen.fill(BLACK)

        # Draw game elements
        room.draw(screen)
        player.draw(screen)
        enemy_1.draw(screen)
        enemy_2.draw(screen)
        enemy_3.draw(screen)
        cursor.draw(screen)
        unit_info.draw(screen)
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()