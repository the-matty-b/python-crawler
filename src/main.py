import pygame
import sys
from game.cursor import Cursor
from game.enemy import Enemy
from game.player import Player
from game.user_controller import UserController
from game.room import Room
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
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

    # Create an instance of the Player class
    cursor = Cursor(0,0)
    user_controller = UserController(cursor)
    player = Player(name="Player", strength=14, defense=4, hp=25, speed=4, grid_x=1, grid_y=3)
    
    player.take_damage(9)
    
    enemy_1 = Enemy("EnemyStrong", strength=9, defense=3, hp=20, speed=4, grid_x=5, grid_y=2)
    enemy_2 = Enemy("EnemyDefensive", strength=5, defense=7, hp=25, speed=3, grid_x=4, grid_y=3)
    enemy_3 = Enemy("EnemyBulky", strength=3, defense=5, hp=30, speed=2, grid_x=5, grid_y=4)
    
    # Create an instance of the Room class
    room = Room()

    clock = pygame.time.Clock()
    
    

    while True:
        user_controller.handle_events()

        # Update game elements
        player.update()
        enemy_1.update()
        enemy_2.update()
        enemy_3.update()
        
        cursor.update()

        # Draw the background
        screen.fill(BLACK)

        # Draw game elements
        room.draw(screen)
        cursor.draw(screen)
        player.draw(screen)
        enemy_1.draw(screen)
        enemy_2.draw(screen)
        enemy_3.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()