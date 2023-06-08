#Создай собственный Шутер!
from random import randint
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, plw, plh, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(plw,plh))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): 
    def update2(self): 
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_DOWN] and self.rect.y < 395: 
            self.rect.y +=self.speed 
        if keys_pressed[K_UP] and self.rect.y>0: 
            self.rect.y -= self.speed 
        if keys_pressed[K_LEFT] and self.rect.x>0: 
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 680: 
            self.rect.x +=self.speed
    def update(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_s] and self.rect.y < 395: 
            self.rect.y +=self.speed 
        if keys_pressed[K_w] and self.rect.y>0: 
            self.rect.y -= self.speed 
        if keys_pressed[K_a] and self.rect.x>0: 
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 680: 
            self.rect.x +=self.speed
    def update3(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_k] and self.rect.y < 395: 
            self.rect.y +=self.speed 
        if keys_pressed[K_i] and self.rect.y>0: 
            self.rect.y -= self.speed 
        if keys_pressed[K_j] and self.rect.x>0: 
            self.rect.x -= self.speed
        if keys_pressed[K_l] and self.rect.x < 680: 
            self.rect.x +=self.speed


window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('bcr.jpg'),(700,500))


player = Player('bar.png',50,200,20, 120, 3)
player2 = Player('bar.png',650,200,20, 120, 3)
player3 = Player('ozel.png',350,250,90, 60, 10)

finish = False

font.init()
font = font.Font(None, 50)
pol = font.render('Player1 Lose!', True, (100, 210, 190))
ptl = font.render('Player2 Lose!', True, (100, 210, 190))

ball = GameSprite('balllll.png', 320, 220, 50, 50, 0)

ball_y = 3
ball_x = 3

game = True
clock = time.Clock()
FPS = 120
while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.reset() 
        player.update()
        player2.reset() 
        player2.update2()
        player3.reset()
        player3.update3()
        ball.rect.x += ball_x
        ball.rect.y += ball_y
        if ball.rect.y > 450 or ball.rect.y <0:
            ball_y *= -1
        if sprite.collide_rect(ball,player) or sprite.collide_rect(ball,player2) or sprite.collide_rect(ball,player3):
            ball_x *= -1
        if ball.rect.x < -10:
            finish = True
            window.blit(pol, (260,220))
        if ball.rect.x > 700:
            finish = True
            window.blit(ptl, (260,220))
        ball.reset()
        clock.tick(FPS) 
        display.update() 
    else:
        finish = False
        time.delay(3000)