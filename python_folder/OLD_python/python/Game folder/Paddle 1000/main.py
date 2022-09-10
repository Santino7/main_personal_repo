

#By Santino .J. Tomasi
#Date 5/6/2022
#Version beta

import pygame

pygame.init()

win_x = 750
win_y = 500

win = pygame.display.set_mode((win_x,win_y))

pygame.display.set_caption("Paddle 1000!")

black = (0,0,0)

white = (255,255,255)

#Paddle class.
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
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


#Sets ball position.
offical_paddle_1000_ball = Ball()
offical_paddle_1000_ball.rect.x = 375
offical_paddle_1000_ball.rect.y = 250

#Puts all sprites into all_sprites group.
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1,offical_paddle_1000_ball)

#Paddle speed for both paddles.
all_paddle_speed = 50.5


def redraw():
    win.fill(black)
    font = pygame.font.SysFont('Comic Sans MS',30)
    text = font.render('Paddle 1000!,the POWER of gamers',False,white)
    textRect = text.get_rect()
    textRect.center = (750//2,25)
    win.blit(text,textRect)

#Paddle1 Score.
    player1_score= font.render(str(paddle1.points),False, white)
    p1Rect = player1_score.get_rect()
    p1Rect.center = (50,50)
    win.blit(player1_score,p1Rect)


#Window loop.
run = True
while run:
    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    redraw()
    
pygame.quit()