import math as m
import pygame
from pygame.draw import *

def cloud(a,b,r):
    c = a
    for i in range(4):
        circle(screen, (149, 146, 146), (c, b), r, 5)
        circle(screen, (255, 255, 255), (c, b), r-2)
        c = c + 30
    c = c - 50
    b = b - 25
    for i in range(2):
        circle(screen, (149, 146, 146), (c, b), r, 5)
        circle(screen, (255, 255, 255), (c, b), r-2)
        c = c - 50

def circtree(a,b,r):
    circle(screen, (16, 66, 25), (a, b), r, 5)
    circle(screen, (6, 82, 6), (a, b), r-4)

def sun(a,b,r1,r2,n):
    pi2 = 2*3.14
    for i in range(0, n):
        polygon(screen, (125, 148, 152), [(a, b), (m.cos(i / n * pi2) * r1 + a, m.sin(i / n * pi2) * r1 + b),(m.cos((i + 1) / n * pi2) * r2 + a, m.sin((i + 1) / n * pi2) * r2 + b),(a, b)], 2)
        polygon(screen, (125, 148, 152),[(a, b), (m.cos((i + 1) / n * pi2) * r2 + a, m.sin((i + 1) / n * pi2) * r2 + b),(m.cos((i + 2) / n * pi2) * r1 + a, m.sin((i + 2) / n * pi2) * r1 + b), (a, b)], 2)
        polygon(screen, (249, 195, 195), [(a,b), (m.cos(i/n*pi2)*r1 + a, m.sin(i/n*pi2)*r1 + b), (m.cos((i+1)/n*pi2)*r2+a, m.sin((i+1)/n*pi2)*r2+b), (a,b)])
        polygon(screen, (249, 195, 195), [(a, b), (m.cos((i+1) / n * pi2) * r2 + a, m.sin((i+1) / n * pi2) * r2 + b),(m.cos((i+2) / n * pi2) * r1 + a, m.sin((i + 2) / n * pi2) * r1 + b),(a, b)])
        circle(screen, (249, 195, 195), (a,b+2), 31)
def home(a,b,c,d):

    rect(screen, (86, 68, 14), (a, b, c, d), 5)
    rect(screen, (148, 107, 6), (a,b,c,d))
    rect(screen, (5, 148, 146), (a+(c/3), b +(d/3), c/3, d/3))
    rect(screen, (177, 100, 6), (a + (c / 3), b + (d / 3), c / 3, d / 3), 5)
    polygon(screen, (236, 43, 66), [(a, b), (a+(c/2), b-d), (a+c, b)])
    polygon(screen, (86, 68, 14), [(a,b), (a+(c/2),b-d), (a+c,b)], 5)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 650))

rect(screen, (159, 235, 245), (0, 0, 1000, 325))
rect(screen, (5, 148, 32), (0, 325, 1000, 325))
home(100,340,300,200)
home(600,320,150,100)
cloud(200,100,40)
cloud(450,150,30)
cloud(850,100,40)
circtree(500, 220, 40)
circtree(455, 255, 40)
circtree(545, 255, 40)
circtree(500, 295, 40)
rect(screen, (30, 5, 0), (490, 320, 25, 120))
circtree(465, 320, 40)
circtree(535, 325, 40)
sun(80, 80, 30, 40, 25)
circtree(850, 240, 25)
circtree(825, 265, 25)
circtree(875, 265, 25)
circtree(850, 290, 25)
rect(screen, (30, 5, 0), (840, 305, 15, 80))
circtree(825, 305, 25)
circtree(870, 310, 25)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()