#This is a learning test file.
#By Santino .J. Tomasi

import pygame,sys

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Lots of learning")

win_size = (600,400)

screen = pygame.display.set_mode(win_size)
display = pygame.Surface((300,200))


player_image = pygame.image.load('Assets/Player.png')
#Fuck yea!
player_image.set_colorkey((255,255,255))
grass_image = pygame.image.load('Assets/Grass_tile.png')
dirt_image = pygame.image.load('Assets/Dirt_tile.png')
Tile_Size = grass_image.get_width()

            # 1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19   
game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'], 
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles): # movement is x and y.
    collision_types = {'top':False,'bottom':False,'right':False,'left':False,}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect,collision_types


player_y_vel = 0
player_rect = pygame.Rect(50,50,player_image.get_width(),player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

moving_up = False
moving_down = False
moving_left = False
moving_right = False

while True:
    
    #Sets the screen background color.
    display.fill(pygame.Color("blue"))

    tile_rects = []
    y=0
    for row in game_map:
        x=0
        for tile in row:
            if tile == '1':
                display.blit(dirt_image, (x * Tile_Size,y * Tile_Size))
            if tile == '2':
                display.blit(grass_image, (x * Tile_Size,y * Tile_Size))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * Tile_Size, y * Tile_Size,Tile_Size,Tile_Size))
            x +=1
        y+=1

    #Player movement.
    player_movement = [0,0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_vel
    player_y_vel += 0.2

    if player_y_vel > 3:
        player_y_vel = 3

    player_rect,collisions = move(player_rect,player_movement, tile_rects)

    #Draws the player to the screen.
    display.blit(player_image,(player_rect.x,player_rect.y))

    #Looks to see if the window close button has been pressed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Closes pygame and the rest of the program.
            pygame.quit()
            sys.exit()

        #Looks to see if the key is down and if it is what key it is.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True

        #Looks to see if the key is up and if it is what key it is.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    #Updates program and sets fps to 60.
    surf = pygame.transform.scale(display, win_size)
    screen.blit(surf, (0,0))
    pygame.display.update()
    clock.tick(60)

