import pygame, sys
from models.game import Game


pygame.init() 

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 840  # creating screen size and background colour
GREY = (30, 30, 28)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a tuple for the screen
pygame.display.set_caption("Pygame Space Shooters")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

SHOOT_MISSILE = pygame.USEREVENT
pygame.time.set_timer(SHOOT_MISSILE, 700)

while True:
    #checks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #checks for quit event
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_MISSILE:   #checks if user is shooting missiles
            game.alien_shoot_missiles()
    
    #updating
    game.spaceship_group.update()         #essentially any and every update in the game
    game.move_aliens()
    game.alien_missiles_group.update()
    game.check_collisions()
    
    """#tests
    
    test.test_spaceship_constrain()"""
    
    #drawing
    screen.fill(GREY)   
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.missiles_group.draw(screen)          #visual aspects
    game.aliens_group.draw(screen)
    game.alien_missiles_group.draw(screen)

   
        
    pygame.display.update()
    clock.tick(60)    #ticks, determines speed of the game