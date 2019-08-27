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
darkRed = (125, 0, 0)
darkGreen = (0, 125, 0)

pygame.init()  # Pygame is an instance and you have to initialize it

car_width = 70  # Sets car width
displayWidth = 800  # Sets displayWidth in pixels
displayHeight = 600  # Sets displayHeight in pixels

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))  # A Tuple with display and height
# Variable  |Calls Pygame|Calls display|Use pygame.display command

pygame.display.set_caption('Vroom')  # Sets title bar text

# A clock is necessary to time in game actions
clock = pygame.time.Clock()  # Creates the clock which is imposed on everything

crash_sound = pygame.mixer.Sound('car_crash.wav')
vroom_intro_music = pygame.mixer.music.load('VroomIntroMusic.wav')

car_image = pygame.image.load('Car.png')  # Load Car.png
truck_image = pygame.image.load('car-truck3.png')
game_icon = pygame.image.load('CarIcon.png')

pygame.display.set_icon(car_image)


#############
# Functions #
#############


def exit_game():
    print("Quit from Menu")
    pygame.quit()
    quit()


def button(msg, x, y, w, h, ic, ac):
    # button(MSG!, 155, 155, 100, 50, red, darkRed)
    mouse = pygame.mouse.get_pos()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 30)
    text_surf, text_rect = text_objects(msg, small_text, ic)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(text_surf, text_rect)


def odometer(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("thing_speed: " + str(count), True, white)
    gameDisplay.blit(text, (5, 15))


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text, (5, 0))


def thing(thingx, thingy, thingw, thingh):  # Defines blocks
    pygame.draw.rect(gameDisplay, black, [thingx, thingy, thingw, thingh])

    pygame.draw.rect(gameDisplay, white, (displayWidth / 2 - 10, 50, 20, 100))
    pygame.draw.rect(gameDisplay, white, (displayWidth / 2 - 10, displayHeight / 2 - 50, 20, 100))
    pygame.draw.rect(gameDisplay, white, (displayWidth / 2 - 10, 450, 20, 100))

    gameDisplay.blit(truck_image, (thingx, thingy))


def car(x, y):  # Defines car
    # pygame.draw.rect(gameDisplay, red, (x, y, 70, 75))
    gameDisplay.blit(car_image, (x, y))  # Blit Car.png on the display
    # 0,0 for computers is upper left. x = right y = down


def text_objects(message, font, color):  # Defines text_objects
    text_surface = font.render(message, True, color)  # Renders the font
    # Define text_surface|Font in Pygame|Put message|Aliasing toggle|Font color
    return text_surface, text_surface.get_rect()  # Returns the value og text_surface and text_surface.get_rect()


def message_display(message):  # Create function for message appearance
    large_text = pygame.font.Font('freesansbold.ttf', 115)  # Defines font
    text_surf, text_rect = text_objects(message, large_text, white)  # Define text_surf and text_rect
    text_rect.center = ((displayWidth / 2), (displayHeight / 2))  # Centers the text
    gameDisplay.blit(text_surf, text_rect)  # Make text appear

    pygame.display.update()  # Update display
    time.sleep(2)  # Display text for 2 seconds
    game_loop()  # Restarts game_loop


def crash():  # Define crash
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    pygame.draw.rect(gameDisplay, black, (displayWidth / 2 - 10, displayHeight / 2 - 50, 20, 100))
    message_display('You Crashed')  # Display message
    print("Crash")


def game_background():
    gameDisplay.fill(black)

    pygame.draw.line(gameDisplay, green, (1, 1), (1, 600), 5)
    pygame.draw.line(gameDisplay, green, (800, 1), (800, 600), 9)
    pygame.draw.rect(gameDisplay, white, (displayWidth / 2 - 10, displayHeight / 2 - 50, 20, 100))
    pygame.draw.rect(gameDisplay, white, (displayWidth / 2 - 10, 450, 20, 100))


def game_intro():
    pygame.mixer.music.play(-1)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_background()
        large_text = pygame.font.Font('freesansbold.ttf', 75)
        text_surf, text_rect = text_objects("Vroom: The Game", large_text, white)
        text_rect.center = (400, 100)
        gameDisplay.blit(text_surf, text_rect)

        ##########
        # Button #
        ##########
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 150 + 150 > mouse[0] > 150 and 250 + 100 > mouse[1] > 250:
            print("button_one: Hover True")
            pygame.draw.rect(gameDisplay, darkRed, (displayWidth / 2 - 250, displayHeight / 2 - 50, 150, 100))
            if click[0] == 1:
                exit_game()
        elif 500 + 150 > mouse[0] > 150 and 250 + 100 > mouse[1] > 250:
            pygame.draw.rect(gameDisplay, darkGreen, (displayWidth / 2 + 100, displayHeight / 2 - 50, 150, 100))
            if click[0] == 1:
                print("button_two: Click True")
                game_loop()

        pygame.draw.rect(gameDisplay, red, (displayWidth / 2 - 250, displayHeight / 2 - 50, 150, 100))
        pygame.draw.rect(gameDisplay, green, (displayWidth / 2 + 100, displayHeight / 2 - 50, 150, 100))

        small_text = pygame.font.Font("freesansbold.ttf", 30)
        text_surf, text_rect = text_objects("Play!", small_text, black)
        text_rect.center = ((displayWidth / 2 + (350 / 2)), (displayHeight / 2))
        gameDisplay.blit(text_surf, text_rect)

        small_text = pygame.font.Font("freesansbold.ttf", 30)
        text_surf, text_rect = text_objects("Quit!", small_text, black)
        text_rect.center = ((displayWidth / 2 - (350 / 2)), (displayHeight / 2))
        gameDisplay.blit(text_surf, text_rect)

        ##############
        # Not Button #
        ##############
        pygame.display.update()
        clock.tick(60)


def game_loop():  # Define game_loop
    vroom_game_music = pygame.mixer.music.load('VroomMusic.wav')
    pygame.mixer.music.play(-1)

    x = (displayWidth * 0.45)  # Set x position
    y = (displayHeight * 0.8)  # Set y position

    x_change = 0  # Sets default change value

    dodged = 0

    ##############
    moving = random.randrange(1, 3)
    if moving == 3:
        thing_startx = x
    else:
        thing_startx = random.randrange(5, displayWidth - 50)
    thing_starty = -600
    thing_speed = 5
    thing_width = 71
    thing_height = 174
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

        ##############
        # Background #
        ##############
        game_background()
        pygame.draw.rect(gameDisplay, white, (displayWidth / 2 - 10, 50, 20, 100))

        thing(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed
        car(x, y)  # Runs car

        ############
        # Odometer ###############
        # odometer(thing_speed)  #
        ##########################
        things_dodged(dodged)

        if x > displayWidth - car_width or x < 0:
            crash()
        if thing_starty > displayHeight:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(5, (displayWidth - 65))
            dodged += 1
            moving = random.randrange(1, 4)
            if moving == 3:
                thing_startx = x
            else:
                thing_startx = random.randrange(5, displayWidth - 50)
            thing_speed += 0.5

        if y < thing_starty + thing_height:
            if thing_startx < x < thing_startx + thing_width:
                print('crash')
                crash()
            elif thing_startx < x + car_width < thing_startx + thing_width:
                print('crash')
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
