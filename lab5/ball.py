import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))

maxx = 1200
maxy = 800

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def ballwindow(x,y,r):
    window = pygame.Surface((2*r, 2*r))
    window.fill((0, 0, 0))
    circle(window, color, (r, r), r)
    screen.blit(window, (x, y))

cdvig = [-3, -2, -1, 1, 2, 3]

sum = 0


clock = pygame.time.Clock()
finished = False
click = False

while not finished:
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    vx = cdvig[randint(0, 5)]
    vy = cdvig[randint(0, 5)]
    click = False
    while (finished == False) and (click == False):
        ballwindow(x, y, r)
        x = x + vx
        y = y + vy
        clock.tick(FPS)
        if x + (2*r) >= maxx or x <= 0:
            vx = vx * (-1)
        if y + (2 * r) >= maxy or y <= 0:
            vy = vy * (-1)
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                if ((x+r) - event.pos[0]) ** 2 + ((y+r) - event.pos[1]) ** 2 <= r ** 2:
                    sum += 1
                    print('счет ', sum)
                    click = True


pygame.quit()
