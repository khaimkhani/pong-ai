import pygame, sys
from pygame.locals import *


class Paddle:
    xpos = 0
    ypos = 0
    length = 0
    width = 0
    speed = 0
    def __init__(self, x, y, l, w, s, n):
        self.ypos = y
        self.xpos = x
        self.length = l
        self.width = w
        self.speed = s
        self.number = n

    def AI_move(self, ypos, dir, playernumber):
        if playernumber == 2:
            if dir == 'UP':
                if (ypos - self.speed < 0):
                    self.ypos = 0
                else:
                    self.ypos -= self.speed
            if dir == 'DOWN':
                if (ypos + self.length + self.speed > 720):
                    self.ypos = 720 - self.length
                else:
                    self.ypos += self.speed
            if dir == 'STAY':
                pass


    def move(self, ypos, k, playernumber):
        if playernumber == 1:
            if k[pygame.K_UP]:
                if(ypos-self.speed < 0):
                    self.ypos = 0
                else:
                    self.ypos -= self.speed
            if k[pygame.K_DOWN]:
                if(ypos+self.length+self.speed > 720):
                    self.ypos = 720-self.length
                else:
                    self.ypos += self.speed

        if playernumber == 2:
            if k[pygame.K_w]:
                if(ypos-self.speed < 0):
                    self.ypos = 0
                else:
                    self.ypos -= self.speed
            if k[pygame.K_s]:
                if(ypos+self.length+self.speed > 720):
                    self.ypos = 720-self.length
                else:
                    self.ypos += self.speed

