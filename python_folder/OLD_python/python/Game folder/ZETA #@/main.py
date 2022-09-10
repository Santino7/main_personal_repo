#This is a ZETA program
#By Santino .J. Tomasi

#Imports sys.
import imp
import sys
#Imports pygame.
import pygame

from settings import *

from tiles import Tile

from level import Level

#Starts pygame.
pygame.init()



#Sets screen to equal the more complicated screen values to make it easier to read.
screen = pygame.display.set_mode((screen_width,screen_height))

#Has clock equal the more complicated and long clock values.
clock = pygame.time.Clock()

level = Level(level_map,screen)

while True:

    #Looks to see if the x button or close button for the screen has been clicked.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #________________________________________________

    #Sets screen color or shade to black.
    screen.fill('black')

    level.run()

    #Updates the display.
    pygame.display.update()

    #Sets fps.
    clock.tick(60)

    