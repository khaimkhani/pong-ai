import pygame, sys

class Ball:
    xspeed = 0
    yspeed = 0
    xpos = 0
    ypos = 0
    size = 0
    pause = 0
    def __init__(self, x, y, xspeed, yspeed, size):
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xpos = x
        self.ypos = y
        self.size = size

    def move(self, x, y, xspeed, yspeed, paddle1, paddle2):
        if(self.pause > 0):
            self. pause -= 1
            return
        
        # Check for bouncing on the top and bottom wall.
        if(y + yspeed < 0):
            self.ypos = 0
            self.yspeed = -yspeed
            
        elif(y + yspeed > 720):
            self.ypos = 720
            self.yspeed = -yspeed

        else:
            self.ypos += yspeed

        # Check for bouncing on paddle.
        if(x < 40 and (paddle1.ypos <= y <= (paddle1.ypos + paddle1.length))):
            self.xpos = 40
            self.xspeed = -xspeed
            self.xspeed += .5
            
        elif(x > 720 and (paddle2.ypos <= y <= (paddle2.ypos + paddle2.length))):
            self.xpos = 720
            self.xspeed = -xspeed
            self.xspeed -= .5

        else:
            self.xpos += xspeed

    
