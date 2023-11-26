# src/game/player.py
import pygame
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, ROOM_GRID_SIZE, GRID_NODE_SIZE

class Room(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

    # def update(self):

    def draw(self, screen):
        grid = [[0] * ROOM_GRID_SIZE for _ in range(ROOM_GRID_SIZE)]
        # Draw the room on the screen
        for x in range(ROOM_GRID_SIZE):
            for y in range(ROOM_GRID_SIZE):
                pygame.draw.rect(screen, WHITE, (x * GRID_NODE_SIZE, y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE), 1)
