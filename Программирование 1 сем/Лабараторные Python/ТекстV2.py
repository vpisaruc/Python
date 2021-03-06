#Бутолин Александр ИУ7-12
#Текст


##s=['Привет как дела.',
##  '    Это совершенно бесполезный текст.',
##  'Он не несёт в себе какую-либо 2 + 5 информацию.',
##  ' Я потратил много времени на эту задачу.',
##  'Я Саша Бутолин мне 36 / 2 лет.']

s=['Привет как дела.',
  '    это совершенно бесполезный текст.',
  'Он не несёт в себе какую-либо 2 + 5 информацию.',
  ' Я потратил много времени на эту задачу.',
  '    Я Саша Бутолин мне 36 / 2 лет.']

#Преобразовываем массив строк в матрицу слов
for i in range(len(s)):
    s[i]=s[i].split()

print('Исходный текст:')
print()

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j],' ',end='')
    print()

print()


#Алгоритм нахождения самого большого слова в каждом предложении
dlina_slova=0
max=0
for i in range(len(s)):
    print('Самое длинное слово в предложении',' ',i+1,' - ',end='')
    for j in range(len(s[i])):
            if j+1==len(s[i]):                #Если слово последнее в строке
                dlina_slova=len(s[i][j])-1    #то вычитать из его длины точку
            else:                             #для нахождения точно длины
                dlina_slova=len(s[i][j])
            if dlina_slova>=max:
                max=dlina_slova
                q=s[i][j]
    for z in q:                           #Не выводим точку
        if z!='.':
           print(z,end='')
    print()
    max=0
print()


#Определение количество слов между самым длинным
#И самым коротким словом
min_dlina_slova=len(s[0][0])
max_dlina_slova=len(s[0][0])
imin=jmin=imax=jmax=0
for i in range(len(s)):
    for j in range(len(s[i])):
        if j+1==len(s[i]):
            dlina_slova=len(s[i][j])-1
        else:
            dlina_slova=len(s[i][j])
        if dlina_slova>max_dlina_slova:
            max_dlina_slova=dlina_slova
            imax=i                            #Находим положение самого
            jmax=j                            #длинного слова
        if dlina_slova<min_dlina_slova:
            min_dlina_slova=dlina_slova
            imin=i                            #короткого слова
            jmin=j
print('Самое короткое слово в тексте: ',s[imin][jmin])
print('Самое длинное слово в тексте: ',s[imax][jmax])
count=0

#Подсчёт слов между найденными словами
if imin<imax:
    for i in range(len(s)):
        for j in range(len(s[i])):
            if imin<=i<=imax and jmin<=j<=jmax:
                count+=1
if imin>imax:
    for i in range(len(s)):
        for j in range(len(s[i])):
            if imin>=i>=imax and jmin>=j>=jmax:
                count+=1
print('Количество слов между самыми коротким и длинным словом: ',count)


#Определить слово которое встречается реже всего
a=[]   #Одномерный массив в котором будут храниться слова
b=[]   #Одномерный массив в котором будут храниться количество
       #вхождений каждого слова в тексте

#Заполняем массив а
for i in range(len(s)):
    for j in range(len(s[i])):    
        if s[i][j] not in a:
            a.append(s[i][j])

#Заполняем массив b
b=[0]*len(a)
for k in range(len(a)):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j]==a[k]:
                b[k]+=1

#Проходим по массиву b и находим ячейку в которой
#Будет лежать 1, этой ячейке будет соответсвовать
#ячейка в массива a - это и есть искомое слово
for i in range(len(b)):
    if b[i]==1:
        print('Самое редкое слово в тексте: ',a[i])
        break

print()

# Выражение '*' и '/' заменить на результат.
for i in range(len(s)):
    while j<=len(s[i])-2:
        if s[i][j]=='+':
            s[i][j]=str(int(s[i][j-1])+int(s[i][j+1]))
            del(s[i][j-1])
            del(s[i][j])
        if s[i][j]=='/':
            s[i][j]=str(int(int(s[i][j-1])/int(s[i][j+1])))
            del(s[i][j-1])
            del(s[i][j])
        j+=1
    j=0
        
print('Текст с заменой арифметических выражений:')
print()
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j],' ',end='')
    print()

#Создание массива в котором хранятся количества элементов строк
count=0
max=0
a=[]
for i in range(len(s)):
    for j in range(len(s[i])):
        for k in s[i][j]:
            count+=1
    count+=(len(s[i])-1)*2
    a.append(count)
    if count>max:
        max=count
    count=0
print()
#print(a) #массив в котором содержатся количество символов в строках
print()

#Выравнивание по ширине
print('Выравнивание по ширине:')
print()
for i in range(len(s)):
    if a[i]<max:
        if (max-a[i])%(len(s[i])-1)==0:
            for j in range(len(s[i])):
                print(s[i][j],' '*int((max-a[i])/(len(s[i])-1)+1),end='')
            print()
        else:
            for j in range((max-a[i])%(len(s[i])-1)):
                print(s[i][j],' '*int((max-a[i])/(len(s[i])-1)+2),end='')
            for j in range(((max-a[i])%(len(s[i])-1)),len(s[i])):
                print(s[i][j],' '*int((max-a[i])/(len(s[i])-1)+1),end='')
            print()
    else:
        for j in range(len(s[i])):
            print(s[i][j],' ',end='')
        print()


print()
#Выравнивание по правому краю
print('Выравнивание по правому краю:')
print()
for i in range(len(s)):
    if a[i]<max:
        print(' '*(max-a[i]),end='')
        for j in range(len(s[i])):
            print(s[i][j],' ',end='')
        print()
    else:
        for j in range(len(s[i])):
            print(s[i][j],' ',end='')
        print()
        
       
#Замена одного слова в указаном предложении.
print()
count=0
inomer=jnomer=iknomer=jknomer=0
nomer=int(input('Введите номер предложения в котором хотите заменить слово: '))
slovo=(input('Введите слово которое хотите заменить: '))
slovo1=slovo+'.'
zamena=(input('Введите новое слово: '))
zamena1=zamena+'.'
for i in range(len(s)):
    if b==1:
        break
    jnomer=0
    for j in range(len(s[i])):
        for k in s[i][j]:
            if k=='.':
                count+=1
                if count==nomer-1:
                    if j==len(s[i])-1:
                        inomer=i+1
                        jnomer=0
                    else:
                        inomer=i
                        jnomer+=1
                    b=1
                    break
                    
#print(inomer)
#print(jnomer)


count=0
for i in range(len(s)):
    for j in range(len(s[i])):
        for k in s[i][j]:
            if k=='.':
                count+=1
                if count==nomer:
                    iknomer=i
                    jknomer=j

#print(iknomer)
#print(jknomer)


for i in range(inomer,iknomer+1):
    for j in range(jnomer,jknomer+1):
        if s[i][j]==slovo:
            s[i][j]=zamena
        if s[i][j]==slovo1:
            s[i][j]=zamena1

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j],' ',end='')
    print()

print()
#Удалить из каждой нечётной строки текста заданное слово
slovo=input('Введите слово которое хотите удалить: ')
slovo1=slovo+'.'
print()
j=0
for i in range(len(s)):
    if i%2==0 or i==0:
        while j<=len(s[i])-1:
            if s[i][j]==slovo:
                del(s[i][j])
            if s[i][j]==slovo1:
                del(s[i][j])
                s[i][j-1]+='.'
            j+=1
        j=0

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j],' ',end='')
    print()
                
            
    
        
        





            

