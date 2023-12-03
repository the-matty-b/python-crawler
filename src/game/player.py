# src/game/player.py
import pygame
from game.transform_2d import Transform2D
from game.unit import Unit
from utils.constants import GREEN, PLAYER_SPRITE_SIZE, ROOM_GRID_SIZE
from utils.position_helpers import calculatePositionForOneDirection

class Player(Unit):
    def __init__(self, name, strength, defense, hp, speed, grid_x, grid_y):

        # Create a player image (replace "player_image.png" with your actual image file)
        self.image = pygame.Surface((PLAYER_SPRITE_SIZE, PLAYER_SPRITE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        # Set the initial position of the player
        self.transform = Transform2D(grid_x, grid_y)
        self.rect.x = calculatePositionForOneDirection(grid_x)
        self.rect.y = calculatePositionForOneDirection(grid_y)
        
        
        self.name = name
        self.strength = strength
        self.defense = defense
        self.hp = hp
        self.speed = speed
        
    def attack(self, target):
        print(f"{self.name} is attacking!")
    
    def take_damage(self, damage):
        print(f"{self.name} has {self.hp} hp before damage!")
        print(f"{self.name} is taking {damage} damage!")
        damage_done = damage - self.defense if damage - self.defense > 0 else 0
        self.hp -= damage_done
        print(f"{self.name} now has {self.hp} hp after taking {damage_done} damage!")
        
    def get_sprite(self):
        return self.image
            
    def move(self, delta_x, delta_y):
        # Update grid position based on movement
        new_x = self.transform.x + delta_x
        new_y = self.transform.y + delta_y
        
        if 0 <= new_x < ROOM_GRID_SIZE and 0 <= new_y < ROOM_GRID_SIZE:
            self.transform.x = new_x
            self.transform.y = new_y
            self.rect.x = calculatePositionForOneDirection(new_x)
            self.rect.y = calculatePositionForOneDirection(new_y)

    def draw(self, screen):
        # Draw the player on the screen
        screen.blit(self.image, self.rect)
