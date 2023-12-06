from game.transform_2d import Transform2D

# TODO: Remove GridNode dependency as we're not using the pathfinding library anymore
class Node():
    def __init__(self, transform : Transform2D, walkable):
        self.x =transform.x
        self.y = transform.y
        self.walkable=walkable

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))