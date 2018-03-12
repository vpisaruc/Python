#Бутолин Александр ИУ7-12
#Метод парабол для заданного количества разбиений

from math import *

try:
    def f(y):
        return y*y
    
    a,b=map(float,input('Введите интервал для подсчёта интеграла: ').split())
    n=int(input('Введите количество разбиений n: '))
    if n%2==0:
        h=(b-a)/n
        s1=s2=0
        for i in range (n):
            if i!=0 and i!=n:
                if i%2!= 0:
                    x=a+i*h
                    s1+=f(x)
                else:
                    x=a+i*h
                    s2+=f(x)
        sum1=h/3*(4*s1+2*s2+f(a)+ f(b))
        print('Значение интеграла для',n,'разбиений =',sum1)
    else:
        print('Количество разбиений должно быть кратно двум')

        
except ValueError:
    print('Введено неправильное значение')
