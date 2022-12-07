import pygame

from Player import *

global bottomPlatform

stage = []

def clearScreen():
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 0, 1280, 720))

def drawStage():
    bottomPlatform = pygame.Rect(320, 500, 600, 100)
    pygame.draw.rect(screen, pygame.Color(0, 255, 255), bottomPlatform, 0)
    
    
def checkCollision():
    print("Collision!")







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
    drawStage()
    player.draw()
    player.movement()

    pygame.display.flip()
    fpsClock.tick(FPS)
