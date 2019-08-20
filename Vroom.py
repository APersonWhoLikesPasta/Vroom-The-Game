#####################
# Pygame Experiment #
#                   ##############
# This is a python program       #
# designed to test to experiment #
# with Pygame.                    #
##################################

##########
# Set Up #
##########
import pygame  # Imports the Pygame module

# Colors
black = (0, 0, 0,)
white = (255, 255, 255)
pygame.init()  # Pygame is an instance and you have to initialize it
displayWidth = 800  # Sets displayWidth in pixels
displayHeight = 600  # Sets displayHeight in pixels
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))  # A Tuple with display and height

# Variable  |Calls Pygame|Calls display|Use pygame.display command
pygame.display.set_caption('Vroom Vroom')  # Sets title bar text

# A clock is necessary to time in game actions
clock = pygame.time.Clock()  # Creates the clock which is imposed on everything

#############
# Game Loop #
#           #############################################
# A 'Game Loop' is where all the game logic is located. #
#########################################################

crashed = False  # Default value crash is false (you have not crashed)
while not crashed:  # When your not crashed
    for event in pygame.event.get():  # Retrieves any event and applies it like *
        if event.type == pygame.QUIT:  # If the 'QUIT' event occurs the game ends
            crashed = True  # Loop cease occurring
            print(event)  # Print the event to console
    pygame.display.update()  # Updates what the player sees
    # pygame.display.update() = change just one thing in the parameter. If none specified than all updated
    # pygame.display.flip() will always update all the surface
    clock.tick(60)  # FPS is tied to clock so 60 tick = 60 FPS

###############
# End Process #
###############
pygame.quit()
quit()
