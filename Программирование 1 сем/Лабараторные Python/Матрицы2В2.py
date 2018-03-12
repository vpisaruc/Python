#Бутолин Александр ИУ7-12
#Написать программу вычисления матрицы Z по формуле z=sinf(f)+sqrt(x) 
#Где f задается масивом
#А x изменяется от 1 с шагом 0.1
#Напечатать полученную матрицу
#Затем напечатать вектор Y

from math import *
try:

    Z=[]
    n=int(input('Введите количество строк матрицы Z: '))
    m=int(input('Введите количество столбцов матрицы Z: '))
    F=[0]*n
    X=[0]*m
    X[0]=1
    jmin=0
    jmax=0
    Y=[]
    Z=[[0]*m for k in range(n)]
    print('Введите массив F по одному элементу в строку:')
    for k in range (n):
        F[k]=int(input())

    print('Введеный вектор F :')
    for k in range (n):
        print(F[k],' ',end='')


    #Формирование одномерного массива X
    for j in range(1,m):
        X[j]=X[j-1]+0.1

    #Подсчет элементов матрицы Z
    for k in range (n):
        for j in range(m):
            Z[k][j]=sin(F[k])+sqrt(X[j])

    #Вывод матрицы Z
    print('\nМатрица Z:')
    for k in range(n):
        for j in range(m):
            print('{:.3f}'.format(Z[k][j]),' ',end='')
        print()

    #Определение столбца минимального и максимального значения матрицы Z
    max=Z[0][0]
    min=Z[0][0]
    for k in range(n):
        for j in range(m):
            if Z[k][j]>max:
                max=Z[k][j]
                jmax=j
            if Z[k][j]<min:
                jmin=j
                min=Z[k][j]

    print('\nmax =','{:.3f}'.format(max),'столбец',jmax+1)
    print('min =','{:.3f}'.format(min),'столбец',jmin+1)

    #Формирование вектора Y
    if jmax==jmin:
        for k in range(n):
            Y.append(Z[k][jmin])
    else:
        for k in range(n):
            Y.append(Z[k][jmin])
        for k in range(n):
            Y.append(Z[k][jmax])

    #Вывод вектора Y
    print('\nВектор Y:\n')
    l=len(Y)
    for i in range(l):
        print('{:.3f}'.format(Y[i]),'',end='')

    
    
except ValueError:
    print('Неправильное значение ')
