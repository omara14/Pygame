import pygame
from models.missile import Missile

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self.screen_height)) #ensures the sprites bottom/centre is aligned, making it ready to be displayed/interacted
        self.speed = 7
        self.missiles_group = pygame.sprite.Group()
        self.missile_ready = True #Missile ready to be fired otherwise constant line of missiels is drawn
        self.missile_time = 0
        self.missiles_delay = 300 # Next missile to be fired after 300 ms from the latest fired missile otherwise a onstant line of missiels is drawn
    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.missile_ready:
            self.missile_ready = False # see comments for controling missiles rate
            missile = Missile(self.rect.center, 7, self.screen_height) # self.rect.center = postion of the missile , 7 = speed
            missile.image = pygame.image.load("images/spaceship_missile.png")   #image of the spaceship's missile, when inherited by aliens will change to aliens missile due to direction reasons
            self.missiles_group.add(missile)
            self.missile_time = pygame.time.get_ticks()

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.missiles_group.update()    #movement and its rules
        self.recharge_missile()

    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0

    def recharge_missile(self): # to control when the next missile can be fire to avoid onstant line of missiels is drawn
        if not self.missile_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.missile_time >= self.missiles_delay:
                self.missile_ready = True


    def reset(self):
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self. screen_height))
        self.missiles_group.empty()