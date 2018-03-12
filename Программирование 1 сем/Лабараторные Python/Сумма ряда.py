
# Бутолин Александр ИУ7-12
# Посчитать сумму ряда

from math import *

try:


    x=float(input('Ведите значение X: '))
    if abs(x)>1:
        print('Неправильное значение X')
    else:
        e=float(input('Введите значение эпсилон: '))
        n=int(input('Введите начальное значение для вывода: '))
        if n<=0:
            print('Неправильное начальное значение: ')
        else:
            h=int(input('Введите шаг вывода результатов: '))
            if h<=0:
                print('Неправильное значение шага вывода результатов: ')
            else:
                max=int(input('Максимальн итераций: '))
                if max<=0:
                    print('Неправильное значение итерации: ')
                else:
                    z=1
                    sum=x
                    t=x
                    k=2
                    print('  k\t  t\t   sum')
                    if n==1:
                        print('  1','\t',x,'\t  ',x)
                    while abs(t)>e:
                        t=t*(-(x**2)*(z)/(z+2))
                        sum+=t
                        if ((k==n) or (k>n and (k-n)%h==0)) and k<max:
                            print('{:3d}'.format(k),'{:10.5f}'.format(t),'  {:7f}'.format(sum))
                        k+=1
                        z+=2
                    if k>=max :
                        print('Ряд не сошелся ')
                    else:
                        print('При X = ',x,'C точностью = ',e,'Cумма ряда = {:7f}\n'.format(sum),'Число просуммированных членов = ',k-1)                 
                        
except ValueError:
    print('Неправильное значение')

                        
                        
                        
                    
                
              
                  
          
