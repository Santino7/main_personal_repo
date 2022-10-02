#This is a test file.
#By Santino .J. Tomasi

import sys
import pygame

pygame.init()

winWidth = 400
winHeight = 400

screen = pygame.display.set_mode((winWidth,winHeight))
clock = pygame.time.Clock()

player_frame1 = pygame.image.load('sprites/sprites_things0.png')
player_frame2 = pygame.image.load('sprites/sprites_things1.png')
player_index = 0
player_frame_array = [player_frame1,player_frame2]
player_test = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('White')
    
    
    screen.blit(player_frame_array[player_index],(200,200))
    player_test+=1
    if player_index == 0 and player_test %2:
        player_index=1
    else:
        player_index=0
    player_test+=1
    
    

    pygame.display.update()
    clock.tick(60)