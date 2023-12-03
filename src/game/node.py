from game.transform_2d import Transform2D
from pathfinding.core.grid import GridNode

class Node(GridNode):
    def __init__(self, transform : Transform2D, walkable):
        super().__init__(x=transform.x, y = transform.y, walkable=walkable)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))