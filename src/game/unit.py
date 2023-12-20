import pygame
from abc import ABC, abstractmethod
from enum import Enum
from game.node import Node

class UnitType(Enum):
    ALLY = 1
    ENEMY = 2

class Unit(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, name, strength, defense, hp, speed, node: Node, unit_type: UnitType):
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