#Бутолин Александр ИУ7-12
#решить систему при разных значения a,b,x
#ctg(ab)-e**2
#1/pow(0.93*pi**2*sin(x),1/5)
from math import *

try:

    a=float(input('Введите коэффициент а:'))
    b=float(input('Введите коэффициент b:'))
    x=float(input('Введите коэффициент x:'))

    s=cos(a*b)/sin(a*b)
    if s>0:
        y=s-e*e
    else:
        y=1/pow(0.93*pi*pi*sin(x),1/5)

    print('{:6.5f}'.format(y))

except ValueError:
        print('Неправильное значение')
