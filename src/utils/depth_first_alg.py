from game.grid import Grid
from game.node import Node
from utils.constants import ROOM_GRID_SIZE

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
            
            if new_node not in visited and new_node.walkable:
                explore_paths_dfs(grid, new_node, current_distance_travelled + 1, max_distance, visited, current_path)


    return current_path, visited