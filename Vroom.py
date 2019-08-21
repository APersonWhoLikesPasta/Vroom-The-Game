#####################
# Pygame Experiment #
#                   ########
# A Game where you         #
# pilot a boat around rocks#
############################

##########
# Set Up #
##########
import pygame  # Imports the Pygame module

# Colors
black = (0, 0, 0,)  # Defines black
white = (255, 255, 255)  # Defines white
red = (255, 0, 0,)  # Defines red
green = (0, 255, 0)  # Defines green
blue = (0, 0, 255)  # Defines blue
gray = (105, 105, 105)  # Defines gray
dimGray = (119, 136, 153)  # Defines dim gray
darkGray = (169, 169, 169)  # Define dark gray

pygame.init()  # Pygame is an instance and you have to initialize it

displayWidth = 800  # Sets displayWidth in pixels
displayHeight = 600  # Sets displayHeight in pixels

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))  # A Tuple with display and height
# Variable  |Calls Pygame|Calls display|Use pygame.display command

pygame.display.set_caption('Vroom')  # Sets title bar text

# A clock is necessary to time in game actions
clock = pygame.time.Clock()  # Creates the clock which is imposed on everything

carImg = pygame.image.load('Car.png')  # Load Car.png


#############
# Functions #
#############

def car(x, y):  # Defines car
    gameDisplay.blit(carImg, (x, y))  # Blit Car.png on the display
    # 0,0 for computers is upper left. x = right y = down


def game_loop():
    x = (displayWidth * 0.45)  # Set x position
    y = (displayHeight * 0.8)  # Set y position

    x_change = 0  # Sets default change value

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
            if event.type == pygame.KEYDOWN:  # Check to see if some pressed a key
                if event.key == pygame.K_LEFT:  # If the keypress if left arrow key
                    x_change = -5  # Moves car 5 pixels to the left
                elif event.key == pygame.K_RIGHT:  # Check to see if keypress is right arrow key
                    x_change = +5  # Moves car five pixels to the right
            if event.type == pygame.KEYUP:  # Check to see if key release
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # If the right / left arrows keys release
                    x_change = 0  # Resets x so it is relative

        x += x_change  # x = x + xChange // If xChange is -5 than x will move over minus five

        gameDisplay.fill(white)  # Creates white background (put in right order or else get overwritten)
        car(x, y)  # Runs car
        pygame.display.update()  # Updates what the player sees
        # pygame.display.update() = change just one thing in the parameter. If none specified than all updated
        # pygame.display.flip() will always update all the surface
        clock.tick(60)  # FPS is tied to clock so 60 tick = 60 FPS


game_loop()  # Run game loop

###############
# End Process #
###############
pygame.quit()
quit()
