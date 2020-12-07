import pygame
from pygame.draw import *
import time


pygame.init()

'''  действия выполняемые пользователем'''
maxx = int(input('введите длину поля ', ))
maxy = int(input('введите ширину поля ', ))
input('для отрисовки многоуголька: 1)нажмите enter 2) отметьте точки мышкой на поверхности  3)нажмите пробел')

FPS = 30
''' создание поля'''
screen = pygame.display.set_mode((maxx, maxy))
screen.fill((255, 255, 255))
pygame.display.update()


clock = pygame.time.Clock()

''' функция рисует многоугольник и возвращает список координат вершин'''
def coords():
    coord = []
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                '''при нажатии левой кнопки мыши ставит точку, координты точки помещает в список'''
                if event.button == 1:
                    circle(screen, (100, 100, 100), event.pos, 1)
                    s = event.pos
                    coord.append(s)
                    pygame.display.update()
            elif event.type == pygame.KEYDOWN:
                ''' при нажатии пробела рисует многоульник, ждет пару секунд и заверщает цикл'''
                if event.key == pygame.K_SPACE:
                    polygon(screen, (100, 100, 100), coord, 5)
                    pygame.display.update()
                    time.sleep(3)
                    finished = True
    return coord

t = coords()

pygame.quit()
''' не умею сбоку писать комментарии, поэтому простите, что они в самой программе :))'''
