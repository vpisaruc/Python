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

# Шелл
clock()
t = int(len(N)/2)
while t > 0:
    for i in range(len(N)-t):
        j = i
        while j >= 0 and N[j] > N[j+t]:
            N[j], N[j+t] = N[j+t], N[j]
            j -= 1
    t = int(t/2)
t = clock()
print('Отсортированный массив Шелл: ')
for i in range (len(N)):
    print(N[i],end = ' ')
print()
print('Время выполнения: ',t)
print()

