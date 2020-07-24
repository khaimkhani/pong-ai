import pygame, sys
from pygame.locals import *
from Paddle import *
from Ball import *
from PayAI import *
from Scorer import *
from genetic_process import *
import time

from random import randint

#Start Pygame
pygame.init()
pygame.font.init()
running = True
limit = 1

#Variables.
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 720
FRAMERATE = 60
BG = pygame.image.load("assets/pongBG.jpg")
FONT = pygame.font.Font("assets/munro.ttf", 30)

#Create screen, clock, and name window.
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('PONG')
clock = pygame.time.Clock()

# Create the scorer
scorer = Score()

# Create the Paddles(x,y,length,width,speed,playernumber).
paddle2 = Paddle(20, 10, 100, 20, 10, 2)
paddle1 = Paddle(740, 10, 100, 20, 10, 1)

# Spawn the Ball(x, y, xspeed, yspeed, size) at a random speed and direction.
randomx = randint(2,3)
randomy = randint(3,5)
if(randint(0,1) == 1):
    randomx = -randomx
if(randint(0,1) == 1):
    randomy = -randomy
pongball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, randomx, randomy, 20)

# Draw a padle on the screen.
def drawPaddle(x, y, length, width):
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (x,y,length,width))

# Draw the ball on the screen.
def drawBall(x, y, size):
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (x,y,size,size))

generation = Genes(10)


# Game Loop
while True:
    start = time.time()
    if generation.size == 0:
        generation.new_gen()
    bott = generation.offering()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:

                total = time.time() - start
                bott.set_fitness(total)
                bott = generation.offering()
                pygame.quit()
                #pygame.quit()
                #sys.exit()
                #pygame.font.init()
                #running = True
                #limit = 1


        info = [pongball.xpos, pongball.ypos, pongball.xspeed, pongball.yspeed, paddle2.ypos, paddle2.xpos]
        #Checking Variables
        k = pygame.key.get_pressed()
        paddle1.move(paddle1.ypos, k, paddle1.number)
        paddle2.AI_move(paddle2.ypos, bott.think(info), paddle2.number)
        paddle2.move(paddle2.ypos, k, paddle2.number)
        pongball.move(pongball.xpos, pongball.ypos, pongball.xspeed, pongball.yspeed, paddle2, paddle1)

        # Drawing screen
        DISPLAYSURF.blit(BG, (0,0))

        # Draw ball and paddles
        drawBall(pongball.xpos, pongball.ypos, pongball.size)
        drawPaddle(paddle1.xpos, paddle1.ypos, paddle1.width, paddle1.length)
        drawPaddle(paddle2.xpos, paddle2.ypos, paddle2.width, paddle2.length)

        # Check for a point
        scorer.checkPoint(pongball.xpos, pongball, SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE)
        scorer.printScore(scorer.player1score, scorer.player2score)
        #running = scorer.checkWin(scorer.player1score, scorer.player2score, limit)

        # Update display and tick clock.
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FRAMERATE)

    # WIP: Trying to implement a game over screen with "Play again" and "Quit"
    while not running:

        # Print box for "Play Again"
        #pygame.draw.rect(DISPLAYSURF, (0,204,0), (100,375,200,150))
        # Print box for "Exit"
        #pygame.draw.rect(DISPLAYSURF, (204,0,0), (480,375,200,150))
        if(scorer.player1score == limit):
            string = "Player 1 wins!"
            winText = FONT.render(string, True, (255,255,255))
            DISPLAYSURF.blit(winText, (100,200))
            pygame.display.update()

        else:
            string = "Player 2 wins!"
            winText = FONT.render(string, True, (255,255,255))
            DISPLAYSURF.blit(winText, (500,200))
            pygame.display.update()


        # Update display and tick clock.

        pygame.display.flip()
        clock.tick(FRAMERATE)




