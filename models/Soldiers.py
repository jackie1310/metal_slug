from models.Soldier import Soldier

class Soldiers:
    def __init__ (self):
        self.soldier_lst:list[Soldier] = []
    
    def add_soldier(self, soldier: Soldier):
        self.soldier_lst.append(soldier)
        
    def draw_soldiers(self, screen):
        for each_soldier in self.soldier_lst:
            each_soldier.draw(screen)