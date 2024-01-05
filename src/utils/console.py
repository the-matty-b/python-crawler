import pygame
from game.unit import Unit
from utils.constants import UNIT_INFO_BOX_HEIGHT, UNIT_INFO_BOX_WIDTH, RED, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT
from game.text import Text

class Console(pygame.sprite.Sprite):
    _instance = None
    
    
    def __new__(self):
        if not self._instance:
            self._instance = super(Console, self).__new__(self)
            self.height = SCREEN_HEIGHT - UNIT_INFO_BOX_HEIGHT
            self.image = pygame.Surface((SCREEN_WIDTH, self.height))
            self.image.fill(BLACK)
            
            self.title = Text("CONSOLE", size=30)
            
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = UNIT_INFO_BOX_HEIGHT
            
            self.text_instances : list[Text] = []
            self.logs : list[str] = []
        return self._instance
    
    def log(self, text: str):
        
        for text_instance in self.text_instances:
            text_instance.cleanup()
        
        self.text_instances.clear()
        
        # pygame.draw.rect(self.image, BLACK, (0, 0, self.rect.width, self.rect.height), 2)
        if text:
            self.logs.append(text)
        
        if self.logs.__len__() > 9:
            self.logs.pop(0)
        

        # Render and blit text lines onto the text box
        for i, log in enumerate(self.logs):
            text_instance = Text(log)
            self.text_instances.append(text_instance)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.title.render(screen, self.rect.x + 10, self.rect.y + 10)
        pygame.draw.rect(self.image, RED, (0, self.height, SCREEN_WIDTH, self.height), 5)
        # pygame.draw.rect(self.image, RED, self.rect, 5)
        
        for i, text_instance in enumerate(self.text_instances):
            text_instance.render(screen, self.rect.x + 10, self.rect.y + 50 + (i * 28))