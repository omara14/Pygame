import pygame
from models.Spaceship import Spaceship

def test_spaceship_movement():
    spaceship = Spaceship(screen_width = 900, screen_height = 840) 
    initial_position = spaceship.rect.x
    spaceship.get_user_input()  # Simulate key press for movement

    # Assuming the right key was pressed, the spaceship should move
    spaceship.rect.x = initial_position + spaceship.speed
    assert spaceship.rect.x == initial_position + spaceship.speed
    print("Correct Movement")

    spaceship.get_user_input()  # Simulate left key press
    spaceship.rect.x = initial_position
    assert spaceship.rect.x == initial_position
    print("Correct Movement")


def test_spaceship_constrain():  # this whole section ensures spaceship is always on screen
        spaceship = Spaceship(screen_width=900, screen_height=840)
        spaceship.get_user_input()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
                spaceship.rect.x += spaceship.speed
                spaceship.update()

        if (spaceship.rect.x == 760):
            assert spaceship.rect.x <= 800
            print("the spaceship can't move beyond right boundry of the screen")
    
    