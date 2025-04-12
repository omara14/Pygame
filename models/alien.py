import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()  #initialises using pygame sprite methods
        self.type = type
        path = f"images/alien_1.png"    # image of aliens, will soon change this to be "alien_{type}" for each type of alien
        self.image = pygame.image.load(path)  #loads the image
        self.rect = self.image.get_rect(topleft = (x, y)) 

    def update(self, direction):
        self.rect.x += direction  # for movement of the aliens    
    