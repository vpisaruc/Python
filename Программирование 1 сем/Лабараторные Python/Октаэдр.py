# Бутолин Александр ИУ7-12
# Вывести Объем,Площадь, Радиус вписанной и описанной сферы правильного октаэдра.
from math import sqrt


try:
    a=float(input('Введите длину ребра: '))
    if a < 0:
        raise Exception('Отрицательная грань')
    if abs(a) == 0:
        raise Exception('Сторона равна нулю')
    s=2*a**2*sqrt(3)
    v=1/3*sqrt(2)*a**3
    ro=a/2*sqrt(2)
    rv=a/6*sqrt(6)
    print('Площадь = {:6.5f}'.format(s))
    print('Объем = {:6.5f}'.format(v))
    print('Радиус описанной = {:6.5f}'.format(ro))
    print('Радиус вписанной = {:6.5f}'.format(rv))
except ValueError:
    print('Неправильное значение')
except Exception as ex:
    print(ex)
