# -*- coding: utf-8 -*-
import pygame

class Platform():
    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        #Загрузка картинкии для платформы
        self.image = pygame.image.load('images/platform.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.movingRight = False
        self.movingLeft = False
        self.cooficient = ai_setting.speefFactor
    #    self.speedUp = float(ai_setting.speedUp)
    def update(self):
        self.moving()
    def moving(self):
        if (self.movingRight == True) :
            if(self.rect.right >= self.screen_rect.right):
            #    print("self.screen_rect.right=",self.screen_rect.right)
                self.rect.centerx = self.screen_rect.right - (self.rect.right-self.rect.centerx)
            #    self.cooficient = float(self.ai_setting.speefFactor)
            else:
                self.rect.centerx += self.cooficient
                #self.cooficient+=self.speedUp
                #print(self.cooficient)
        if (self.movingLeft == True) :
            if(self.rect.left <= 0):
                self.rect.centerx = 0+(-self.rect.left)+self.rect.centerx
            #    self.cooficient=float(self.ai_setting.speefFactor)
            else:
                self.rect.centerx -= self.cooficient
            #    self.cooficient+=self.speedUp
        #if(self.movingLeft == False and self.movingRight == False):
            #self.cooficient=float(self.ai_setting.speefFactor)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #print(self.rect.right-self.rect.left)
