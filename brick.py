# -*- coding: utf-8 -*- 
import pygame
from pygame.sprite import Sprite

class Bricks(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize and set its starting position."""
        super(Bricks, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the bricks image, and set its rect attribute.
        self.image = pygame.image.load('images/brick.bmp')
        self.rect = self.image.get_rect()

        # Start each new brick near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if bricks is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """Draw the bricks at its current location."""
        self.screen.blit(self.image, self.rect)
