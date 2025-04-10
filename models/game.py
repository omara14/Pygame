import pygame, random
from models.Spaceship import Spaceship
from models.alien import Alien
from models.missile import Missile

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.aliens_group = pygame.sprite.Group()
        self.create_aliens()
        self.aliens_direction = 1
        self.alien_missiles_group = pygame.sprite.Group()
        self.lives = 3
        self.run = True

    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = 90 + column * 65 # cell size
                y = 132 + row * 65

                if row == 0:
                    alien_type = 3
                elif row in (1,2):
                    alien_type = 2
                else: 
                    alien_type = 1

                alien = Alien(alien_type, x, y)
                self.aliens_group.add(alien)
    
    def move_aliens(self):
        self.aliens_group.update(self.aliens_direction)

        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width:      #if it hits each side, it will move down and move toward the otherside
                self.aliens_direction = -1
                self.alien_move_down(7)
            elif alien.rect.left <= 0:
                self.aliens_direction = 1
                self.alien_move_down(7)

    def alien_move_down(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot_missiles(self):
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            missile_sprite = Missile(random_alien.rect.center, -3, self.screen_height) #-3 as we want it to move downwards at this speed
            self.alien_missiles_group.add(missile_sprite)

    def check_collisions(self):
        #spacship check
        if self.spaceship_group.sprite.missiles_group:
            for missile_sprite in self.spaceship_group.sprite.missiles_group:
                """aliens_hit = pygame.sprite.spritecollide(missile_sprite, self.aliens_group, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.type * 10"""

                if pygame.sprite.spritecollide(missile_sprite, self.aliens_group, True):
                    missile_sprite.kill()
                    
                
        #alien missiles check
        if self.alien_missiles_group:
            for missile_sprite in self.alien_missiles_group:
                if pygame.sprite.spritecollide(missile_sprite, self.spaceship_group, False):
                    missile_sprite.kill()
                    print("Spaceship hit")
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()
                        
        #check for aliens reaching spaceship            
        if self.aliens_group:
            for alien in self.aliens_group:           
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()

    def game_over(self):
        self.run = False
        
    def reset(self):
        self.run = True
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_missiles_group.empty()
        self.create_aliens()
