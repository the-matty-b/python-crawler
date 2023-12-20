import pygame

from game.node import Node
from game.transform_2d import Transform2D
from game.unit import Unit, UnitType
from utils.constants import RED, PLAYER_SPRITE_SIZE
from utils.position_helpers import calculatePositionForOneDirection

class Enemy(Unit):
    def __init__(self, name, strength, defense, hp, speed, node: Node, unit_type: UnitType):
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
        self.unit_type = unit_type
        
        node.unit_moved_to_node(self)
        
    def attack(self, target):
        print(f"{self.name} is attacking!")
        target.take_damage(self.strength)
    
    def take_damage(self, damage):
        print(f"{self.name} has {self.hp} hp before damage!")
        print(f"{self.name} is taking {damage} damage before defenses!")
        damage_done = damage - self.defense if damage - self.defense > 0 else 0
        self.hp -= damage_done
        print(f"{self.name} now has {self.hp} hp after taking {damage_done} damage!")
        if self.hp <= 0:
            print("need to kill unit")
    
    def get_sprite(self):
        return self.image        
    
    def move(self, node: Node):
        self.node.__setattr__("walkable", True)
        self.node.unit_left_node()
        node.__setattr__("walkable", False)
        node.unit_moved_to_node(self)
        self.node = node
        self.rect.x = calculatePositionForOneDirection(node.x)
        self.rect.y = calculatePositionForOneDirection(node.y)
        
    def draw(self, screen):
        # Draw the player on the screen
        screen.blit(self.image, self.rect)
