import pygame
from pygame.draw import *
from random import randint

pygame.init()

name = input('введите имя игрока ', )
level = int(input('введите сложность уровня от 10 до 99 ', ))
t = level // 10
s = level % 10

FPS = 150
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

color = []
for i in range(20):
    color.append(COLORS[randint(0, 5)])

def haracterfig(n, m, l):
    coord = []
    for i in range(l):
        coord.append(randint(n, m))
    return coord

'''задаем характеристики кругов'''
xb = haracterfig(100, 700, t)
yb = haracterfig(100, 500, t)
r = haracterfig(30, 50, t)
vxb = haracterfig(-6, 6, t)
vyb = haracterfig(-6, 6, t)

'''задаем характеристики квадратов'''
xr = haracterfig(100, 700, s)
yr = haracterfig(100, 500, s)
ar = haracterfig(30, 70, s)
br = haracterfig(30, 70, s)
vxr = haracterfig(-3, 3, s)
vyr = haracterfig(-3, 3, s)

sum = 0

clock = pygame.time.Clock()
finished = False

while not finished:
    while finished == False:
        '''рисуем круги'''
        for i in range(t):
            circle(screen, color[i], (xb[i], yb[i]), r[i])
            xb[i] = xb[i] + vxb[i]
            yb[i] = yb[i] + vyb[i]
            clock.tick(FPS)
            if xb[i] + r[i] >= maxx or xb[i] - r[i] <= 0:
                vxb[i] = vxb[i] * (-1)
            if yb[i] + r[i] >= maxy or yb[i] - r[i] <= 0:
                vyb[i] = vyb[i] * (-1)
        '''рисуем квадраты'''
        for i in range(s):
            rect(screen, color[i], (xr[i], yr[i], ar[i], br[i]))
            xr[i] = xr[i] + vxr[i]
            yr[i] = yr[i] + vyr[i]
            clock.tick(FPS)
            if xr[i] + ar[i] >= maxx:
                xr[i] = 1
            elif xr[i] <= 0:
                xr[i] = maxx - 1 - ar[i]
            if yr[i] + br[i] >= maxy:
                yr[i] = 1
            elif yr[i] <= 0:
                yr[i] = maxy - 1 - br[i]
        pygame.display.update()
        screen.fill(BLACK)
        '''проверка на попадание в цель'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(t):
                    if (xb[i] - event.pos[0]) ** 2 + (yb[i] - event.pos[1]) ** 2 <= r[i] ** 2:
                        sum += 1
                        print('счет ', sum)
                        r[i] = 0
                for i in range(s):
                    if (event.pos[0] >= xr[i]) and (event.pos[0] <= (xr[i] + ar[i])) and (event.pos[1] >= yr[i]) and (event.pos[1] <= (yr[i] + br[i])):
                        sum += 2
                        print('счет ', sum)
                        ar[i] = 0
        k=0
        for i in range(t):
            if r[i] == 0:
                k = k + 1
        for i in range(s):
            if ar[i] == 0:
                k = k + 1
        if k == t + s:
            print(name, 'итоговый счет: ', sum)
            finished = True

pygame.quit()

str = name + ' ' + str(sum) + ' '
f = open('igroki.txt', 'a')
f.write(str)
f.close()