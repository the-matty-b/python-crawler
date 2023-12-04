import pygame

from game.node import Node
from game.transform_2d import Transform2D
from game.unit import Unit
from utils.constants import RED, PLAYER_SPRITE_SIZE
from utils.position_helpers import calculatePositionForOneDirection

class Enemy(Unit):
    def __init__(self, name, strength, defense, hp, speed, node: Node):
        node.__setattr__("walkable", False)

        self.image = pygame.Surface((PLAYER_SPRITE_SIZE, PLAYER_SPRITE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.node = node
        self.rect.x = calculatePositionForOneDirection(node.x)
        self.rect.y = calculatePositionForOneDirection(node.y)
        
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
    
    def move(self, node: Node):
        # Update grid position based on movement
        self.node.__setattr__("walkable", True)
        node.__setattr__("walkable", False)
        self.node = node
        self.rect.x = calculatePositionForOneDirection(node.x)
        self.rect.y = calculatePositionForOneDirection(node.y)
        
        # if 0 <= new_x < ROOM_GRID_SIZE and 0 <= new_y < ROOM_GRID_SIZE:
        #     self.node.x = new_x
        #     self.node.y = new_y
        #     self.rect.x = calculatePositionForOneDirection(new_x)
        #     self.rect.y = calculatePositionForOneDirection(new_y)

    def draw(self, screen):
        # Draw the player on the screen
        screen.blit(self.image, self.rect)
