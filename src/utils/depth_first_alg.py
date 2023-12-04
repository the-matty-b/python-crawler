from utils.constants import ROOM_GRID_SIZE

def explore_paths_dfs(grid, current_position, visited=None, current_path=None):
    if visited is None:
        visited = set()

    if current_path is None:
        current_path = []

    x, y = current_position
    visited.add(current_position)
    current_path.append(current_position)

    # Define the possible moves (up, down, left, right)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # Iterate through possible moves
    for move in moves:
        new_position = (x + move[0], y + move[1])

        # Check if the new position is within the grid and hasn't been visited
        if 0 <= new_position[0] < ROOM_GRID_SIZE and 0 <= new_position[1] < ROOM_GRID_SIZE and new_position not in visited:
            explore_paths_dfs(grid, new_position, visited.copy(), current_path.copy())

    return current_path