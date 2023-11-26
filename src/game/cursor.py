# src/game/player.py
import pygame
from game.transform_2D import Transform2D
from utils.constants import WHITE, PLAYER_SPRITE_SIZE, ROOM_GRID_SIZE
from utils.position_helpers import calculatePositionFromCoordinates

MAX_CURSOR_ALPHA = 201
MIN_CURSOR_ALPHA = 111


class Cursor(pygame.sprite.Sprite):
    def __init__(self, grid_x, grid_y):
        self.current_alpha = MAX_CURSOR_ALPHA

        # Create a player image (replace "player_image.png" with your actual image file)
        self.image = pygame.Surface((PLAYER_SPRITE_SIZE, PLAYER_SPRITE_SIZE))
        self.image.fill(WHITE)
        self.image.set_alpha(self.current_alpha)
        self.rect = self.image.get_rect()

        # Set the initial position of the player
        self.transform = Transform2D(grid_x, grid_y)
        self.rect.x = calculatePositionFromCoordinates(grid_x)
        self.rect.y = calculatePositionFromCoordinates(grid_y)
        self.alpha_increasing = False
        
    def move(self, delta_x, delta_y):
        # Update grid position based on movement
        new_x = self.transform.x + delta_x
        new_y = self.transform.y + delta_y
        
        if 0 <= new_x < ROOM_GRID_SIZE and 0 <= new_y < ROOM_GRID_SIZE:
            self.transform.x = new_x
            self.transform.y = new_y
            self.rect.x = calculatePositionFromCoordinates(new_x)
            self.rect.y = calculatePositionFromCoordinates(new_y)

    def update(self):
        self.update_alpha()
    
    def draw(self, screen):
        # Draw the player on the screen
        screen.blit(self.image, self.rect)

    def update_alpha(self):
        self.current_alpha = self.current_alpha + 1 if self.alpha_increasing else self.current_alpha - 1
        if self.current_alpha <= MIN_CURSOR_ALPHA:
            self.alpha_increasing = True
        elif self.current_alpha >= MAX_CURSOR_ALPHA:
            self.current_alpha = MAX_CURSOR_ALPHA
            self.alpha_increasing = False
        self.image.set_alpha(self.current_alpha)