from game.node import Node
from utils.constants import PLAYER_SPRITE_SIZE

# This function adjusts for the pixels drawn by the grid map
def calculatePositionForOneDirection(Node_value):
    return 1 + (Node_value * PLAYER_SPRITE_SIZE) + (2 *Node_value)

def calculatePositionFromCoordinates(Node: Node):
    return (calculatePositionForOneDirection(Node.x), calculatePositionForOneDirection(Node.y))