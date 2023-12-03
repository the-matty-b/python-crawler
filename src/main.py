import pygame
import sys

from game.cursor import Cursor
from game.enemy import Enemy
from game.grids import TEST_GRID_WITH_OBSTACLES
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
    
    player = Player(name="Player", strength=14, defense=4, hp=25, speed=4, grid_x=1, grid_y=3)
    
    # Create some enemies
    enemy_1 = Enemy("EnemyStrong", strength=9, defense=3, hp=20, speed=4, grid_x=6, grid_y=2)
    enemy_2 = Enemy("EnemyDefensive", strength=5, defense=7, hp=25, speed=3, grid_x=5, grid_y=3)
    enemy_3 = Enemy("EnemyBulky", strength=3, defense=5, hp=30, speed=2, grid_x=6, grid_y=4)
    
    room.add_units_to_list([player, enemy_1, enemy_2, enemy_3])
    
    # -----------------
    # pathfinding stuff
    
    pathfinding_grid = Grid(matrix=TEST_GRID_WITH_OBSTACLES)
    
    player_node = Node(Transform2D(player.transform.x, player.transform.y), True)
    enemy_1_node = Node(Transform2D(enemy_1.transform.x, enemy_1.transform.y), True)
    
    test_start = Node(Transform2D(0,0), True)
    test_end = Node(Transform2D(1,0), True)
    
    print("player_node: ", player_node)
    print("enemy_1_node: ", enemy_1_node)
    
    print("Node Details:")
    for row in pathfinding_grid.nodes:
        for node in row:
            print(f"Node ({node.x}:{node.y}) - Walkable: {node.walkable}")
        
    print("Start Node - Walkable:", test_start.walkable)
    print("End Node - Walkable:", test_end.walkable)
    
    finder = AStarFinder()
    
    path, runs = finder.find_path(player_node, enemy_1_node, pathfinding_grid)
    print("path: ", path)
    print("runs: ", runs)
    
    # -----------------
    
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
        
        
        for node in path:
            x = node.x * GRID_NODE_SIZE
            y = node.y * GRID_NODE_SIZE
            rect = pygame.Rect(x, y, GRID_NODE_SIZE, GRID_NODE_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), rect)
            pygame.draw.rect(screen, (0, 0, 255), rect, 2)
            
            # pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(node.x * GRID_NODE_SIZE, node.y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE))
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()