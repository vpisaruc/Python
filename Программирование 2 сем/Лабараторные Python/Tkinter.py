# Бутолин Александер ИУ7-22
# Задано множество окружностей.
# Определить ту, которая пересекает больше всего окружностей.

from math import sqrt
from tkinter import *


try:

    def distance(x1,y1,x2,y2):
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def pifagor(r):
        return (sqrt((2*r)**2 + (2*r)**2))/2

##    r = [0, 0, 0, 0, 0] # Радиусы
##    x = [0, 0, 0, 0, 0] # Координаты центра по оси абцис
##    y = [0, 0, 0, 0, 0] # Коорждинаты центра по оси оординат
##    I = [0] * len(r) # Intersections(пересечения)

##    r = [3, 2, 2, 1, 1] # Радиусы
##    x = [5, 5, 8, 9, 10] # Координаты центра по оси абцис
##    y = [4, 4, 4, 6, 1] # Коорждинаты центра по оси оординат
##    I = [0] * len(r) # Intersections(пересечения)

##    r = [2, 3, 4, 5, 6] # Радиусы
##    x = [3, 3, 3, 3, 3] # Координаты центра по оси абцис
##    y = [3, 3, 3, 3, 3] # Коорждинаты центра по оси оординат
##    I = [0] * len(r)  # Intersections(пересечения)

##    r = [2, 2, 2] # Радиусы
##    x = [0, 2, 3] # Координаты центра по оси абцис
##    y = [0, 2, 0] # Коорждинаты центра по оси оординат
##    I = [0] * len(r)  # Intersections(пересечения)

    x = []
    y = []
    r = []

    n = int(input(('Введите количество окружностей: ')))

    for i in range(n):
        z = float(input('Введите кооридану Х центра окружности: '))
        x.append(z)
        z = float(input('Введите кооридану Y центра окружности: '))
        y.append(z)
        z = float(input('Введите радиус окружности: '))
        r.append(z)
        
    I = len(r)*[0]
    
    for i in range(len(r)-1):
        for j in range(i+1,len(r)):
            if (distance(x[i],y[i],x[j],y[j]) <= (r[i] + r[j])) and (distance(x[i],y[i],x[j],y[j]) >= abs(r[i] - r [j])): #and ((x[i] != x[j]) and (y[i] != y[j])):    
                I[i] += 1
                I[j] += 1

    print('Intersections = ',I)
    root=Tk()            

    max = I[0]
    for i in range(len(I)):
        if I[i] > max:
            max = I[i]
    
    canv = Canvas(root,width = 500, height = 500, bg = "white", cursor = "pencil")
    for i in range(len(r)):
        if I[i] == max:
            canv.create_oval([100 + (x[i] - r[i])*30,100 + (y[i] - r[i])*30],[100 + (x[i] + r[i])*30, 100 + (y[i] + r[i])*30], outline='red')   
        else:
            canv.create_oval([100 + (x[i] - r[i])*30,100 + (y[i] - r[i])*30],[100 + (x[i] + r[i])*30, 100 + (y[i] + r[i])*30], outline='black')
    canv.pack()
    root.mainloop()        


except ValueError:
    print('Неправильный ввод')
