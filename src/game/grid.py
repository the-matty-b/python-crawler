from game.node import Node
from game.transform_2d import Transform2D

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
        
        print(grid)
        
        for y, row in enumerate(grid):
            row_nodes = []
            for x, value in enumerate(row):
                print(value)
                node = Node(transform=Transform2D(x=x, y=y), walkable=(value == 1))
                print(f"transform: ({x}, {y}) & walkable: {(value == 1)}")
                row_nodes.append(node)
            self.nodes_grid.append(row_nodes)
        
    
    def get_node(self, x, y):
        return self.nodes_grid[y][x]