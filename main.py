import pygame, sys, time
from models.button import Button
from models.game import Game

pygame.init()

# Your game's screen size
SCREEN_WIDTH = 825
SCREEN_HEIGHT = 770

GREY = (30, 30, 28)
YELLOW = (240, 215, 60)  #colours
RED = (255, 20, 20)

# Menu screen setup
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Space Shooters")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("monogram", size)

def play():
    # full game code

    font = pygame.font.SysFont('monogram', 40)
    level_surface = font.render("LEVEL 01", False, YELLOW)
    game_over_surface = font.render("GAME OVER! PRESS SPACE TO RESTART", False, RED)
    game_win_surface = font.render("YOU WIN! PRESS SPACE TO RESTART", False, YELLOW)
    score_text_surface = font.render("SCORE", False, YELLOW)

    screen = SCREEN  # use same screen
    clock = pygame.time.Clock()

    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

    SHOOT_MISSILE = pygame.USEREVENT
    pygame.time.set_timer(SHOOT_MISSILE, 700)

    while True:
        #checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SHOOT_MISSILE and game.run:
                game.alien_shoot_missiles()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and game.run == False:
                time.sleep(2)# to allow the player to read the win or loss message before restarting the game
                game.reset()

        #updating
        if game.run:
            game.spaceship_group.update()
            game.move_aliens()
            game.alien_missiles_group.update()
            game.check_collisions()
            if game.score == "990":  #this is the max score a player can get in the first level
                game.create_boss_alien()

        """#tests
        
        test.test_spaceship_constrain()"""

        #drawing
        screen.fill(GREY)

        #ui
        if game.run:
            screen.blit(level_surface, (570, 740, 50, 50))

        elif game.boss_defeated:
            screen.blit(game_win_surface, (140, 100, 100, 100))

        elif game.run == False: 
            screen.blit(game_over_surface, (140, 100, 100, 100))
            

        x = 50
        for life in range(game.lives - 1):
            screen.blit(game.spaceship_group.sprite.image, (x, 745))
            x += 50

        screen.blit(score_text_surface, (50, 15, 50, 50))
        formatted_score = str(game.score).zfill(4)
        score_surface = font.render(formatted_score, False, YELLOW)
        screen.blit(score_surface, (50, 40, 50, 50))

        game.spaceship_group.draw(screen)
        game.spaceship_group.sprite.missiles_group.draw(screen)
        game.aliens_group.draw(screen)
        game.alien_missiles_group.draw(screen)


        pygame.display.update()
        clock.tick(60)

def about():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(GREY)

        about_lines = [
            "Developed By Omar Abdou",
            "Developed in 2025",
        ]

        font = get_font(45)
        y_offset = 150  # Starting y position for first line

        for line in about_lines:
            text_surface = font.render(line, True, YELLOW)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            SCREEN.blit(text_surface, text_rect)
            y_offset += 60  # Space between lines

        ABOUT_BACK = Button(
            image=None,
            pos=(SCREEN_WIDTH // 2, 500),
            text_input="BACK",
            font=get_font(75),
            base_color="White",
            hovering_color="Green"
        )

        ABOUT_BACK.changeColor(ABOUT_MOUSE_POS)
        ABOUT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.checkForInput(ABOUT_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def instructions():
    while True:
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(GREY)

        instructions_text = [
            "1. Press space to shoot at the aliens",
            "2. Press the right arrow key to move to the right",
            "3. Press the left arrow key to move to the left",
            "4. Dodge the aliens' attacks and defeat them all",
            "before they reach you"
        ]

        font = get_font(45)
        y_offset = 150  # Starting y position for first line

        for line in instructions_text:
            text_surface = font.render(line, True, YELLOW)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            SCREEN.blit(text_surface, text_rect)
            y_offset += 60  # Adjust the spacing between lines

        INSTRUCTIONS_BACK = Button(
            image=None,
            pos=(SCREEN_WIDTH // 2, 500),
            text_input="BACK",
            font=get_font(75),
            base_color="White",
            hovering_color="Green"
        )

        INSTRUCTIONS_BACK.changeColor(INSTRUCTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.fill(GREY)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("MAIN MENU", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play.png"), pos=(SCREEN_WIDTH // 2, 250),
                             text_input="PLAY", font=get_font(60), base_color= YELLOW, hovering_color="White")
        ABOUT_BUTTON = Button(image=pygame.image.load("images/About.png"), pos=(SCREEN_WIDTH // 2, 400),
                                text_input="ABOUT", font=get_font(60), base_color=YELLOW, hovering_color="White")
        INSTRUCTIONS_BUTTON = Button(image=pygame.image.load("images/Instructions.png"), pos=(SCREEN_WIDTH // 2, 550),
                                text_input="INSTRUCTIONS", font=get_font(60), base_color=YELLOW, hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit.png"), pos=(SCREEN_WIDTH // 2, 700),
                             text_input="QUIT", font=get_font(60), base_color=YELLOW, hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, ABOUT_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
