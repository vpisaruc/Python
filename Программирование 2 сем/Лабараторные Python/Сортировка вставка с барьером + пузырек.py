# Бутолин Александр ИУ7-22
# Сортировка вставкой с барьером
# Улучшенный пузырек

from numpy import *
from random import *
import time

try:
    
    mas_1 = array([randint(-500, 500) for i in range(0,1000)])
    mas_2 = array([randint(-500, 500) for i in range(0,100)])
    mas_3 = array([randint(-500, 500) for i in range(0,10)])
    cmas_1 = [mas_1[i] for i in range(len(mas_1))]
    cmas_2 = [mas_2[i] for i in range(len(mas_2))]
    cmas_3 = [mas_3[i] for i in range(len(mas_3))]


    #print('Исходный массив: ')
    #for i in range(len(mas_1)):
        #print(mas_1[i],' ',end='')

    print()
    print('Массив',end='')
    print('        Вставка с барьером',end='   ')
    print('Улучшеный пузырек')
    print('10',end='')
    time.clock()
    for i in range(1,len(mas_1)):
        if mas_1[i - 1] > mas_1[i]:
            mas_1[-1] = mas_1[i]
            j = i - 1
            while mas_1[j] > mas_1[-1]:
                mas_1[j + 1] = mas_1[j]
                j -= 1
            mas_1[j + 1] = mas_1[-1]
    T1 = time.clock()
    print('               ','{:.6f}'.format(T1),end='              ')

    
    time.clock()
    i = -1
    flag = True
    while flag:
        flag = False
        for j in range(len(cmas_1) - i - 2):
            if cmas_1[j] > cmas_1[j + 1]:
                cmas_1[j], cmas_1[j + 1] = cmas_1[j + 1], cmas_1[j]
                flag = True
        i += 1
    T11 = time.clock()
    print('{:.6f}'.format(T11))

    

    print('100',end='')
    time.clock()
    for i in range(1,len(mas_2)):
        if mas_2[i - 1] > mas_2[i]:
            mas_2[-1] = mas_2[i]
            j = i - 1
            while mas_2[j] > mas_2[-1]:
                mas_2[j + 1] = mas_2[j]
                j -= 1
            mas_2[j + 1] = mas_2[-1]
    T2 = time.clock()
    print('              ','{:.6f}'.format(T2),end='              ')

    time.clock()
    i = -1
    flag = True
    while flag:
        flag = False
        for j in range(len(cmas_2) - i - 2):
            if cmas_2[j] > cmas_2[j + 1]:
                cmas_2[j], cmas_2[j + 1] = cmas_2[j + 1], cmas_2[j]
                flag = True
        i += 1
    T22 = time.clock()
    print('{:.6f}'.format(T22))

    print('1000',end='')
    time.clock()
    for i in range(1,len(mas_3)):
        if mas_3[i - 1] > mas_3[i]:
            mas_3[-1] = mas_3[i]
            j = i - 1
            while mas_3[j] > mas_3[-1]:
                mas_3[j + 1] = mas_3[j]
                j -= 1
            mas_3[j + 1] = mas_3[-1]

    T3 = time.clock()
    print('             ','{:.6f}'.format(T3),end='              ')

    time.clock()
    i = -1
    flag = True
    while flag:
        flag = False
        for j in range(len(cmas_3) - i - 2):
            if cmas_3[j] > cmas_3[j + 1]:
                cmas_3[j], cmas_3[j + 1] = cmas_3[j + 1], cmas_3[j]
                flag = True
        i += 1
    T33 = time.clock()
    print('{:.6f}'.format(T33),end=' ')


    
except ValueError:
    print('Неправильный ввод данных')
