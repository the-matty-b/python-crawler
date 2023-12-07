import pygame
from typing import List

from game.grid_highlight import HighlightType
from game.node import Node
from game.transform_2d import Transform2D

from utils.constants import ROOM_GRID_SIZE, GRID_NODE_SIZE, HIGHLIGHT_BLUE


TEST_GRID_NO_OBSTACLES = [
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
]
TEST_GRID_WITH_OBSTACLES = [
    [1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1],
    [1,1,0,0,0,1,1],
    [1,1,0,0,0,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
]

class Grid():
    def __init__(self, grid):
        self.nodes_grid : list[list[Node]] = []
        self.highlighted_nodes: list[Node] = []
        
        for y, row in enumerate(grid):
            row_nodes = []
            for x, value in enumerate(row):
                node = Node(transform=Transform2D(x=x, y=y), walkable=(value == 1))
                row_nodes.append(node)
            self.nodes_grid.append(row_nodes)
        
    
    def get_node(self, x, y) -> Node:
        return self.nodes_grid[y][x]
    
    def set_highlighted_nodes(self, nodes: List[Node], highlight: HighlightType):
        self.highlighted_nodes.clear()
        self.highlighted_nodes = nodes
        
        for node in nodes:
            node.set_highlight(highlight)
    
    def draw(self, screen):
        for node in self.highlighted_nodes:
            node.draw(screen)
            
            # pygame.draw.rect(screen, HIGHLIGHT_BLUE, (node.x * GRID_NODE_SIZE, node.y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE))
            # pygame.draw.rect(screen, WHITE, (x * GRID_NODE_SIZE, y * GRID_NODE_SIZE, GRID_NODE_SIZE, GRID_NODE_SIZE), 1)