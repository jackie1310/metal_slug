import pygame 
import random
from models.Small import SmallBullet
from setting import Status_Soldier, Direction

class Soldier:
    def __init__(self):
        self.image = pygame.image.load('./images/left/soldier/freeze/0.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 300
        self.frame = 0
        self.status = Status_Soldier.FREEZE
        self.direction = Direction.LEFT
        self.lst_bullet:list[SmallBullet] = []
        self.time_status_start = 0
        self.time_bullet_start = 0
        self.max_pos = random.randint(600, 1000)
        
    def move(self):
        if self.rect.x <= self.max_pos:
            self.status = Status_Soldier.FREEZE   
        else:
            self.status = Status_Soldier.MOVE 
            self.rect.x -= 1
            
    def attack(self):
        self.status = Status_Soldier.ATTACK
        x_bullet = self.rect.x - self.rect.width // 2
        y_bullet = self.rect.y + self.rect.height // 2
        new_bullet = SmallBullet(x_bullet, y_bullet)
        self.lst_bullet.append(new_bullet)
        
    def update_status(self):
        folder_name_direct = 'left'
        
        folder_status_name = ''
        frame_count = 0
        
        if self.status == Status_Soldier.MOVE:
            folder_status_name = 'move'
            frame_count = 7
        elif self.status == Status_Soldier.ATTACK:
            folder_status_name = 'attack'
            frame_count = 5
        elif self.status == Status_Soldier.DIE:
            folder_status_name = 'die'
            frame_count = 9
        else:
            folder_status_name = 'freeze'
            frame_count = 4
            
        image_src = f'./images/{folder_name_direct}/soldier/{folder_status_name}/{self.frame % frame_count}.png'
        
        self.image = pygame.image.load(image_src)
        
    def draw(self, screen):
        key = pygame.key.get_pressed()
        self.move()
        current_status_time = pygame.time.get_ticks()
        if self.rect.x <= self.max_pos:
            if current_status_time - self.time_bullet_start >= 2000:
                self.attack()
                self.time_bullet_start = current_status_time
            
        for small in self.lst_bullet:
            small.move()
            small.draw(screen)
            if small.rect.x < 0:
                self.lst_bullet.remove(small)
            
            
        screen.blit(self.image, self.rect)
        if current_status_time - self.time_status_start >= 300:
            self.frame += 1
            self.time_status_start = current_status_time
        self.update_status()