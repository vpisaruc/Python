from math import *

a=float(input('Введите начальное значение функции: '))
c=float(input('Введите конечное значение функции: '))
h=float(input('Введите шаг: '))
n=a
maxzv=-999999999999999
min=9999999999999
max=-999999999999
while round(n,7)<=c:
    z=sin(n)
    if min>z:
        min=z
    if max<z:
        max=z
    n+=h


print('{:.5f}'.format(min),end='')
print(' '*50,'{:.5f}'.format(max))
print(' ','-'*59,end='')
print('+')
while round(a,7)<=c:
   z=sin(a)
   o=int(round((0-min)/(max-min)*59+1,0))  
   zv=int(round((z-min)/(max-min)*59+1,0))
   maxzv=int(round((max-min)/(max-min)*59+1,0))
   r0=(' '*o)+'|'                          
   rz=(' '*zv)+'*'                           
   if min >0:
       print('{}    {:9.3f}'.format(rz,a))
   else:    
       if zv<o:
           o=o-zv-1
           r0=((' '*o) + '|')
           if a<0:
               print(' {}{}'.format(rz,r0),' '*((maxzv-30)+5),'{:9.3f}'.format(a))
           else:
               print(' {}{}'.format(rz,r0),' '*((maxzv-30)+5),'{:9.3f}'.format(a))
       elif zv>o:
           zv=zv-o-1
           rz=((' '*(zv) + '*'))
           if a<0:    
               print(' {}{}'.format(r0,rz),' '*((maxzv-zv-30)+4),'{:9.3f}'.format(a))
           else:
               print(' {}{}'.format(r0,rz),' '*((maxzv-zv-30)+4),'{:9.3f}'.format(a))
       else:
           print(' {}'.format(rz),' '*((maxzv-30)+5),'{:9.3f}'.format(a))
                  
   a+=h
 
    
    
    
        






























