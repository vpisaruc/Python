import pygame
from math import *

window = pygame.display.set_mode((400,400))
pygame.display.set_caption('Zashita')

screen = pygame.Surface((400,400))


Xc = 200
Yc = 300
x = 170
y = 260
_1x = 230
_1y = 340
teta = -1*pi/12
    
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    screen.fill((255,255,255))

    

    x1 =Xc + ((x - Xc)*cos(teta) + (y - Yc)*sin(teta))
    y1 =Yc + ((y - Yc)*cos(teta) - (x - Xc)*sin(teta))
    x = x1
    y = y1

    x1 =Xc + ((_1x - Xc)*cos(teta) + (_1y - Yc)*sin(teta))
    y1 =Yc + ((_1y - Yc)*cos(teta) - (_1x - Xc)*sin(teta))
    _1x = x1
    _1y = y1
        
    pygame.draw.circle(screen,(0,0,0),[200,300],50,5)
    pygame.draw.line(screen,(0,0,0),(Xc,Yc),(x,y),5)
    pygame.draw.line(screen,(0,0,0),(Xc,Yc),(_1x,_1y),5)
    
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(50)
                      
