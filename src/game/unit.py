import pygame
from abc import ABC, abstractmethod

class Unit(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, name, strength, defense, hp, speed, pos_x, pos_y):
        pass

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass