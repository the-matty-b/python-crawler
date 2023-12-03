import pygame
from utils.constants import WHITE

DEFAULT_FONT_PATH = pygame.font.match_font("Arial")
DEFAULT_FONT_SIZE = 24

class Text:
    def __init__(self, text, font_path=DEFAULT_FONT_PATH, size=DEFAULT_FONT_SIZE, color=WHITE):
        self.font = pygame.font.Font(font_path, size)
        self.text_surface = self.font.render(text, True, color)
        self.rect = self.text_surface.get_rect()

    def render(self, surface, x, y):
        surface.blit(self.text_surface, (x, y))

    def cleanup(self):
        self.text_surface = None