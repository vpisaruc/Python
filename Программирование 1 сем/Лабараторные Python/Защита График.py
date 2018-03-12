from math import *

c1=float(input('Введите начальное значение функции: '))
c2=float(input('Введите конечное значение функции: '))
h=float(input('Введите шаг: '))
n=c1
min=9999999999999
max=-999999999999
while round(n,7)<=c2:
    s=n*n*n+n-1
    if s<min:
        min=s
    if s>max:
        max=s
    n+=h
print()
print('График функции S')
print('              {:3.3f}'.format(min),end='')
print('',' '*50,'{:3.3f}'.format(max))
print('               ','-'*59,end='')
print('+')
while round(c1,7)<=c2:
   s=c1*c1*c1+c1-1
   o=int(round((0-min)/(max-min)*59+1,0))  
   zv=int(round((s-min)/(max-min)*59+1,0))
   r0=(' '*o)+'|'                          
   rz=(' '*zv)+'*'
   if min >0:
       print('{:4.3f}    {}'.format(c1,rz))
   else:    
       if zv<o:
           o=o-zv-1
           r0=((' '*o) + '|')
           if c1<0:
               print('{:10.3f}     {}{}'.format(c1,rz,r0))
           else:
               print('{:10.3f}     {}{}'.format(c1,rz,r0))
       elif zv>o:
           zv=zv-o-1
           rz=((' '*(zv) + '*'))
           if c1<0:    
               print('{:10.3f}      {}{}'.format(c1,r0,rz))
           else:
               print('{:10.3f}     {}{}'.format(c1,r0,rz))
       else:
           print('{:10.3f}     {}'.format(c1,rz))            

   c1+=h
 
    
    
    
        




