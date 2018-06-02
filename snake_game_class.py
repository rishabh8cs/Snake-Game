import pygame
import sys
from pygame.locals import *
import random

WIDTH = 500
HEIGHT = 500

# Defining colors 
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Defining snake initial position
snakeposx = [280,280,280,280,280]
snakeposy = [280,260,240,220,200]
snakeimg = pygame.Surface((20,20))
snakeimg.fill(GREEN)

# Defining apple surface
appleimg = pygame.Surface((20,20))
appleimg.fill(RED)

# Defining apple initial position
appleposx = random.randint(0,WIDTH-20)
appleposy = random.randint(0,HEIGHT-20)

# motion of snake
direction = 'down'

def collide(x1, x2, y1, y2):
    if x1+20>x2 and x2+20>x1 and y1+20>y2 and y2+20>y1:
        return True
    else:
        return False

pygame.init()
displaySurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
FRAMES_PER_SEC = 10

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            # keyboard key is pressed
            if event.key == K_UP and direction != 'down':
                direction = 'up'
            elif event.key == K_DOWN and direction != 'up':
                direction = 'down'
            elif event.key == K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == K_RIGHT and direction != 'left':
                direction = 'right'

    # Collision with self
    i = len(snakeposx) - 1
    while i >= 2:
        if collide(snakeposx[0], snakeposx[i], snakeposy[0], snakeposy[i]):
            print "Collision happened!"
            pygame.quit()
            sys.exit(0)
        i = i - 1

    # Collision with border
    if snakeposx[0] < 0 or snakeposx[0] > (WIDTH-20) :
        print "Collision with border!"
        pygame.quit()
        sys.exit(0)
        
    if snakeposy[0] < 0 or snakeposy[0] > (HEIGHT-20):
        print "Collision with border!"
        pygame.quit()
        sys.exit(0)

    # Collision with apple
    if collide(snakeposx[0], appleposx, snakeposy[0], appleposy):
        score = score + 1
        appleposx = random.randint(0,WIDTH-20)
        appleposy = random.randint(0,HEIGHT-20)
        print "Score updated ", score
    
    i = len(snakeposx) - 1
    while i >= 1:
        snakeposx[i] = snakeposx[i-1]
        snakeposy[i] = snakeposy[i-1]
        i = i - 1

    # making a new head (appear like moving)
    if direction == 'left':
        snakeposx[0] = snakeposx[0] - 20
    elif direction == 'right':
        snakeposx[0] = snakeposx[0] + 20
    elif direction == 'up':
        snakeposy[0] = snakeposy[0] - 20
    elif direction == 'down':
        snakeposy[0] = snakeposy[0] + 20

    displaySurface.fill(BLUE)
    for i in range(len(snakeposx)):
        displaySurface.blit(snakeimg, (snakeposx[i], snakeposy[i]))

    displaySurface.blit(appleimg, (appleposx, appleposy))
    
    clock.tick(FRAMES_PER_SEC)
    pygame.display.update()





