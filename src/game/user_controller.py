# src/game/player.py
import pygame
from game.cursor import Cursor
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, GREEN, PLAYER_SPRITE_SIZE, GRID_NODE_SIZE, ROOM_GRID_SIZE
from utils.position_helpers import calculatePositionFromCoordinates

class UserController():
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

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
        print('we are receiving a keydown event')
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