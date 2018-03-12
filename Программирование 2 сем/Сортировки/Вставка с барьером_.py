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

# Вставка с барьером
clock()
b = N[0]
for i in range (2, len(N)):
    if N[i-1] > N[i]:
        N[0] = N[i]
        j = i - 1
        while N[j] > N[0]:
            N[j+1] = N[j]
            j -= 1
        N[j+1] = N[0]
N[0] = b
i = 1
while (N[i] < b):
    N[i-1] = N[i]
    i += 1
    if i == (len(N)):
            break
N[i-1] = b
t = clock()
print('Отсортированный массив методом Вставки с барьером: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()
