#####################
#    Vroom.py       #
#                   ########
# A Game where you         #
# pilot a car around rocks #
# that 'just happen' to    #
# appear in the middle of  #
# the road.                #
#############################

##########
# Set Up #
##########
import random
import time

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

car_width = 70  # Sets car width
displayWidth = 800  # Sets displayWidth in pixels
displayHeight = 600  # Sets displayHeight in pixels

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))  # A Tuple with display and height
# Variable  |Calls Pygame|Calls display|Use pygame.display command

pygame.display.set_caption('Vroom')  # Sets title bar text

# A clock is necessary to time in game actions
clock = pygame.time.Clock()  # Creates the clock which is imposed on everything

car_image = pygame.image.load('Car.png')  # Load Car.png


#############
# Functions #
#############

def odometer(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("thing_speed: " + str(count), True, black)
    gameDisplay.blit(text, (0, 15))


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def thing(thingx, thingy, thingw, thingh):  # Defines blocks
    pygame.draw.rect(gameDisplay, red, [thingx, thingy, thingw, thingh])


def car(x, y):  # Defines car
    gameDisplay.blit(car_image, (x, y))  # Blit Car.png on the display
    # 0,0 for computers is upper left. x = right y = down


def text_objects(message, font):  # Defines text_objects
    text_surface = font.render(message, True, black)  # Renders the font
    # Define text_surface|Font in Pygame|Put message|Aliasing toggle|Font color
    return text_surface, text_surface.get_rect()  # Returns the value og text_surface and text_surface.get_rect()


def message_display(message):  # Create function for message appearance
    largeText = pygame.font.Font('freesansbold.ttf', 115)  # Defines font
    TextSurf, TextRect = text_objects(message, largeText)  # Define TextSurf and TextRect
    TextRect.center = ((displayWidth / 2), (displayHeight / 2))  # Centers the text
    gameDisplay.blit(TextSurf, TextRect)  # Make text appear

    pygame.display.update()  # Update display
    time.sleep(2)  # Display text for 2 seconds
    game_loop()  # Restarts game_loop


def crash():  # Define crash
    message_display('You Crashed')  # Display message


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        smallText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("Vroom", largeText)
        TextRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(60)


def game_loop():  # Define game_loop
    x = (displayWidth * 0.45)  # Set x position
    y = (displayHeight * 0.8)  # Set y position

    x_change = 0  # Sets default change value

    dodged = 0
    ##############
    thing_startx = random.randrange(0, displayWidth)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100
    ##############

    #############
    # Game Loop #
    #           #############################################
    # A 'Game Loop' is where all the game logic is located. #
    #########################################################

    game_exit = False  # Default value crash is false (you have not crashed)
    while not game_exit:  # When your not leaving
        for event in pygame.event.get():  # Retrieves any event and applies it like *
            if event.type == pygame.QUIT:  # If the 'QUIT' event occurs the game ends
                game_exit = True  # Loop ceases to occur
                pygame.quit()  # Quits Pygame
                quit()  # Quits Python
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

        thing(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed
        car(x, y)  # Runs car
        ############
        # Odometer ##############
        odometer(thing_speed)  #
        #########################
        things_dodged(dodged)

        if x > displayWidth - car_width or x < 0:
            crash()
        if thing_starty > displayHeight:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, displayWidth)
            dodged += 1
            thing_speed += 0.5

        if y < thing_starty + thing_height:
            print('y crossover')
            if thing_startx < x < thing_startx + thing_width or thing_startx < x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()  # Updates what the player sees
        # pygame.display.update() = change just one thing in the parameter. If none specified than all updated
        # pygame.display.flip() will always update all the surface
        clock.tick(60)  # FPS is tied to clock so 60 tick = 60 FPS


############
# Game Run #
############

game_intro()  # Run intro

game_loop()  # Run game loop

###############
# End Process #
###############
pygame.quit()
quit()
