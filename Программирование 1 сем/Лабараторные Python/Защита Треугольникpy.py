from math import (sqrt,sin,cos)

try:

    x1=int(input('Введите координату 1 веришны по оси OX: '))
    y1=int(input('Введите координату 1 веришны по оси OY: '))
    x2=int(input('Введите координату 2 веришны по оси OX: '))
    y2=int(input('Введите координату 2 веришны по оси OY: '))
    x3=int(input('Введите координату 3 веришны по оси OX: '))
    y3=int(input('Введите координату 3 веришны по оси OY: '))

    if x1==x2==x3==y1==y2==y3:
        print('Введена точка')
    else:

        st12=sqrt((x2-x1)**2+(y2-y1)**2)
        st23=sqrt((x3-x2)**2+(y3-y2)**2)
        st31=sqrt((x1-x3)**2+(y1-y3)**2)


        m=st12
        if st23>=m:
             m=st23
        if st31>=m:
             m=st31

        kos123=(st12**2+st23**2-st31**2)/(2*st12*st23)
        kos231=(st31**2+st23**2-st12**2)/(2*st31*st23)
        kos312=(st12**2+st31**2-st23**2)/(2*st12*st31)

        if abs(kos123)==1 or abs(kos231)==1 or abs(kos312)==1:
              print('Введена прямая: ')

        sin123=sqrt(1-kos123**2)
        sin231=sqrt(1-kos231**2)
        sin312=sqrt(1-kos312**2)

        if m==st12:
            visota=sin123*st23
            print('Высота проведенная из наибольшего угла: ''{:.5f}'.format(visota))
        elif m==st23:
            visota=st12*sin123
            print('Наибольшая высота треугольника: ''{:.5f}'.format(visota))
        else :
            visota=st12*sin312
            print('Наибольшая высота треугольника: ''{:.5f}'.format(visota))

except ValueError:
    print('Введено неправильное значение ')

    
    
