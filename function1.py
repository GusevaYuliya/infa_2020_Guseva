import pygame
from pygame.draw import *
from random import randint

pygame.init()

maxx = int(input('введите длину поля ', ))
maxy = int(input('введите ширину поля ', ))

FPS = 30
screen = pygame.display.set_mode((maxx, maxy))

rect(screen, (100, 100, 100), (50, 50, 50, 50))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
