from random import *

class Score:
    
    def __init__(self):
        self.player1score = 0
        self.player2score = 0

    def randomNumber(self,a,b):
        rand = randint(a,b)
        if(randint(1,2) == 1):
            rand = -rand
        return rand

    def checkPoint(self, x, ball, width, height, framerate):
        if(x < 0):
            self.player2score += 1
            ball.xpos = width/2
            ball.ypos = height/2
            ball.xspeed = self.randomNumber(2,3)
            ball.yspeed = self.randomNumber(3,5)
            ball.pause = 2 * framerate
        elif(x > 760):
            self.player2score += 1
            ball.xpos = width/2
            ball.ypos = height/2
            ball.xspeed = self.randomNumber(2,3)
            ball.yspeed = self.randomNumber(3,5)
            ball.pause = 2 * framerate

    def printScore(self, p1, p2):
        n = 0

    def checkWin(self, p1, p2, limit):
        if(p1 == limit):
            return False
        elif(p2 == limit):
            return False 
        else:
            return True
