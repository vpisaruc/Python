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

# Метод Расчески
clock()
k = i = 0
n = s = len(N)
while n > 1:
    s = s//1.247
    if s < 1:
        s = 1
    k = i = 0
    while i + s < n:
        if N[i] > N[i+s]:
            N[i], N[i+s] = N[i+s], N[i]
            k = i
        i += 1
    if s == 1:
        n = k+1
t = 0
t = clock()
print('Отсортированный массив методом Расчески: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()
