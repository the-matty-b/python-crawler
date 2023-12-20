from enum import Enum

from utils.constants import HIGHLIGHT_BLUE, HIGHLIGHT_RED, HIGHLIGHT_YELLOW

class HighlightType(Enum):
    BLUE = 1
    RED = 2
    YELLOW = 3

def convert_highlight_to_color(highlight: HighlightType):
    if (highlight == HighlightType.BLUE):
        return HIGHLIGHT_BLUE
    if (highlight == HighlightType.RED):
        return HIGHLIGHT_RED
    if (highlight == HighlightType.YELLOW):
        return HIGHLIGHT_YELLOW