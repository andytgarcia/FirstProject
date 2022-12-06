import pygame

from Player import *


def clearScreen():
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 0, 1280, 720))


def drawMap():
    pygame.draw.rect(200, 500, 320, 300)


# start of program
pygame.init()  # start engine
FPS = 60  # 60 frames per second
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
gameOver = False
player = Player(screen, 640, 360)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    clearScreen()
    player.draw()
    player.movement()

    pygame.display.flip()
    fpsClock.tick(FPS)
