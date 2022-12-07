#This is paddle 1000
#By Santino .J. Tomasi
#Date 5/22/2022
#Version 4
#Version 1 Date 5/20/2020
#Version 1 was the base game.
#Version 2 Date 5/20/2022
#Version 2 added the game over screen.
#Version 3 Date 5/22/2022
#Version 3 Added a score and points.
#Version 4 Date 5/22/2022
#Version 4 Added a life meter.


#All imports.
import subprocess
from turtle import speed
import pygame

pygame.init()

#Window size.
win_x = 750
win_y = 500

win = pygame.display.set_mode((win_x,win_y))

pygame.display.set_caption("Paddle 1000!")

#Colors in window.
black = (0,0,0)
white = (255,255,255)

#Paddle class.
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([75,10])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.points = 0
        self.life = 2

#Ball class.
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1

#Life cube 1 class.
class Life_cube_bar1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(black)
        self.rect = self.image.get_rect()

#Sets life cube position.
life_cube1 = Life_cube_bar1()
life_cube1.rect.x = 90
life_cube1.rect.y = 60

#Life cube 2 class.
class Life_cube_bar2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(black)
        self.rect = self.image.get_rect()

#Sets life cube position.
life_cube2 = Life_cube_bar2()
life_cube2.rect.x = 90
life_cube2.rect.y = 60

#Sets Paddles position.
paddle1 = Paddle()
paddle1.rect.x = 375
paddle1.rect.y = 475

#Sets Balls position.
ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

#Speed for paddle.
paddle_speed = 30

#Sprite group.
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1,ball,life_cube1)

#Redraws thee window.
def redraw():
    win.fill(white)
    font = pygame.font.SysFont('Comic Sans MS',30)
    text = font.render("""Paddle 1000,
    you better
    be 
    ready""",False,black)
    textc = font.render("1000!!!",False,black)
    textcRect = textc.get_rect()
    textcRect.center = (650,60)
    textb = font.render("This is Paddel",False,black)
    textbRect = textb.get_rect()

    #Text b rect.
    textbRect.center = (500,40)
    textRect = text.get_rect()

    #Orignal text rect.
    textRect.center = (25,300)

    #Player points.
    paddle1_score = font.render(str(paddle1.points),False,black)
    p1pRect = paddle1_score.get_rect()
    p1pRect.center = (110,45)

    #Player points label.
    paddle1_points_label = font.render("Points:",False,black)
    p1plRect = paddle1_points_label.get_rect()
    p1plRect.center = (47,45)

    #Player life.
    paddle1_life = font.render(str(paddle1.life),False,black)
    p1fRect = paddle1_life.get_rect()
    p1fRect.center = (73,75)


    #player life label.
    paddle1_life_label = font.render("Life:",False,black)
    p1flRect = paddle1_life_label.get_rect()
    p1flRect.center = (31,75)


    
    #Adds text to screen.
    win.blit(paddle1_life_label,p1flRect)
    win.blit(paddle1_points_label,p1plRect)
    win.blit(paddle1_life,p1fRect)
    win.blit(paddle1_score,p1pRect)
    win.blit(text,textRect)
    win.blit(textb,textbRect)
    win.blit(textc,textcRect)
    all_sprites.draw(win)
    pygame.display.update()

def game_over_screen():
    win.fill(white)
    font = pygame.font.SysFont('Comic Sans MS',30)
    text = font.render("Game over",False,black)
    textb = font.render("Quit or stay y/n",False,black)
    
    textbRect = textb.get_rect()
    textbRect.center = (375,250)
    
    textRect = text.get_rect()
    textRect.center = (375,200)

    #Player points.
    paddle1_score = font.render(str(paddle1.points),False,black)
    p1pRect = paddle1_score.get_rect()
    p1pRect.center = (375,150)

    #Adds text to screen.
    win.blit(paddle1_score,p1pRect)
    win.blit(text,textRect)
    win.blit(textb,textbRect)
    pygame.display.update()




#Window/game loop.
game_over = False
run = True
while run:
    pygame.time.delay(100)
    if game_over==True:
        run = False
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        paddle1.rect.x += paddle_speed
    if key[pygame.K_a]:
        paddle1.rect.x -= paddle_speed
    if key[pygame.K_o]:
        paddle_speed += 10
    if key[pygame.K_k]:
        paddle_speed -= 10
    if key[pygame.K_i]:
        ball.speed += 1
    if key[pygame.K_j]:
        ball.speed -= 1
    if paddle1.rect.x > 692:
        paddle1.rect.x = 0
    if paddle1.rect.x < 0:
        paddle1.rect.x = 692
        
    ball.rect.x += ball.speed * ball.dx
    ball.rect.y += ball.speed * ball.dy

    if ball.rect.y > 500:
        paddle1.life -= 1
        if paddle1.life == 0:
            game_over = True
        ball.dy = -1

    if ball.rect.x > 750:
        ball.dx = -1
    if ball.rect.y < 0:
        ball.dy = 1
    if ball.rect.x < 0:
        ball.dx = 1

    if paddle1.rect.colliderect(ball):
        ball.dy = -1
        paddle1.points += 1


    redraw()


#Game over window loop.
while game_over == True:
    key = pygame.key.get_pressed()
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
    if key[pygame.K_n]:
        game_over = False   
    if key[pygame.K_y]:
        pygame.quit()
        subprocess.call("rerun.bat")
    game_over_screen()

#Ends program.
pygame.quit()