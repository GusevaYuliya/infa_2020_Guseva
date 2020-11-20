import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))

maxx=1200
maxy=800

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def haracterball(n,m):
    coord = []
    for i in range(5):
        coord.append(randint(n, m))
    return coord



cdvig = [-3, -2, -1, 1, 2, 3]

sum = 0

clock = pygame.time.Clock()
finished = False
click = False

x = haracterball(100, 700)
y = haracterball(100, 500)
r = haracterball(30, 50)
color = COLORS[randint(0, 5)]
vx = cdvig[randint(0, 5)]
vy = cdvig[randint(0, 5)]

while not finished:
    click = False
    while (finished == False) and (click == False):
        for i in range(5):
            circle(screen, color, (x[i], y[i]), r[i])
            x[i] = x[i] + vx
            y[i] = y[i] + vy
            clock.tick(FPS)
            if x[i] + r[i] >= maxx or x[i] - r[i] <= 0:
                vx = vx * (-1)
            if y[i] + r[i] >= maxy or y[i] - r[i] <= 0:
                vy = vy * (-1)
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
                    sum += 1
                    print('счет ', sum)
                    click = True


pygame.quit()
