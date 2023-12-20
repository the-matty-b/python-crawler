import pygame
from typing import List

from game.grid_highlight import HighlightType
from game.node import Node
from game.transform_2d import Transform2D
from game.unit import Unit, UnitType

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
        self.attackable_nodes: list[Node] = []
        
        for y, row in enumerate(grid):
            row_nodes = []
            for x, value in enumerate(row):
                node = Node(transform=Transform2D(x=x, y=y), walkable=(value == 1))
                row_nodes.append(node)
            self.nodes_grid.append(row_nodes)
        
    
    def get_node(self, x, y) -> Node:
        return self.nodes_grid[y][x]
    
    def set_highlighted_movement_nodes(self, unit: Unit, highlight: HighlightType):
        self.clear_highlighted_nodes()
        explored, visited = explore_paths_dfs(self, unit.node, 0, unit.speed)
        
        self.highlighted_nodes = visited
        
        for node in visited:
            node.set_highlight(highlight)
    
    def clear_highlighted_nodes(self):
        self.highlighted_nodes.clear()
    
    def set_highlighted_attackable_nodes(self, unit: Unit, highlight: HighlightType):
        # can potentiall get rid of these two lines
        self.clear_attackable_nodes()
        explored, attackable = explore_attack_range_dfs(self, unit.node, unit.unit_type, 0, 1)
        
        self.attackable_nodes = attackable
        for node in attackable:
            node.set_highlight(highlight)
        
            
    def find_attackable_nodes(self, unit: Unit):
        self.clear_attackable_nodes()
        explored, attackable = explore_attack_range_dfs(self, unit.node, unit.unit_type, 0, 1)
        
        self.attackable_nodes = attackable
        print("printing attackables list")
        print(self.attackable_nodes)
    
    def clear_attackable_nodes(self):
        self.attackable_nodes.clear()
    
    def update(self):
        for node in self.highlighted_nodes:
            node.update()
        for node in self.attackable_nodes:
            node.update()
    
    def draw(self, screen):
        for node in self.highlighted_nodes:
            node.draw(screen)
            # node.draw()
            
        for node in self.attackable_nodes:
            node.draw(screen)
            # node.draw()
    
def explore_attack_range_dfs(grid: Grid, current_node: Node, unit_type: UnitType, current_distance_travelled, range, attackable=None, current_path=None):
    if current_distance_travelled > range:
        return
    
    if attackable is None:
        attackable = set()

    if current_path is None:
        current_path = []

    if current_node.unit_ref and current_node.unit_ref.unit_type != unit_type and current_distance_travelled > 0:
        attackable.add(current_node)
    
    current_path.append((current_node.x, current_node.y))
    
    # Define the possible moves (up, down, left, right)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # Iterate through possible moves
    for move in moves:
        if 0 <= current_node.x + move[0] < ROOM_GRID_SIZE and 0 <= current_node.y + move[1] < ROOM_GRID_SIZE:
            new_node = grid.get_node(current_node.x + move[0], current_node.y + move[1])
            
            if new_node:
                explore_attack_range_dfs(grid, new_node, unit_type, current_distance_travelled + 1, range, attackable, current_path)

    return current_path, attackable

def explore_paths_dfs(grid: Grid, current_node: Node, current_distance_travelled, max_distance, visited=None, current_path=None):
    
    if current_distance_travelled > max_distance:
        return
    
    if visited is None:
        visited = set()

    if current_path is None:
        current_path = []

    visited.add(current_node)
    current_path.append((current_node.x, current_node.y))
    
    # Define the possible moves (up, down, left, right)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # Iterate through possible moves
    for move in moves:
        if 0 <= current_node.x + move[0] < ROOM_GRID_SIZE and 0 <= current_node.y + move[1] < ROOM_GRID_SIZE:
            new_node = grid.get_node(current_node.x + move[0], current_node.y + move[1])
            
            if new_node.walkable:
                explore_paths_dfs(grid, new_node, current_distance_travelled + 1, max_distance, visited, current_path)

    return current_path, visited