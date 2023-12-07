import pygame

from game.grid_highlight import HighlightType, convert_highlight_to_color
from game.transform_2d import Transform2D

from utils.constants import PLAYER_SPRITE_SIZE
from utils.position_helpers import calculatePositionFromCoordinates


# TODO: Remove GridNode dependency as we're not using the pathfinding library anymore
class Node():
    def __init__(self, transform : Transform2D, walkable):
        self.image = pygame.Surface((PLAYER_SPRITE_SIZE, PLAYER_SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.image.set_alpha(130)
        
        self.x = transform.x
        self.y = transform.y
        self.walkable = walkable
        self.highlight_color = None
        position = calculatePositionFromCoordinates(transform)
        self.rect.x = position.x
        self.rect.y = position.y
        

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def set_highlight(self, highlight: HighlightType):
        self.highlight_color = convert_highlight_to_color(highlight)
        self.image.fill(self.highlight_color)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)