import pygame
from game.unit import Unit
from utils.constants import UNIT_INFO_BOX_HEIGHT, UNIT_INFO_BOX_WIDTH, RED, BLACK
from game.text import Text

class EnemyInfo(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((UNIT_INFO_BOX_WIDTH // 2, UNIT_INFO_BOX_HEIGHT // 2))
        self.image.fill(BLACK)
        
        self.title = Text("ENEMY INFO", size=24)
        
        self.rect = self.image.get_rect()
        self.rect.x = UNIT_INFO_BOX_HEIGHT + UNIT_INFO_BOX_WIDTH // 2
        self.rect.y = 0
        
        self.unit_ref = None
        self.text_instances : list[Text] = []
        
        self.isVisible = False
    
    def show(self):
        self.isVisible = True
        self.image.fill(BLACK)
        pygame.draw.rect(self.image, RED, (0, 0, UNIT_INFO_BOX_WIDTH // 2, UNIT_INFO_BOX_HEIGHT // 2), 5)
    
    def hide(self):
        self.isVisible = False
        self.image.fill(BLACK)
        
    def update_unit_info(self, target: Unit):
        self.unit_ref = target
        
        for text_instance in self.text_instances:
            text_instance.cleanup()
        
        self.text_instances.clear()
        
        # pygame.draw.rect(self.image, BLACK, (0, 0, self.rect.width, self.rect.height), 2)
        
        if self.unit_ref is not None:
            # Draw unit information
            text_lines = [
                f"Name: {self.unit_ref.name}",
                f"HP: {self.unit_ref.hp}",
                f"Strength: {self.unit_ref.strength}",
                f"Defense: {self.unit_ref.defense}",
                f"Speed: {self.unit_ref.speed}",
                # Add more unit information as needed
            ]

            # Render and blit text lines onto the text box
            for i, line in enumerate(text_lines):
                text_instance = Text(line)
                self.text_instances.append(text_instance)

    def draw(self, screen):
        if not self.isVisible: return
        
        screen.blit(self.image, self.rect)
        self.title.render(screen, self.rect.x + 10, self.rect.y + 10)
        
        for i, text_instance in enumerate(self.text_instances):
            text_instance.render(screen, self.rect.x + 10, self.rect.y + 50 + (i * 28))