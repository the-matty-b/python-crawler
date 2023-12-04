import pygame
from typing import Union, List
from game.node import Node
from game.transform_2d import Transform2D
from game.unit import Unit
from utils.constants import WHITE, DARK_GRAY, ROOM_GRID_SIZE, GRID_NODE_SIZE

class Room(pygame.sprite.Sprite):
    
    def __init__(self, obstacle_grid):
        self.units : list[Unit] = []
        self.obstacle_grid = obstacle_grid
        
        self.nodes = pygame.sprite.Group()

        for y, row in enumerate(obstacle_grid):
            for x, value in enumerate(row):
                node = pygame.sprite.Sprite()
                node.rect = pygame.Rect(x * GRID_NODE_SIZE, y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE)
                node.walkable = (value == 1)
                self.nodes.add(node)

    # def update(self):
    
    def check_space_for_unit(self, node: Node):
        unit_to_return = None
        
        for unit in self.units:
            if unit.node == node:
                unit_to_return = unit
                break
        
        return unit_to_return
        
    def add_units_to_list(self, units: Union[Unit, List[Unit]]):
        if isinstance(units, list):
            for unit in units:
                self.units.append(unit)
        else:
            self.units.append(units)

    def draw(self, screen):
        grid = [[0] * ROOM_GRID_SIZE for _ in range(ROOM_GRID_SIZE)]
        # Draw the room on the screen
        for x in range(ROOM_GRID_SIZE):
            for y in range(ROOM_GRID_SIZE):
                if self.obstacle_grid[y][x] == 1:
                    pygame.draw.rect(screen, WHITE, (x * GRID_NODE_SIZE, y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE), 1)
                else:
                    pygame.draw.rect(screen, DARK_GRAY, (x * GRID_NODE_SIZE, y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE))

