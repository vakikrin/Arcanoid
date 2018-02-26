# -*- coding: cp1251 -*-
import pygame
import math
import random
import time
import gameFunctions as gameF

#clock = pygame.time.Clock()
pygame.mixer.init(44100, -16, 2, 2048)#Инициализируем микшер.
pygame.mixer.music.set_volume(0.5)#Устанавливаем грокость - средняя.
     
    
class Ball():
    def __init__(self,ai_setting,screen,platform,brick):
        self.image = pygame.image.load('images/ball.gif')
        self.brick = brick
        self.rect = self.image.get_rect()
        self.screen=screen
        self.screen_rect = screen.get_rect()
        self.platform = platform
        self.rect.centerx = self.platform.rect.centerx
        self.rect.centery = self.platform.rect.top - 18
        self.ai_setting = ai_setting
        self.color = ai_setting.ballColor
        self.ballSpeedFactor = ai_setting.ballSpeedFactor
        self.colision = False
        self.KoofY = float(-1)
        self.KoofX = float(-1)
        self.tmp1 = float(self.rect.centery)
        self.tmp2 = float(self.rect.centerx)
        self.font = pygame.font.SysFont("comicsansms", 40)
        self.font1 = pygame.font.SysFont("comicsansms", 100)
        self.t = 0
        self.text = self.font.render("Score: "+str(self.t), True, (255, 255, 255))
        #self.t_l = 1
        self.text_l = self.font.render("Lives: "+str(self.ai_setting.life), True, (255, 255, 255))
        self.can_play = True;
        self.game_stop = self.font.render((""), True, (255, 255, 255))
           
        print(self.rect.bottom)
        self.music_file1 = "mus/lostball.mp3"
        self.music_file2 = "mus/ball.mp3"

    def update(self):
        #print('self.centerx_ball =' , self.centerx)
        #print('self.centery_ball =',self.centery)
        #print(self.platform.rect.top)

        #счет
        self.screen.blit(self.text,(self.ai_setting.screen_width-100 - self.text.get_width() // 2, 420))
        self.screen.blit(self.text_l,(self.ai_setting.screen_width-100 - self.text_l.get_width() // 2, 500))
        self.screen.blit(self.game_stop,(self.ai_setting.screen_width-100 - self.text_l.get_width() // 2, 250))
           
        pygame.display.flip()
        #конец счета
        
        
        if(self.rect.left <= self.screen_rect.left):
            self.KoofX*=-1.0
        if(self.rect.top <= self.screen_rect.top):
            self.KoofY*=-1.0
        if(self.rect.right >= self.screen_rect.right):
            print("3")
            self.KoofX*=-1.0
        if((self.rect.bottom >= self.platform.rect.top) and (self.rect.right >= self.platform.rect.left and self.rect.left <= self.platform.rect.right)):
            #self.KoofX = ((self.platform.rect.centerx-self.rect.centerx)*1.0)/(self.platform.rect.right - self.platform.rect.left)
            #self.KoofY = ((self.platform.rect.centerx-self.rect.centerx)*1.0)/(self.platform.rect.right - self.platform.rect.left)
            print("4")
            self.KoofY = -math.sin(((self.rect.right-self.platform.rect.left)*1.44*3.14+int((random.random()*10)))/180)
            self.KoofX = -math.cos(((self.rect.right-self.platform.rect.left)*1.44*3.14+int((random.random()*10)))/180)
    
        #if(self.rect.bottom > self.platform.rect.top and (self.rect.right >= self.platform.rect.left or self.rect.left >= self.platform.rect.right)):
         #   if(self.can_play==True):
          #      print("5")
           #     pygame.mixer.music.load(self.music_file1)
            #    pygame.mixer.music.play()
             #   self.ch_lives(-1)
             #   self.can_play = False #пока такое условие
        self.tmp1 += self.KoofY*self.ballSpeedFactor
        self.tmp2 += self.KoofX*self.ballSpeedFactor
        self.rect.centerx = int(self.tmp2)
        self.rect.centery = int(self.tmp1)
        if(self.rect.centery > self.ai_setting.screen_height):
            #self.ai_setting.life -=1
            self.ch_lives(-1)
            self.rect.centerx = self.platform.rect.centerx
            self.rect.centery = self.platform.rect.top -18
            self.KoofY = float(-1)
            self.KoofX = float(-1)
            self.tmp1 = float(self.rect.centery)
            self.tmp2 = float(self.rect.centerx)
            self.screen.fill(self.ai_setting.bg_color)
            self.platform.blitme()
            self.blitme()
            self.brick.draw(self.screen)
            self.screen.blit(self.text,(self.ai_setting.screen_width-100 - self.text.get_width() // 2, 420))
            self.screen.blit(self.text_l,(self.ai_setting.screen_width-100 - self.text_l.get_width() // 2, 500))
            self.screen.blit(self.game_stop,(self.ai_setting.screen_width-700 - self.text_l.get_width() // 2, 300))
            pygame.display.flip()
            time.sleep(2)
        #gameF.print_score(self.screen, self.ai_setting.screen_width, self.text)
       



    def ch_score(self, val):
        self.t += val
        self.text = self.font.render("Score: "+ str(self.t), True, (255, 255, 255))

    def ch_lives(self, val):
        self.ai_setting.life += val
        print("DSA")
        if(self.ai_setting.life == 0):
            print("DSA2")
            self.game_stop = self.font1.render((" Game over"), True, (255, 0, 0))
           # 
            #pygame.display.flip()
        else:
            self.game_stop = self.font.render((""), True, (255, 255, 255))
           
        self.text_l = self.font.render("Lives: "+ str(self.ai_setting.life), True, (255, 255, 255))
       
    def check_ball_brick_collisions(self):
    # Remove any bullets and aliens that have collided.
        if(pygame.sprite.spritecollide(self,self.brick, True)):
            self.KoofY*=-1
            self.ch_score(1)
            pygame.mixer.music.load(self.music_file2)
            pygame.mixer.music.play()
            #gameF.print_score(self.screen, self.ai_setting.screen_width, self.text)
        if len(self.brick) == 0:
        #create new wall
            gameF.create_wall(self.ai_setting, self.screen, self.platform, self.brick)
            self.ballSpeedFactor = self.ballSpeedFactor + self.ai_setting.ballSpeedAcceleration
        
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
