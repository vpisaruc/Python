#Бутолин Александр ИУ7-12
#Сформировать из исходной строки новую строку преобразовав каждое слово:
#Удалить центральную букву слова, если оно нечётной длины.

from math import *

try:

    s3=s2=''
    kolp=kol=0
    k=0
    #s=input('Введите строку: ')
    s='Привет как дела я ковбой'
    while k!=len(s):
        if s[k]!=' ':
            kol+=1
            kolp+=1
        else:
            if kol%2!=0:
                s=s[:(kolp-kol)+(kol-kol//2)]+s[(kolp-kol)+((kol-kol//2)+1):]+' '
                k-=1
            else:
                kol=0
        k+=1
    print(s)
            
            
    
except ValueError:
    print('Введено неправильное значение')
        
        
        

