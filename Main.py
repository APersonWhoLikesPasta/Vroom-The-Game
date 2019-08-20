#####################
# Pygame Experiment #
#                   ##############
# This is a python program       #
# desgined to test to experiment #
# with pygam.                    #
##################################

##########
# Set Up #
##########
import pygame  # Imports the pygame module

pygame.init()  # Pygame is an instance and you have to initiaze it
gameDisplay = pygame.display.set_mode((800, 600))  # In the tulple is width and height

# Variable  |Calls pygame|Calls display|Use pygame.display command
pygame.display.set_caption('Vroom Vroom')  # Sets titlebar text

# A clock is nessery to time in game actions
clock = pygame.time.Clock()  # Creates the clock which is imposed on everything

#############
# Game Loop #
#           #############################################
# A 'Game Loop' is where all the game logic is located. #
#########################################################

crashed = False  # Default value crash is false (you have not crashed)
while not crashed:  # When your not crashed
    for event in pygame.event.get():  # Retreaves any event and applies it like *
        if event.type == pygame.QUIT:  # If the 'QUIT' event occurs the game ends
            crashed = True  # Loop cease occuring
            print(event)  # Print the event to console
    pygame.display.update()  # Updates what the player sees
    # pygame.display.update() = change just one thing in the parmeter. If none specifed than all updated
    # pygame.display.flip() will always update all the surface
    clock.tick(60)  # FPS is tied to clock so 60 tick = 60 FPS

###############
# End Process #
###############
pygame.quit()
quit()
