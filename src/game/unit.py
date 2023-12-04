import pygame
from abc import ABC, abstractmethod
from game.node import Node

class Unit(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, name, strength, defense, hp, speed, node: Node):
        pass

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass
    
    @abstractmethod
    def get_sprite(self):
        pass