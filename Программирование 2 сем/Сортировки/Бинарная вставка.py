import numpy as np
import random as rn
from time import clock,time

N = np.array([rn.randint(-10,10) for i in range (10)])
N1 = np.array([rn.randint(-100,100) for i in range (100)])
N2 = np.array([rn.randint(-1000,1000) for i in range (1000)])


print('Исходный массив: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print()
print()

# Бинарная вставка
clock()
for i in range(1, len(N)):
    while i > 0 and N[i] < N[i-1]:
        N[i], N[i-1] = N[i-1], N[i]
        i -= 1
t = 0 
t = clock()
print('Отсортированный массив Бинарной вставкой: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()
