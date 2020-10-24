import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((800, 500))



def people(a, x, y):
    if a == 1 or a == 4:
        window = pygame.Surface((200, 500))
        window.fill((255, 255, 255))
        rect(window, (112, 239, 243), (0, 0, 200, 250))
        rect(window, (41, 212, 92), (0, 250, 200, 250))
        ellipse(window, (210, 121, 238), (110, 230, 50, 110))
        circle(window, (255, 255, 255), (135, 215), 25)
        line(window, (0, 0, 0), (72, 297), (117, 252))
        line(window, (0, 0, 0), (152, 252), (197, 300))
        screen.blit(window, (x, y))
    else:
        window = pygame.Surface((200, 500))
        window.fill((255, 255, 255))
        rect(window, (112, 239, 243), (0, 0, 200, 250))
        rect(window, (41, 212, 92), (0, 250, 200, 250))
        polygon(screen, (255, 78, 231), [(300, 215), (270, 340), (330, 340)])
        circle(screen, (255, 255, 255), (300, 215), 25)
        line(screen, (0, 0, 0), (197, 300), (290, 252))
        line(screen, (0, 0, 0), (310, 251), (340, 265))
        line(screen, (0, 0, 0), (340, 265), (370, 251))
        screen.blit(window, (x, y))


people(1, 0, 0)
'''
#background
rect(screen,   (112, 239, 243),  (0,   0,   800, 250))
rect(screen,   (41,  212, 92),   (0,   250, 800, 250))

#icecream1
line(screen,   (0,   0,   0),    (50, 205), (75,300))
polygon(screen,(255, 10,  10),  [(15,160),(65,155),(50,205)])
circle(screen,(255, 10,  10, ),(30,155),(15))
circle(screen,(255, 10,  10, ),(50,155),(15))


#kid1
ellipse(screen,(210, 121, 238),  (110, 230,  50, 110))
circle(screen, (255, 255, 255),  (135, 215), 25)
line(screen,   (0,   0,   0),    (72, 297), (117,252))
line(screen,   (0,   0,   0),    (152,252), (197,300))


#kid2
polygon(screen,(255, 78,  231), [(300, 215),(270,340),(330,340)])
circle(screen, (255, 255, 255),  (300, 215), 25)
line(screen,   (0,   0,   0),    (197,300),(290,252))
line(screen,   (0,   0,   0),    (310,251),(340,265))
line(screen,   (0,   0,   0),    (340,265),(370,251))

#icecream2
line(screen,   (0,   0,   0),    (368,252),(380,132))
polygon(screen,(243, 243, 1),   [(382,133),(352,80),(412,75)])
circle(screen, (114, 58,  16),   (368,80),  15)
circle(screen, (255, 10,  10),   (395,80),  15)
circle(screen, (255, 255, 255),  (381,60),  15)

#kid3
polygon(screen,(255, 78, 231),  [(440, 215),(410,340),(470,340)])
circle(screen, (255, 255, 255),  (441, 215), 25)
line(screen,   (0,   0,   0),    (370,250),(400,265))
line(screen,   (0,   0,   0),    (400,265),(430,252))
line(screen,   (0,   0,   0),    (449,252),(510,297))


#kid4
ellipse(screen,(210, 121, 238),  (560, 230,  50, 110))
circle(screen, (255, 255, 255),  (585, 215), 25)
line(screen,   (0  , 0,   0),    (507,295),(565,252))
line(screen,   (0,   0,   0),    (604,252),(645,297))

#icecream3
polygon(screen,(243, 243, 1),   [(645,300),(652,253),(685,280)])
circle(screen, (114, 58,  16),   (665,257),  15)
circle(screen, (255, 10,  10),   (680,269),  15)
circle(screen, (255, 255, 255),  (680,247),  15)
'''

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()