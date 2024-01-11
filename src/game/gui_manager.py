import pygame

from game.enemy_info import EnemyInfo
from game.unit import Unit
from game.unit_info import UnitInfo

class GUIManager():
    _instance = None
    
    
    def __new__(self):
        if not self._instance:
            self._instance = super(GUIManager, self).__new__(self)
            self.unit_info = UnitInfo()
            self.enemy_info = EnemyInfo()
             
        return self._instance
    
    def draw(self, screen):
        self.unit_info.draw(screen)
        self.enemy_info.draw(screen)
    
    # def update(self):
    #     self.unit_info.update()
    #     self.enemy_info.update()
        
    def show_enemy_info(self, unit: Unit):
        self.enemy_info.update_unit_info(unit)
        self.enemy_info.show()
        self.unit_info.change_size(True)
    
    def hide_enemy_info(self):
        self.enemy_info.hide()
        self.unit_info.change_size(False)