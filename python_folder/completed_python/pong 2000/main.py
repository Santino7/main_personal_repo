#Pong 2000 version 2.2
#By Santino .J. Tomasi
#Date of current version 4/28/2022
#Date of version 1 4/28/2022
#Version 1 notes.
#Version 1 was the making of the base game.
#Version 2 notes.
#Version to added the abilty to change the balls speed with the keys i and j.
#Version 2.1 notes.
#Version 2.1 added a cap so that you could not get negative speed but you may get -1 speed if you continue to hold down j.
#Version 2.2 notes.
#Now after the ball hits on of the players goals then the ball woll respawn in the center of the screen.

from turtle import speed
import pygame

pygame.init()

#Orginal win_x and win_y is 750x and 500y.
win_x = 750
win_y = 500

win = pygame.display.set_mode((win_x,win_y))

pygame.display.set_caption("Pong 2000")

white = (255,255,255)

black = (0,0,0)

#Universal Paddle class.
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0


#Ball class.
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1

#Sets paddle1 position.
paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

offical_pong_2000_ball = Ball()
offical_pong_2000_ball.rect.x = 375
offical_pong_2000_ball.rect.y = 250


#Puts all sprites into all_sprites group.
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1,paddle2,offical_pong_2000_ball)

#Paddle speed for both paddles.
all_paddle_speed = 50.5

def redraw():
    win.fill(black)
    font = pygame.font.SysFont('Comic Sans MS',30)
    text = font.render('Pong 2000!,the future of gamers',False,white)
    textRect = text.get_rect()
    textRect.center = (750//2,25)
    win.blit(text,textRect)

    #Player 1 Score.
    player1_score= font.render(str(paddle1.points),False, white)
    p1Rect = player1_score.get_rect()
    p1Rect.center = (50,50)
    win.blit(player1_score,p1Rect)

    #Player 2 Score.
    player2_score= font.render(str(paddle2.points),False, white)
    p2Rect = player2_score.get_rect()
    p2Rect.center = (700,50)
    win.blit(player2_score,p2Rect)

    all_sprites.draw(win)
    pygame.display.update()





#Window loop.
run = True
while run:
    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y += -all_paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y += all_paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y += -all_paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += all_paddle_speed
    if key[pygame.K_i]:
        offical_pong_2000_ball.speed = offical_pong_2000_ball.speed + 1
    if key[pygame.K_j]:
        offical_pong_2000_ball.speed = offical_pong_2000_ball.speed - 1
    if offical_pong_2000_ball.speed < 0:
        offical_pong_2000_ball.speed = 1

    if paddle1.rect.bottom >500:
        paddle1.rect.bottom = 500
    if paddle2.rect.bottom >500:
        paddle2.rect.bottom = 500
    if paddle1.rect.top <0:
        paddle1.rect.top = 0
    if paddle2.rect.top <0:
        paddle2.rect.top = 0

    offical_pong_2000_ball.rect.x += offical_pong_2000_ball.speed * offical_pong_2000_ball.dx

    offical_pong_2000_ball.rect.y += offical_pong_2000_ball.speed * offical_pong_2000_ball.dy

    #Ball x is 375 and y is 250.
    if offical_pong_2000_ball.rect.y > 500:
        offical_pong_2000_ball.dy = -1
    if offical_pong_2000_ball.rect.x > 750:
        offical_pong_2000_ball.rect.x = 375
        offical_pong_2000_ball.rect.y = 250
        paddle1.points = paddle1.points+1
    if offical_pong_2000_ball.rect.top < 0:
        offical_pong_2000_ball.dy = 1
    if offical_pong_2000_ball.rect.x < 0:
        offical_pong_2000_ball.rect.x = 375
        offical_pong_2000_ball.rect.y = 250
        paddle2.points = paddle2.points+1
    if paddle1.rect.colliderect(offical_pong_2000_ball.rect):
        offical_pong_2000_ball.dx = 1
    if paddle2.rect.colliderect(offical_pong_2000_ball.rect):
        offical_pong_2000_ball.dx = -1

    redraw() 

pygame.quit()
