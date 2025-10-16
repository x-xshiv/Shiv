import sys
import numpy as np
import pandas as pd
import pygame as pg
import time as t



class AlienInvasion:
    def __init__(self):

        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    


    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()
            
    

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    return
    

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pg.display.flip()
        





class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)


class Ship:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pg.transform.scale(pg.image.load('images/ship.png'), (80 , 60))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    

    def blitme(self):
        self.screen.blit(self.image, self.rect)



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

        

