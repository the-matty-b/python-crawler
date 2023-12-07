from game.transform_2d import Transform2D
from utils.constants import PLAYER_SPRITE_SIZE

# This function adjusts for the pixels drawn by the grid map
def calculatePositionForOneDirection(node_value):
    return 1 + (node_value * PLAYER_SPRITE_SIZE) + (2 * node_value)

def calculatePositionFromCoordinates(transform: Transform2D) -> Transform2D:
    return Transform2D(calculatePositionForOneDirection(transform.x), calculatePositionForOneDirection(transform.y))