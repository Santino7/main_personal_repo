#This is a test learing file.
#By Santino .J. Tomasi

#Imports pygame.
import pygame
#Imports exit from sys.
from sys import exit

#Starts pygame.
pygame.init()

#Width and Height for screen.
winWidth = 800
winHeight = 400

#Sets the screen to equal the display values.
screen = pygame.display.set_mode((winWidth,winHeight))

#Sets title or caption for window.
pygame.display.set_caption("Test file")

#Sets clock to equal clock values.
clock = pygame.time.Clock()

#Sets Background and ground values.
background = pygame.image.load('Assets/Background.png')
ground = pygame.image.load('Assets/Ground.png')

#Main loop
while True:

    #Looks to see if the user has pressed the x or close button on the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Makes the background on the screen.
    screen.blit(background,(0,0))
    #Makes the ground on the screen.
    screen.blit(ground,(0,300))

    #Updates window or screen.
    pygame.display.update()
    #Sets fps value.
    clock.tick(60)
