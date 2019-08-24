import pygame

pygame.init()

#######################################################
# A file to test and experiment with shapes in Pygame #
#######################################################

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((800, 600))

game_display.fill(black)

pixAr = pygame.PixelArray(game_display)
pixAr[10][20] = green
#     |X|Y|

pygame.draw.rect(game_display, red, (400, 500, 100, 10))
# Use Pygame                 |Color|Top left|Width|Height

pygame.draw.circle(game_display, green, (300, 200), 25)
# Use Pygame                    |Color|Center|Radius

pygame.draw.line(game_display, blue, (100, 200), (300, 450), 5)
# Use Pygame for stuff       |Color|Start Point|End Point|Line width

pygame.draw.polygon(game_display, white, ((25, 75), (76, 125), (600, 575)))
# Use Pygame                             |Start Point|Point One|Point Two|

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
