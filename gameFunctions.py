
# -*- coding: utf-8 -*-
import sys
from time import sleep

import pygame
score = 0;
from brick import Bricks

#t = 0;
#f = pygame.font.SysFont("comicsansms", 72)
#text = f.render(str(t), True, (0, 0, 0))

pygame.mixer.init(44100, -16, 2, 2048)#Инициализируем микшер.
pygame.mixer.music.set_volume(0.5)#Устанавливаем грокость - средняя.


def checkEvents(platform):
    #"Обработка нажатий клавиш и событий мыши"
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            checkEventsKEYDOWN(event,platform)
        elif(event.type == pygame.KEYUP):
            checkEventsKEYUP(event,platform)
        
def checkEventsKEYDOWN(event,platform):
        if event.key == pygame.K_RIGHT:
            platform.movingRight = True
        if event.key == pygame.K_LEFT:
            platform.movingLeft = True
def checkEventsKEYUP(event,platform):
    if event.key == pygame.K_RIGHT:
        platform.movingRight = False
    if event.key == pygame.K_LEFT:
        platform.movingLeft = False


def updateScreen(ai_setting, screen, platform, ball, bricks):
    #'Функция перерисовки экрана'
    screen.fill(ai_setting.bg_color)
    platform.blitme()
    ball.blitme()
    bricks.draw(screen)
    ball.check_ball_brick_collisions()
    #pygame.display.flip()


 ###FIGHT###


##update bricks    






 
 
 ###BRICKS###

def get_number_bricks_x(ai_settings, bricks_width):
    """Determine the number of bricks that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 #* bricks_width
    number_bricks_x = int(available_space_x / (1.6* bricks_width))
    return number_bricks_x

    
def get_number_rows(ai_settings, platform_height, bricks_height):
    """Determine the number of rows of bricks that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (5 * bricks_height) - platform_height)
    number_rows = int(available_space_y / (1.9 * bricks_height))
    return number_rows

     
def create_brick(ai_settings, screen, bricks, brick_number, row_number):
    """Create a bricks, and place it in the row."""
    brick = Bricks(ai_settings, screen)
    bricks_width = brick.rect.width
    brick.x = bricks_width +  1.3*bricks_width * brick_number
    brick.rect.x = brick.x
    brick.rect.y = brick.rect.height + 1.7 * brick.rect.height * row_number
    bricks.add(brick)


def create_wall(ai_settings, screen, platform, bricks):
    """Create a full wall of bricks."""
    # Create an brick, and find number of bricks in a row.
    brick = Bricks(ai_settings, screen)
    number_bricks_x = get_number_bricks_x(ai_settings, brick.rect.width)
    number_rows = get_number_rows(ai_settings, platform.rect.height, brick.rect.height)
    
    # Create the wall of bricks.
    for row_number in range(number_rows):
        for brick_number in range(number_bricks_x):
            create_brick(ai_settings, screen, bricks, brick_number, row_number)


    
