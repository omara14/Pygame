import pygame, sys
from models.game import Game


pygame.init() 

SCREEN_WIDTH = 825
SCREEN_HEIGHT = 770  # creating screen size and background colour

GREY = (30, 30, 28)
YELLOW = (240, 215, 60)  # creating colors using RBG layout
RED = (255, 20, 20)

font = pygame.font.SysFont('monogram', 40)  #setting font
level_surface = font.render("LEVEL 01", False, YELLOW) #text stating which level players are on
game_over_surface  = font.render("GAME OVER", False, RED) # text to replace the above text, indicating game end
score_text_surface = font.render("SCORE", False, YELLOW) #text to keep track of score

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a tuple for the screen
pygame.display.set_caption("Pygame Space Shooters") #sets caption for the game

clock = pygame.time.Clock() #importing pygame clock to control time

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT) 

SHOOT_MISSILE = pygame.USEREVENT #creating a user event for when a missile is shot
pygame.time.set_timer(SHOOT_MISSILE, 700)  #time between missile shots

while True:
    #checks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #checks for quit event 
            pygame.quit()
            sys.exit() #quits the game and exits
        if event.type == SHOOT_MISSILE and game.run:   #checks if user is shooting missiles
            game.alien_shoot_missiles() 
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:  # resets the game when space bar is pressed after death
            game.reset() 



    #updating
    if game.run: #if the game is running
        game.spaceship_group.update()         #essentially any and every update in the game
        game.move_aliens()
        game.alien_missiles_group.update()
        game.check_collisions()
    
    """#tests
    
    test.test_spaceship_constrain()"""
    
    #drawing
    screen.fill(GREY) #background creation

    #ui
    if game.run:
            screen.blit(level_surface, (570, 740, 50, 50)) #writing the level on the screen
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))  #if there is no level, it will show game over 
    
    x = 50 # explained in line 67
    for life in range(game.lives - 1):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50  #this is used to seperate each image of the spaceship which represents lives

    screen.blit(score_text_surface, (50, 15, 50, 50)) #the text that represents the score
    formatted_score = str(game.score).zfill(4)  #zfill is used to make 0000 turn into 0100, replacing the previous number whilst keeping it in 4 digits
    score_surface = font.render(formatted_score, False, YELLOW) #gets the formatted score and presents it in yellow
    screen.blit(score_surface, (50, 40, 50, 50)) #draws the score

    game.spaceship_group.draw(screen) #draws all visual aspects
    game.spaceship_group.sprite.missiles_group.draw(screen)          
    game.aliens_group.draw(screen)
    game.alien_missiles_group.draw(screen)
        
    pygame.display.update()
    clock.tick(60)    #ticks, determines speed of the game