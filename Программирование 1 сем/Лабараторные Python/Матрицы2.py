#Бутолин Александр ИУ7-12
#Написать программу вычисления матрицы Z по формуле z=sinf(f)+sqrt(x) 
#Где f задается масивом
#А x изменяется от 1 с шагом 0.1
#Напечатать полученную матрицу
#Затем напечатать вектор Y

from math import *

try:

    Z=[]
    Y=[]
    x=1
    k=0
    n=int(input('Введите количество строк матрицы Z: '))
    m=int(input('Введите количество столбцов матрицы Z: '))
    print('Заполните массив F введя',m*n,'элементов в одну строку через пробел: ')
    F=[0]*(m*n)
    Z=[[0]*m for i in range(n)]
    F=list(map(int,input().split()))


    #Подсчет элементов массива по формуле: Z=sin(f[k]) + Корень из Х
    for i in range(n):
        for j in range(m):
            Z[i][j]=sin(F[k])+sqrt(x)
            x+=0.1
            k+=1

    print('Вывод полученного массива Z:\n ')
    for i in range(n):
        for j in range(m):
            print('{:.4f}'.format(Z[i][j]),' ',end='')
        print()

    #Нахождение положений макисмального и минимального элементов матрицы Z
    min=Z[0][0]
    max=Z[0][0]
    jmin=0
    jmax=0
    for i in range(n):
        for j in range(m):
            if Z[i][j]<min:
                jmin=j
            if Z[i][j]>max:
                jmax=j

    #Определения столбцов для печати
    if jmin==jmax:
        for i in range(n):
                Y.append(Z[i][jmax])
    if jmin!=jmax:
        for i in range(n):
                Y.append(Z[i][jmin])
        for i in range(n):
                Y.append(Z[i][jmax])

    #Печать вектора Y
    print('\nВектор Y:\n')
    l=len(Y)
    for i in range(l):
        print('{:.4f}'.format(Y[i]),'',end='')

except ValueError:
    print('Неправильное значение ')


            
