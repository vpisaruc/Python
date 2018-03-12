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


# Шейкер
clock()

k = ub = len(N)-1
lb = 1
while (lb < ub):
    for j in range (ub, lb-1, -1):
        if N[j-1] > N[j]: 
            N[j-1], N[j] = N[j], N[j-1]
            k = j
        lb = k
    for j in range (lb, ub+1):
        if N[j-1] > N[j]:
            N[j-1], N[j] = N[j], N[j-1]
            k = j
        ub = k
t = clock()
print('Отсортированный массив Шейкер: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()
