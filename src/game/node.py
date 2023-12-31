import pygame

from game.grid_highlight import HighlightType, convert_highlight_to_color
from game.transform_2d import Transform2D

from utils.constants import PLAYER_SPRITE_SIZE
from utils.position_helpers import calculatePositionFromCoordinates

MIN_NODE_ALPHA = 90
MAX_NODE_ALPHA = 150

class Node():
    def __init__(self, transform : Transform2D, walkable):
        self.current_alpha = MAX_NODE_ALPHA
        self.alpha_increasing = False
        
        self.image = pygame.Surface((PLAYER_SPRITE_SIZE, PLAYER_SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.image.set_alpha(MAX_NODE_ALPHA)
        
        self.x = transform.x
        self.y = transform.y
        self.walkable = walkable
        self.highlight_color = None
        position = calculatePositionFromCoordinates(transform)
        self.rect.x = position.x
        self.rect.y = position.y
        
        self.unit_ref = None
        
    def unit_moved_to_node(self, unit):
        from game.unit import Unit
        self.unit_ref : Unit = unit
    
    def unit_left_node(self):
        self.unit_ref = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def set_highlight(self, highlight: HighlightType):
        self.highlight_color = convert_highlight_to_color(highlight)
        self.image.fill(self.highlight_color)
    
        
    def draw(self, screen):
        if self.highlight_color:
            screen.blit(self.image, self.rect)