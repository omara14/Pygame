import pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__() #initializes using pygame sprite methods
        try:
            self.image = pygame.image.load("images/alien_missile.png")   #image of the aliens's missile, when inherited by spaceship will change to aliens missile due to direction reasons
        except pygame.error as e:
            print(f"Failed to load missile image: {e}")  # print error message
        self.rect = self.image.get_rect(center = position)
        self.speed = speed 
        self.screen_height = screen_height

    def update(self): 
       self.rect.y -= self.speed #to move missile vertically 
       if self.rect.y > self.screen_height + 30 or self.rect.y < -30: #if the missile goes out ot the screen delete it 
            print("Missile moved out of range to be deleted") #for testing only 
            self.kill()

