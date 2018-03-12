import pygame
from math import *

window = pygame.display.set_mode((500,500))
pygame.display.set_caption('Zashita')

screen = pygame.Surface((500,500))

okno = pygame.Surface((40,40))
#tucha = pygame.Surface((150,100))
#sun = pygame.Surface((90,90))


    
done = True
tuchaflag = True
x = 450

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    
    if x > 100 and  x < 280:
        color = (255,255,0)
    else:
        color = (255,255,255)



    screen.fill((255,255,255))
    okno.fill((color))
    #tucha.fill((100,100,100))


    pygame.draw.circle(screen,(255,255,0),[250,100],45)

    

    
    if tuchaflag == True:
        x -= 1
        if x <= -200:
            tuchaflag = False
    else:
        x = 600
        tuchaflag = True

    screen.blit(okno,(110,320))
    #screen.blit(tucha,(x,50))
    

    #Домик
    pygame.draw.rect(screen,(0,0,0),(50,250,150,200),3)
    pygame.draw.line(screen,(0,0,0),(50,250),(125,150),4)
    pygame.draw.line(screen,(0,0,0),(125,150),(200,250),4)
    pygame.draw.line(screen,(0,0,0),(85,200),(85,150),4)
    pygame.draw.line(screen,(0,0,0),(85,150),(65,150),4)
    pygame.draw.line(screen,(0,0,0),(65,150),(65,228),4)
    pygame.draw.rect(screen,(0,0,0),(110,320,40,40),6)

    pygame.draw.ellipse(screen,(100,100,100),(x,50,200,100))
    



    
    
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(10)
                      
