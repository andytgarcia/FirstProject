import pygame


from Player import *

def clearScreen():
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 0, 1280, 720))

def handleStage():
    bottomPlatform = pygame.Rect(320, 500, 600, 100)
    pygame.draw.rect(screen, pygame.Color(0, 255, 255), bottomPlatform, 0)
    if pygame.Rect.colliderect(bottomPlatform, player.getPlayerHurtBox()):
        print("Collision")
    
    
def drawPlayerHurtBox():
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), player.getPlayerHurtBox(), 1)
    

        





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
    handleStage()
    player.draw()
    drawPlayerHurtBox()
    player.movement()

    pygame.display.flip()
    fpsClock.tick(FPS)
