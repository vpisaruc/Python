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

# Улучшенный пузырек
clock()
i = -1
flag = True
while flag:
    flag = False
    for j in range(len(N) - i - 2):
        if N[j] > N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]
            flag = True
    i += 1
t = clock()
print('Отсортированный массив Улучшенный пузырек: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()
