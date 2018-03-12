# Бутолин Александр ИУ7-12
# Вычислить таблицу значений функции.Построить график одной из функций.

from math import *

try:

    t=float(input('Введите начальное значение: '))
    h=float(input('Введите шаг выполнения программы: '))
    k=float(input('Введите конечное значение: '))
    print('      x\t\t\t      R1\t\t    R2')
    n=t
    min=999999999999
    max=-999999999999
    kz=0 
    #Вывод таблицы
    while round(n,7)<=k:
        r1=n**2-cos(pi*n)
        r2=-14.5*n**2+60.69*n-70.9+n**3
        if r1<=min:
            min=r1
        if r1>=max:
            max=r1
        if -0.4<=r1<=0.6:
            kz+=1
        print('{:10.5f}'.format(n),'\t\t{:10.5f}'\
              .format(r1),'\t\t{:10.5f}'.format(r2))
        n+=h
         
    # Кол-во значений функцици попавших в диапазон
    print('\nКол-во значений R1 попавших в диапазон [-0.4,0.6] = ',kz,'\n')

    
    #Вывод шапки графика
    print('График функции R1\n')
    print('         {:.5f}'.format(min),end='')
    print(' '*(54),'{:.5f}'.format(max))
    print('              -',end='')
    print('-'*(58),end='')
    print('+')
    
    # Вывод  графика
    while round(t,7)<=k:
        r1=t**2-cos(pi*t)
        o=int(round((0-min)/(max-min)*59+1,0))  #Количество пробелов до нулевой линии
        z=int(round((r1-min)/(max-min)*59+1,0)) #Количество пробелов до звездочки
        r0=(' '*o)+'|'                          #Строка которая будет выводитсья до нулевой линии
        rz=(' '*z)+'*'                          #Строка которая будет выводиться до звездочек
        if min >0:
           print('{:9.3f}    {}'.format(t,rz))
        else:    
            if z<o:
                o=o-z-1
                r0=((' '*o) + '|')
                if t<0:
                    print('{:9.3f}    {}{}'.format(t,rz,r0))
                else:
                    print('{:9.3f}    {}{}'.format(t,rz,r0))
            elif z>o:
                z=z-o-1
                rz=((' '*z) + '*')
                if t<0:    
                    print('{:9.3f}    {}{}'.format(t,r0,rz))
                else:
                    print('{:9.3f}    {}{}'.format(t,r0,rz))
            else:
                 print('{:9.3f}    {}'.format(t,rz))
                  
        t+=h

except ValueError:
    print('Неправильное значение ')
