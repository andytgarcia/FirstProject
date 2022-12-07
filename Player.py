import pygame


class Player:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color(0, 0, 255), (self.x, self.y), 7.5)

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.moveUp()
        if keys[pygame.K_s]:
            # moveDown
            self.moveDown()
        if keys[pygame.K_a]:
            # moveLeft
            self.moveLeft()
        if keys[pygame.K_d]:
            # moveRight
            self.moveRight()

    def moveUp(self):
        self.y = self.y - 5

    def moveDown(self):
        self.y = self.y + 5

    def moveLeft(self):
        self.x = self.x - 5

    def moveRight(self):
        self.x = self.x + 5
        
    def getSize():
        return 7.5
    
    
    def getPlayerHurtBox(self):
        return pygame.Rect(self.x - 7.5, self.y - 7.5, 7.5 * 2, 7.5 * 2)
    
    
    
    
