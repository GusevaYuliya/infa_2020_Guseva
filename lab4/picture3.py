import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((700, 500))

def people(a, x, y, t):
    if a == 1 or a == 4:
        window = pygame.Surface((200*t//4, 500*t//4))
        window.fill((255, 255, 255))
        window.set_colorkey((255, 255, 255))
        rect(window, (41, 212, 92), (0, 500*t//4/2+15, 200, 500*t//4/2+15))
        line(window, (0, 0, 0), (90*t//4, 400*t//4), (100*t//4, 400*t//4))
        line(window, (0, 0, 0), (100*t//4, 400*t//4), (130*t//4, 335*t//4))
        line(window, (0, 0, 0), (140*t//4, 335*t//4), (140*t//4, 400*t//4))
        line(window, (0, 0, 0), (140*t//4, 400*t//4), (150*t//4, 400*t//4))
        ellipse(window, (210, 121, 238), (110*t//4, 230*t//4, 50*t//4, 110*t//4))
        circle(window, (254, 255, 255), (135*t//4, 215*t//4), 25*t//4)
        line(window, (0, 0, 0), (72*t//4, 297*t//4), (117*t//4, 252*t//4))
        line(window, (0, 0, 0), (152*t//4, 252*t//4), (200*t//4, 300*t//4))

    if a == 2 or a == 3:
        window = pygame.Surface((170, 500))
        window.fill((255, 255, 255))
        rect(window, (112, 239, 243), (0, 0, 200, 250))
        rect(window, (41, 212, 92), (0, 250, 200, 250))
        line(window, (0, 0, 0), (80, 400), (90, 400))
        line(window, (0, 0, 0), (90, 400), (90, 335))
        line(window, (0, 0, 0), (110, 335), (110, 400))
        line(window, (0, 0, 0), (110, 400), (120, 400))
        polygon(window, (255, 78, 231), [(100, 215), (70, 340), (130, 340)])
        circle(window, (255, 255, 255), (100, 215), 25)
        line(window, (0, 0, 0), (0, 300), (90, 252))
        line(window, (0, 0, 0), (110, 251), (140, 265))
        line(window, (0, 0, 0), (140, 265), (170, 251))
    if a == 3 or a == 4:
        window = pygame.transform.flip(window, True, False)
    screen.blit(window, (x, y))




#background
rect(screen, (112, 239, 243), (0, 0, 700, 250))
rect(screen, (41, 212, 92), (0, 250, 700, 250))

people(1, 0, 0, 4)
people(2, 200, 0, 4)
people(3, 370, 0, 4)
people(4, 490, 50, 3)




#icecream1
line(screen, (0, 0, 0), (50, 205), (75, 300))
polygon(screen, (255, 10,  10),  [(15, 160), (65, 155), (50, 205)])
circle(screen, (255, 10,  10), (30, 155), 15)
circle(screen, (255, 10,  10), (50, 155), 15)

#icecream2
line(screen, (0,   0,   0), (368, 252), (380, 132))
polygon(screen, (243, 243, 1),   [(382, 133), (352, 80), (412, 75)])
circle(screen, (114, 58,  16),   (368, 80),  15)
circle(screen, (255, 10,  10),   (395, 80),  15)
circle(screen, (255, 255, 255),  (381, 60),  15)

#icecream3
polygon(screen, (243, 243, 1),   [(585, 275), (602, 228), (635, 255)])
circle(screen, (114, 58,  16),   (615, 227),  15)
circle(screen, (255, 10,  10),   (630, 239),  15)
circle(screen, (255, 255, 255),  (630, 217),  15)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()