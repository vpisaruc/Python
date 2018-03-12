try:
    x=int(input('Введите значение X: '))
    a=int(input('Введите значение A: '))
    b=a*x 
    y1=-(x**6+a**6)+b*(x**4+a**4)-b**2*(x**2+a**2)+b**3
    y2=-x**6+a*x**5-a**2*x**4+a**3*x**3-a**4*x**2+a**5*x-a**6
    print(y1)
    print(y2)
    input('Нажмите ENTER')
except ValueError:
    print('Неподходящиее значение ')
