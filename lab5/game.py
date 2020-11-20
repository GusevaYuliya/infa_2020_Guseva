import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 70
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



cdvig = [-6, -5, -4, 4, 5, 6]

sum = 0

clock = pygame.time.Clock()
finished = False


x = haracterball(100, 700)
y = haracterball(100, 500)
r = haracterball(30, 50)
color = COLORS[randint(0, 5)]
vx = [cdvig[randint(0, 5)], cdvig[randint(0, 5)], cdvig[randint(0, 5)], cdvig[randint(0, 5)], cdvig[randint(0, 5)]]
vy = [cdvig[randint(0, 5)], cdvig[randint(0, 5)], cdvig[randint(0, 5)], cdvig[randint(0, 5)], cdvig[randint(0, 5)]]

while not finished:
    click = False
    while finished == False:
        for i in range(5):
            circle(screen, color, (x[i], y[i]), r[i])
            x[i] = x[i] + vx[i]
            y[i] = y[i] + vy[i]
            clock.tick(FPS)
            if x[i] + r[i] >= maxx or x[i] - r[i] <= 0:
                vx[i] = vx[i] * (-1)
            if y[i] + r[i] >= maxy or y[i] - r[i] <= 0:
                vy[i] = vy[i] * (-1)
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(5):
                    if (x[i] - event.pos[0]) ** 2 + (y[i] - event.pos[1]) ** 2 <= r[i] ** 2:
                        sum += 1
                        print('счет ', sum)
                        r[i] = 0
        k=0
        for i in range(5):
            if r[i] == 0:
                k = k + 1
        if k == 5:
            finished = True





pygame.quit()
