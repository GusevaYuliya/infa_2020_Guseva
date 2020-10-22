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

def tree(a,b,r):
    c = a
    d = b
    circle(screen, (16, 66, 25), (c, d), r, 5)
    circle(screen, (6, 82, 6), (c, d), r)
    c = c - (3/2*r)
    d = d + (3/2*r)
    circle(screen, (16, 66, 25), (c, d), r, 5)
    circle(screen, (6, 82, 6), (c, d), r)
    c = c + (3*r)
    circle(screen, (16, 66, 25), (c, d), r, 5)
    circle(screen, (6, 82, 6), (c, d), r)
    c = c
    rect(screen, (30, 5, 0), (c, d, 20, 110))

    circtree(600, 120)
    circtree(550, 160)
    circtree(650, 160)
    circtree(600, 190)

    circtree(560, 220)
    circtree(630, 225)
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
'''''''''
circtree(600, 120)
circtree(550, 160)
circtree(650, 160)
circtree(600, 190)
rect(screen, (30, 5, 0), (585, 245, 20, 110))
circtree(560, 220)
circtree(630, 225)
'''''
sun(80, 80, 30, 40, 25)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()