import math as m
import pygame
from pygame.draw import *

def circloud(a,b):
    circle(screen, (149, 146, 146), (a, b), 30, 3)
    circle(screen, (255, 255, 255), (a, b), 28)
def circtree(a,b):
    circle(screen, (16, 66, 25), (a, b), 40, 5)
    circle(screen, (6, 82, 6), (a, b), 36)
def draw_ngon(surface, color, n, radius, position):
    pi2 = 2 * 3.14
    for i in range(0,n):
        line(surface,color,position, (m.cos(i/n*pi2)*radius + position[0], m.sin(i/n*pi2)*radius+position[1]))
    return lines(surface, color, True, [(m.cos(i/n*pi2)*radius + position[0], m.sin(i/n*pi2)*radius + position[1]) for i in range(0,n)])
#def sun(a,b,n):
#    for i in range(0, n):
#        polygon(screen, (249,195,195), [(a,b), (a+3,b+3), (a,b+6)])


pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 520))

rect(screen, (159, 235, 245), (0, 0, 800, 260))
rect(screen, (5, 148, 32), (0, 260, 800, 260))
rect(screen, (86, 68, 14), (120, 220, 220, 150), 5)
rect(screen, (148, 107, 6), (122, 222, 215, 145))
rect(screen, (5, 148, 146), (190, 260, 80, 60))
polygon(screen, (236, 43, 66), [(120,220), (230, 100), (340, 220)])
polygon(screen, (86, 68, 14), [(120, 220), (230, 100), (340, 220)], 5)
circloud(390, 80)
circloud(420, 80)
circloud(450, 80)
circloud(480, 80)
circloud(450, 60)
circloud(410, 60)
circtree(600, 120)
circtree(550, 160)
circtree(650, 160)
circtree(600, 190)
rect(screen, (30, 5, 0), (585, 245, 20, 110))
circtree(560, 220)
circtree(630, 225)
draw_ngon(screen, 2, 50, 50, [100,100])





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()