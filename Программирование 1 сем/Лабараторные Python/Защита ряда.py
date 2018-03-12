from math import *

n=float(input('Введите значение N: '))
e=float(input('Введите эпсилон: '))
sum=1
m=1
z=1
t=1
while abs(t)>e:
    t=t*((-1)*z/(z+2))
    sum=sum+t
    z+=2
    #print('{:6f}'.format(t)
    m+=1
    if m==n:
        break
ksum=sum*4
print('Cумма ряда = {:5f}'.format(ksum))
    
        
 
