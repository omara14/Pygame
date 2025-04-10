import pygame, sys
from models.game import Game


pygame.init() 

SCREEN_WIDTH = 825
SCREEN_HEIGHT = 770  # creating screen size and background colour

GREY = (30, 30, 28)
YELLOW = (240, 215, 60)
RED = (255, 20, 20)

font = pygame.font.SysFont('monogram', 40)
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface  = font.render("GAME OVER", False, RED)
score_text_surface = font.render("SCORE", False, YELLOW)

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

    #ui
    if game.run:
            screen.blit(level_surface, (570, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))
    
    x = 50
    for life in range(game.lives - 1):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(4)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.missiles_group.draw(screen)          #visual aspects
    game.aliens_group.draw(screen)
    game.alien_missiles_group.draw(screen)
        
    pygame.display.update()
    clock.tick(60)    #ticks, determines speed of the game