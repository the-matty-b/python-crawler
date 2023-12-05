import pygame
from typing import Union, List
from game.node import Node
from game.transform_2d import Transform2D
from game.unit import Unit
from utils.constants import WHITE, DARK_GRAY, ROOM_GRID_SIZE, GRID_NODE_SIZE

# Make this the grid class?
class Room(pygame.sprite.Sprite):
    
    def __init__(self, grid):
        self.units : list[Unit] = []
        self.grid : list[list[Node]] = []

        for y, row in enumerate(grid):
            row_nodes = []
            for x, value in enumerate(row):
                row_nodes.append(Node(transform=Transform2D(x=x, y=y), walkable=(value == 1)))
            self.grid.append(row_nodes)

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
        
        # Draw the room on the screen
        for x in range(ROOM_GRID_SIZE):
            for y in range(ROOM_GRID_SIZE):
                if self.grid[y][x].walkable:
                    pygame.draw.rect(screen, WHITE, (x * GRID_NODE_SIZE, y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE), 1)
                else:
                    pygame.draw.rect(screen, DARK_GRAY, (x * GRID_NODE_SIZE, y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE))

