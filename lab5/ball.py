import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

'''задаем цвет'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def ballxyr(event):
    '''записывает координаты круга'''
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

sum = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            ballxyr(event)
            if (x-event.pos[0])**2 + (y - event.pos[1])**2 <= r**2:
                sum += 1
                print('счет ', sum)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()