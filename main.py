import pygame, sys
from models.game import Game


pygame.init() 

SCREEN_WIDTH = 825
SCREEN_HEIGHT = 770  # creating screen size and background colour
OFFSET = 50

GREY = (30, 30, 28)
YELLOW = (240, 215, 60)


screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET)) #create a tuple for the screen
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
        if event.type == SHOOT_MISSILE and game.run:   #checks if user is shooting missiles
            game.alien_shoot_missiles()
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset() 



    #updating
    if game.run:
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