import pygame, sys, random
from models.Hero import Hero
from models.Soldier import Soldier
from models.Soldiers import Soldiers
from setting import Direction

pygame.init()

# Chiều dài, chiều rộng
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 600
# Khởi tạo màn hình game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Khai báo nhân vật hero
hero = Hero()
first_soldier = Soldier()
soldiers_army:list[Soldier] = [first_soldier]
soldiers_army.append(first_soldier)
# Background game
bg_game = pygame.image.load('./images/bkgd.png')

bg_game_rect = bg_game.get_rect()
bg_game = pygame.transform.scale(bg_game, (bg_game_rect.width, SCREEN_HEIGHT))

scroll_bg = bg_game_rect.x
x_hero_start = hero.rect.x

start_time = 0

running = True
while running:
    x_current_hero = hero.rect.x 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Background
    if hero.direction == Direction.RIGHT and x_hero_start != x_current_hero and hero.rect.x <= SCREEN_WIDTH // 2:
        scroll_bg -= hero.speed
        x_hero_start = x_current_hero
    elif hero.direction == Direction.LEFT and x_hero_start != x_current_hero and hero.rect.x > 0:
        scroll_bg += hero.speed
        # if hero.rect.x > SCREEN_WIDTH // 2:
        #     scroll_bg = min(scroll_bg, bg_game_rect.x - SCREEN_WIDTH)
        x_hero_start = x_current_hero
    screen.blit(bg_game, (scroll_bg, bg_game_rect.y))
    #Vẽ hero
    current = pygame.time.get_ticks()
    if current - start_time >= 5000:
        soldier = Soldier()
        soldiers_army.append(soldier)
        start_time = current
    
    for each_soldier in soldiers_army:
        each_soldier.draw(screen)
    # soldiers_army.draw_soldiers(screen)
    
    hero.draw(screen, soldiers_army, SCREEN_WIDTH)
    #Cập nhật màn hình game
    pygame.display.flip()
pygame.quit()
sys.exit()