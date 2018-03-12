import pygame
window = pygame.display.set_mode((400,400))
pygame.display.set_caption('Animation')

screen = pygame.Surface((400,400))

square1 = pygame.Surface((40,100))
square2 = pygame.Surface((40,100))
aircraft = pygame.Surface((150,40))

square1.fill((255,255,255))
square2.fill((255,255,255))
aircraft.fill((255,255,255))

x = 0
y = 0

square_go_right = True
aircraft_go_right = True

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    screen.fill((255,255,255))

    # Анимация солдат
    if square_go_right == True:
        x += 1
        if x > 130:
            square_go_right = False
            pygame.draw.line(square1,(0,0,0), [35,60],[20,20],3)
            pygame.draw.line(square2,(0,0,0), [6,60],[20,30],3)
            

    # Анимация самолёт
    if aircraft_go_right == True:
        y += 4.5
        if y > 450:
            aircraft_go_right = False
    else:
        y = -150
        aircraft_go_right = True
    

    screen.blit(square1, (x, 250))        
    screen.blit(square2, (290 + (-1 * (x - 40)), 250 ))
    screen.blit(aircraft,(y,30))

    # Будка
    line = pygame.draw.line(screen,(0,0,0), [380,350],[380,200],4)
    line = pygame.draw.line(screen,(0,0,0), [380,200],[325,200],4)
    line = pygame.draw.line(screen,(0,0,0), [325,200],[315,210],6)    

    # Звезда
    line = pygame.draw.line(screen,(255,0,0), [130,210],[165,155],5)
    line = pygame.draw.line(screen,(255,0,0), [165,155],[100,130],5)
    line = pygame.draw.line(screen,(255,0,0), [100,130],[165,130],5)
    line = pygame.draw.line(screen,(255,0,0), [165,130],[180,85],5)
    line = pygame.draw.line(screen,(255,0,0), [180,85],[195,130],5)
    line = pygame.draw.line(screen,(255,0,0), [195,130],[260,130],5)
    line = pygame.draw.line(screen,(255,0,0), [260,130],[195,155],5)
    line = pygame.draw.line(screen,(255,0,0), [195,155],[230,210],5)
    line = pygame.draw.line(screen,(255,0,0), [230,210],[180,165],6)
    pygame.draw.line(screen,(255,0,0), [180,165],[130,210],6)


    # Человек 1
    pygame.draw.line(square1,(0,0,0), [0,100],[15,100],5)
    pygame.draw.line(square1,(0,0,0), [25,100],[40,100],5)
    pygame.draw.line(square1,(0,0,0), [0,100],[20,70],3)
    pygame.draw.line(square1,(0,0,0), [25,100],[20,70],3)
    pygame.draw.line(square1,(0,0,0), [20,70],[20,40],3)
    pygame.draw.line(square1,(0,0,0), [20,40],[5,60],3)
    pygame.draw.line(square1,(0,0,0), [20,40],[35,60],3)
    pygame.draw.line(square1,(0,0,0), [20,20],[30,20],3)
    pygame.draw.circle(square1,(0,0,0), (20,30),10,0)
    pygame.draw.rect(square1, (51,102,0),(10, 10, 15, 14), 0)

    # Человек 2
    pygame.draw.line(square2,(0,0,0), [0,100],[15,100],3)
    pygame.draw.line(square2,(0,0,0), [25,100],[40,100],3)
    pygame.draw.line(square2,(0,0,0), [15,100],[20,70],3)
    pygame.draw.line(square2,(0,0,0), [40,100],[20,70],4)
    pygame.draw.line(square2,(0,0,0), [20,70],[20,40],3)
    pygame.draw.line(square2,(0,0,0), [20,40],[5,60],3)
    pygame.draw.line(square2,(0,0,0), [20,40],[35,60],3)
    pygame.draw.circle(square2,(0,0,0), (20,30),10,0)

    # Самолёт
    pygame.draw.line(aircraft,(0,0,0), [30,40],[150,40],5)
    pygame.draw.line(aircraft,(0,0,0), [150,40],[120,15],5)
    pygame.draw.line(aircraft,(0,0,0), [120,15],[40,15],3)
    pygame.draw.line(aircraft,(0,0,0), [40,15],[30,5],3)
    pygame.draw.line(aircraft,(0,0,0), [30,5],[0,5],3)
    pygame.draw.line(aircraft,(0,0,0), [0,5],[30,40],3)
    pygame.draw.line(aircraft,(0,0,0), [65,25],[65,30],2)
    pygame.draw.line(aircraft,(0,0,0), [65,25],[85,25],2)
    pygame.draw.line(aircraft,(0,0,0), [65,30],[90,30],2)
    pygame.draw.line(aircraft,(0,0,0), [85,25],[90,30],2)
    
    
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(18)
 
