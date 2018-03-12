# Бутолин Александр ИУ7-22
# Комбинированный метод уточнения корней

from math import *
import matplotlib.pyplot as plt
import time
import numpy as np

try:

    def func(k): # Значение функции
        return(sin(k) * k)

    def der(k): # Первая производная
        return(cos(k) * k + sin(k))

    def second_der(k): # Вторая производная
        return(cos(k) + (-1 * sin(k)) * k + cos(k) )

    def tangent(k): # Касательная
        k = k - (func(k) / der(k))
        return(k)

    def chord(k, q): # Хорда
        k = k - func(k)*((k - q) / (func(k) - func(q)))
        return(k)

    a = float(input('Введите начало отрезка: '))
    b = float(input('Введите конец отрезка: '))
    h = float(input('Введите шаг программы: '))
    e1 = float(input('Введите точность по аргументу функции: '))
    e2 = float(input('Введите точность по аргументу функции: '))
    max_iteration = float(input('Введите максимальное количество итераций: '))
    mas_x = []
    mas_y = []
    
    time.clock()
    
    int_part = int(abs(b - a) // h) # Количество целых интервалов
    N = 0 # Номер корня
    iteration = 0 # Количество итераций

    print('№-корня         Xn..Xn+1           X            F(X)     iteration   Error') # Шапка

    for i in range(int_part):
        iteration = 1
        h1 = a + h * i
        h2 = a + h * (i + 1)
        flag = False
        if func(h1) * func(h2) < 0:
            z1 = h1
            z2 = h2
            while abs(z1 - z2) > e1 and iteration < max_iteration:
                iteration += 1
                #print('z1,z2','{:12.7f}'.format(z1),'{:12.7f}'.format(z2))
                if func(z1) * second_der(z1) < 0: # Метод смешанный улучшенный
                    z1 = chord(z1,z2)
                elif func(z1) * second_der(z1) > 0:
                        z1 = tangent(z1)
                if func(z2) * second_der(z2) < 0:
                    z2 = chord(z2,z1)
                elif func(z2) * second_der(z2) > 0:
                        z2 = tangent(h2)
                #print('z1,z2','{:12.7f}'.format(z1),'{:12.7f}'.format(z2))
                if z1 < h1 or z1 > h2 or z2 < h1 or z2 > h2:
                    N += 1
                    print(N,end='           ')
                    print('{:5.2f}'.format(h1),'.','{:5.2f}'.format(h2),end='        ')
                    print(' --- ',end='         ')
                    print(' --- ',end='       ')
                    print(' --- ',end='       ')
                    print('2')
                    flag = True
                    break
            if flag == False:
                x = (z1 + z2) / 2
                N += 1
                print(N,end='           ')
                print('{:5.2f}'.format(h1),'.','{:5.2f}'.format(h2),end='')
                if iteration >= max_iteration:
                    print('      ',end=' ')
                    print(' --- ',end='         ')
                    print(' --- ',end='       ')
                    print(' --- ',end='       ')
                    print('1')
                else:
                    print('{:15.6f}'.format(x),end='')
                    mas_x.append(x)
                    print('{:15.6e}'.format(func(x)),end='      ')
                    mas_y.append(func(x))
                    print(iteration,end='         ')
                    print('0')
                
        elif func(h1) == 0:
            x = h1
            N += 1
            print(N,end='           ')
            print('{:5.2f}'.format(h1),'.','{:5.2f}'.format(h2),end='')
            print('{:15.6f}'.format(x),end='')
            mas_x.append(x)
            print('{:15.6e}'.format(func(x)),end='      ')
            mas_y.append(func(x))
            print('1',end='         ')
            print('0')

    iteration = 1
    flag = False
    if func(h2) * func(b) < 0:
        z1 = h2
        z2 = b
        while abs(z1 - z2) > e1 and iteration < max_iteration:
            iteration += 1
            #print('z1,z2','{:12.7f}'.format(z1),'{:12.7f}'.format(z2))
            if func(z1) * second_der(z1) < 0: # Метод смешанный улучшенный
                z1 = chord(z1,z2)
            elif func(z1) * second_der(z1) > 0:
                z1 = tangent(z1)
            if func(z2) * second_der(z2) < 0:
                z2 = chord(z2,z1)
            elif func(z2) * second_der(z2) > 0:
                z2 = tangent(h2)
                #print('z1,z2','{:12.7f}'.format(z1),'{:12.7f}'.format(z2))
                if z1 < h2 or z1 > b or z2 < h2 or z2 > b:
                    N += 1
                    print(N,end='           ')
                    print('{:5.2f}'.format(h2),'.','{:5.2f}'.format(b),end='        ')
                    print(' --- ',end='          ')
                    print(' --- ',end='       ')
                    print(' --- ',end='       ')
                    print('2')
                    flag = True
                    break
        if flag == False:
            x = (z1 + z2) / 2
            N += 1
            print(N,end='           ')
            print('{:5.2f}'.format(h2),'.','{:5.2f}'.format(b),end='')
            if iteration >= max_iteration:
                print('      ',end=' ')
                print(' --- ',end='         ')
                print(' --- ',end='       ')
                print(' --- ',end='       ')
                print('1')
            else:
                print('{:15.6f}'.format(x),end='')
                mas_x.append(x)
                print('{:15.6e}'.format(func(x)),end='      ')
                mas_y.append(func(x))
                print(iteration,end='         ')
            
    elif func(h2) == 0:
        x = h1
        N += 1
        print(N,end='           ')
        print('{:5.2f}'.format(h2),'.','{:5.2f}'.foramt(b),end='')
        print('{:15.6f}'.format(x),end='')
        mas_x.append(x)
        print('{:15.6e}'.format(func(x)),end='      ')
        mas_y.append(func(x))
        print('1',end='         ')
        print('0')


    print('\n')
    print('Errors: 0 - Ошибки отсутсвуют')
    print('        1 - Превышено максимальное чисто итераций')
    print('        2 - На данном отрезке находится экстремум') 
    print()
    print('        Время выполнения: ','{:.5f}'.format(time.clock()),'секунд')
    
    # Построение графика
    X = []
    Y = []
    i = a
    while i<= b:
        X.append(i)
        Y.append(func(i))
        i += e1
    plt.plot(X,Y)
    

    # Корни уравнения при f(x) = 0
    for i in range(len(mas_x)):
        if i == 0:
            plt.scatter(mas_x[i],mas_y[i],s = 100, c = 'r', label = 'points')
        else:
            plt.scatter(mas_x[i],mas_y[i],s = 100, c = 'r')

    # Макс, мин, экстремумы, точки перегиба
    min = a
    max = a
    i = a
    E = []
    P = []

    q1 = i
    q2 = i + e1
    if func(q1) < func(q2):
        flag = True
    if func(q1) > func(q2):
        flag = False
    i += e1

    while(i) <= b:
        q1 = i
        q2 = i + e1
        if (flag == False) and (func(q1) < func(q2)):
            flag = True
            E.append((q1+q2)/2)
        if (flag == True) and (func(q1) > func(q2)):
            flag = False
            E.append((q1 + q2)/2)
        i += e1
    
    
    i = a
    while(i) <= b:
        #if der(i) <= 0.005 and der(i) >= -0.005:
            #E.append(i)
        if second_der(i) <= 0.005 and second_der(i) >= -0.005:
            P.append(i)
        if func(i) > func(max):
            max = i
        if func(i) < func(min):
            min = i
        i += e1
        i = round(i,6)
    plt.scatter(max, func(max),s = 200, c ='k',label = 'Max')
    plt.scatter(min, func(min),s = 200, c ='w',label = 'Min')
    for i in range(len(E)):
        if i == 0:
            plt.scatter(E[i],func(E[i]), s = 30, c ='g',label = 'extremum')
        else:
            plt.scatter(E[i],func(E[i]), s = 30, c ='g')
    for i in range(len(P)):
        if i == 0:
            plt.scatter(P[i],func(P[i]), s = 30, c ='y',label = 'inflaction')
        else:
            plt.scatter(P[i],func(P[i]), s = 30, c ='y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    #plt.axis('equal')
    plt.show()
    
except ValueError:
    print('Неправильный ввод')
