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

# Простой выбор

clock()
for i in range(0,len(N) - 1):
    for j in range(i+1, len(N)):
        if N[i] > N[j]:
            N[i], N[j] = N[j], N[i]
t = clock()
print('Отсортированный массив Простым выбором: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()
