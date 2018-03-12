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

# Сортировка вставками

clock()
for i in range(1,len(N)):
    j = i - 1
    while j >= 0 and N[j] > N[j+1]:
        N[j], N[j+1] = N[j+1], N[j]
        j -= 1
t = clock()
print('Отсортированный массив Вставками: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()
