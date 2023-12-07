from enum import Enum

from utils.constants import HIGHLIGHT_BLUE

class HighlightType(Enum):
    BLUE = 1

def convert_highlight_to_color(highlight: HighlightType):
    if (highlight == HighlightType.BLUE):
        return HIGHLIGHT_BLUE