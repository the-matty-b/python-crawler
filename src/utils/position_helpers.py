from utils.constants import PLAYER_SPRITE_SIZE

# This function adjusts for the pixels drawn by the grid map
def calculatePositionFromCoordinates(coordinate):
    return 1 + (coordinate * PLAYER_SPRITE_SIZE) + (2 * coordinate)