import pygame
from setting import Direction

class Bullet:
    def __init__(self, x, y, direction):
        self.image = pygame.image.load('./images/bullet/0.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 15
        
    def move(self):
        if self.direction == Direction.LEFT:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        
# class Small_Bullet:
#     def __init__(self, x, y):
#         self.image = pygame.image.load('./images/bullet/1.png')
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         # self.direction = direction
#         self.speed = 15
        
#     def move(self):
#         # if self.direction == Direction.LEFT:
#         self.rect.x -= self.speed
#         # else:
#         #     self.rect.x += self.speed
            
#     def draw(self, screen):
#         screen.blit(self.image, self.rect)