import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((700, 500))

def people(a, x, y):
    window = pygame.Surface((200, 500))
    window.fill((255, 255, 255))
    rect(window, (112, 239, 243), (0, 0, 200, 250))
    rect(window, (41, 212, 92), (0, 250, 200, 250))
    if a == 1 or a == 4:
        ellipse(window, (210, 121, 238), (110, 230, 50, 110))
        circle(window, (255, 255, 255), (135, 215), 25)
        line(window, (0, 0, 0), (72, 297), (117, 252))
        line(window, (0, 0, 0), (152, 252), (200, 300))
    if a == 2 or a == 3:
        polygon(window, (255, 78, 231), [(100, 215), (70, 340), (130, 340)])
        circle(window, (255, 255, 255), (100, 215), 25)
        line(window, (0, 0, 0), (0, 300), (90, 252))
        line(window, (0, 0, 0), (110, 251), (140, 265))
        line(window, (0, 0, 0), (140, 265), (200, 251))
    if a == 3:
        window = pygame.transform.flip(window, True, False)
    screen.blit(window, (x, y))




#background
rect(screen, (112, 239, 243), (0, 0, 800, 250))
rect(screen, (41, 212, 92), (0, 250, 800, 250))

people(1, 0, 0)
people(2, 200, 0)
people(3, 400, 0)
people(4, 500, 0)

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
polygon(screen, (243, 243, 1),   [(645, 300), (652, 253), (685, 280)])
circle(screen, (114, 58,  16),   (665, 257),  15)
circle(screen, (255, 10,  10),   (680, 269),  15)
circle(screen, (255, 255, 255),  (680, 247),  15)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()