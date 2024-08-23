import pygame
from setting import Direction, Status_Hero
from models.Bullet import Bullet
from models.Soldiers import Soldiers

class Hero:
    def __init__(self):
        self.image = pygame.image.load('./images/right/hero/freeze/0.png')
        self.rect = self.image.get_rect()
        self.rect.y = 300
        self.frame = 0
        self.status = Status_Hero.FREEZE
        self.direction = Direction.RIGHT
        self.lst_bullet:list[Bullet] = []
        self.time_status_start = 0
        self.speed = 1
        
    def move(self, direction):
        self.direction = direction
        self.status = Status_Hero.MOVE
        if self.direction == Direction.LEFT:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
    def attack(self):
        self.status = Status_Hero.ATTACK
        
        #Tạo ra một viên đạn mới nạp vào self.list_bullet
        if self.direction == Direction.RIGHT:
            x_bullet = self.rect.x + self.rect.width 
            y_bullet = self.rect.y + self.rect.height // 2
            new_bullet = Bullet(x_bullet, y_bullet, Direction.RIGHT)
            self.lst_bullet.append(new_bullet)
        else:
            x_bullet = self.rect.x
            y_bullet = self.rect.y + self.rect.height // 2
            new_bullet = Bullet(x_bullet, y_bullet, Direction.LEFT)
            self.lst_bullet.append(new_bullet)
    
    def jump(self):
        pass
    
    def update_status(self):
        #Xử lý folder hướng
        folder_name_direct = ''
        if self.direction == Direction.LEFT:
            folder_name_direct = 'left'
        else:
            folder_name_direct = 'right'
        #Xử lý folder status
        folder_status_name = ''
        frame_count = 0
        
        if self.status == Status_Hero.MOVE:
            folder_status_name = 'move'
            frame_count = 4
        elif self.status == Status_Hero.ATTACK:
            folder_status_name = 'attack'
            frame_count = 4
        elif self.status == Status_Hero.DIE:
            folder_status_name = 'die'
            frame_count = 19
        else:
            folder_status_name = 'freeze'
            frame_count = 3
            
        image_src = f'./images/{folder_name_direct}/hero/{folder_status_name}/{self.frame % frame_count}.png'
        
        self.image = pygame.image.load(image_src)
        
        
    def draw(self, screen, soldiers_army, SCREEN_WIDTH):
        
        #Xử lý di chuyển
        key = pygame.key.get_pressed()
        
        # w: đi lên, x: xuống, a:left, d:right, j:attack, k:jump
        if key[pygame.K_a] and self.rect.x > 0:
            self.move(Direction.LEFT)
        elif key[pygame.K_d] and self.rect.x <= SCREEN_WIDTH - self.rect.width:
            self.move(Direction.RIGHT)
        else:
            #Nếu người dùng không nhấn phím nào thì trả về trạng thái đứng yên
            self.status = Status_Hero.FREEZE

        #Xử lý bắn đạn
        if key[pygame.K_j]:
            self.attack()
        
        #Vẽ đạn
        for bullet in self.lst_bullet:
            bullet.move()
            bullet.draw(screen)
            if bullet.rect.x > screen.get_width() and bullet.direction == Direction.RIGHT:
                self.lst_bullet.remove(bullet)
            elif bullet.rect.x < 0 and bullet.direction == Direction.LEFT:
                self.lst_bullet.remove(bullet)

        
        screen.blit(self.image, self.rect)
        #Update status cập nhật frame
        current_status_time = pygame.time.get_ticks()
        if current_status_time - self.time_status_start >= 300:
            self.frame += 1
            self.time_status_start = current_status_time
        self.update_status()