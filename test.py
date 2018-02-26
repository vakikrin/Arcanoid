# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Group

#from pygame import mixer

from setting import Settings
from platform import Platform
import gameFunctions as gameF
from ball import Ball


pygame.mixer.init(44100, -16, 2, 2048)#Инициализируем микшер.
pygame.mixer.music.set_volume(0.5)#Устанавливаем грокость - средняя.
#реализовать жизни
#при увеличении счета увеличивается скорость мячика и платформі
#скорость мячика и платформі д.б. пропорциональна
#мячик начинает движение от пробела    

def run_game():
    #Инициализация игры и создание объекта на экране
    #timer = pygame.time.Clock()
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Arcanoid")
    platform = Platform(ai_setting,screen)
    bricks = Group()
    ball = Ball(ai_setting,screen,platform,bricks)
    
    #блок музыки - начало игры
    music_file = "mus/title.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()#Проигрываем5
    #

   
    # Create the wall of bricks.
    gameF.create_wall(ai_setting, screen, platform, bricks)
    
    #Запуск основного цикла в игре
    while True:
    #    timer.tick(240)
        if(ai_setting.life == 0):
            
            break
        gameF.checkEvents(platform) #Функция реагирования на события
        platform.update() #Обновление платформы
        ball.update()   #Обновление мяча

        
        gameF.updateScreen(ai_setting, screen, platform, ball, bricks)#Функция перерисовки экрана
    
    #run_game()
run_game()

