import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()  #initialises using pygame sprite methods
        self.type = type
        path = f"images/alien_{self.type}.png"# image of aliens, will soon change this to be "alien_{type}" for each type of alien
        try:  #error handling for ensuring files exist
            self.image = pygame.image.load(path)
        except pygame.error as e:
            print(f"Failed to load spaceship image: {e}")
        self.rect = self.image.get_rect(topleft = (x, y)) 
        self.health = 1

    def update(self, direction):
        self.rect.x += direction  # for movement of the aliens    
    
class BossAlien(Alien):
    def __init__(self, x, y):
        super().__init__(type=5, x=x, y=y)
        self.type = 5  
        self.image = pygame.transform.scale(self.image, (100, 100))  
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 10  # Boss has more health 
        
    def update(self, direction):
        self.rect.x += direction