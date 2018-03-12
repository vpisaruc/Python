#Бутолин Александр ИУ7-12
#Сформировать из исходной строки новую строку преобразовав каждое слово:
#далить центральную букву слова, если оно нечётной длины.

from math import *

try:
    s=input('Введите строку: ')
    s+=' а'
    stroka=''
    l=len(s)
    count=0
    s2=''
    i=0
    while i!=l:
        if s[i]!=' ':
            i+=1
        else:
            break
    s2=s[:i]
    print('Первое слово: ',s2)

    k=s.find(s2,i+1,l)
    #print(k)
    if k!=-1:
        s=s[:k+1]+s[i+k:]
    i=0
    s+=' a'
    while i<l:
        if s[i]!=' ':
            count+=1
        else:
            if count%2!=0:
                stroka+=(s[i-count:i-(count//2)-1]+s[i-(count//2):i])
                i-=1
                l-=1
            else:
                stroka+=s[i-count:i]+' '
            count=0
                
        i+=1
    
    print(stroka)
    
except ValueError:
    print('Введено неправильное значение')
        
        
