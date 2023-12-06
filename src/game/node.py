import pygame

from game.transform_2d import Transform2D

# from utils.constants import PLAYER_SPRITE_SIZE
# from utils.position_helpers import calculatePositionFromCoordinates


# TODO: Remove GridNode dependency as we're not using the pathfinding library anymore
class Node():
    def __init__(self, transform : Transform2D, walkable):
        self.x = transform.x
        self.y = transform.y
        self.walkable = walkable
        self.color = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def set_color(self, color):
        self.color = color
    