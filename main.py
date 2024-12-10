import sys
from random import choice

import pygame
from sys import exit

def ball_animation():

    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= choice((1,-1))

pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')
game_active = True

ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(screen_width-10,screen_height/2-70,10,140)
opponent = pygame.Rect(0, screen_height/2-70, 10, 140)

#ball1 = pygame.image.load('snowball.png')
#ball1_rect = ball1.get_rect(center=(600,400))

ball_speed_x = 7 * choice((1,-1))
ball_speed_y = 7 * choice((1,-1))
player_speed = 0
opponent_speed = 7

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill((100,0,0))

#    screen.blit(ball1, ball1_rect)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)
    pygame.draw.rect(screen, (200,200,200), player)
    pygame.draw.rect(screen, (200,200,200), opponent)
    pygame.draw.aaline(screen, (200,200,200), (screen_width/2,0), (screen_width/2,screen_height))

    pygame.display.update()
    clock.tick(60)