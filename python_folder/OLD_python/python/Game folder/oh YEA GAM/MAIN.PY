from tkinter.tix import MAIN
from turtle import width
import pygame
import os

#Folder name OH+`` YEA GAM 
#By Santino .J. Tomasi
#Version beta 1.0
#Date of version 4/25/2022
#Name of game Tech nnwale.

WIDTH,HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tech nnwale")
FPS = 60

VEL = 5

RED = (255,0,50)
WHITE = (255,255,255)

player_hight = 200

player_width = 140

player_image = pygame.image.load(os.path.join('Game assets','rad_dude.png'))
player = pygame.transform.scale(player_image,(player_hight,player_width))


def draw_window(player_pos):
    WIN.fill(WHITE)

    player_gravity = 0
    player_gravity +=1
    player_pos.y += player_gravity
    WIN.blit(player, (player_pos.x,player_pos.y))
    pygame.display.update()

def main():
    player_pos = pygame.Rect(250 ,500,player_width,player_hight)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        #Left
        if keys_pressed[pygame.K_a]:
            player_pos.x -= VEL
        #Right 
        if keys_pressed[pygame.K_d]:
            player_pos.x += VEL
        #Up
        if keys_pressed[pygame.K_w]:
            player_pos.y -= VEL
        #Down
        if keys_pressed[pygame.K_s]:
            player_pos.y += VEL

        #Ground
        if player_pos.bottom >= 500: 
            player_pos.bottom =500

        draw_window(player_pos)
    
    pygame.quit()



if __name__ == "__main__":
    main()
