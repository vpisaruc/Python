#Бутолин ИУ7-12
#Защита матрицы


from math import log

z=list(map(int,input('Введите элементы массива Z в одну строку  : ').split()))
m=int(input('Введите количество строк матрицы F : '))
k=len(z)
s=0.05
y=0.1

f=[0]*m
for i in range (m):
    f[i]=[0]*k



for i in range (m):
    for j in range (k):
        f[i][j]=z[j]*log(y)
    y+=s
sum=[0]*m
print('\nПолученная матрица F: ')
for i in range (m):                    
    for j in range (k):
        print('{:7.3f}'.format(f[i][j]),end=' ')
        sum[i]+=f[i][j]
    print('\n',end='')


a=sum.index(max(sum))
b=sum.index(min(sum))
print('\nМаксимальная сумма элементов = ','{:7.4f}'.format(max(sum)),'Номер строки = ',a+1)
print('Минимальная сумма элементов = ','{:7.4f}'.format(min(sum)), ' Номер строки = ',b+1)


a=sum.index(max(sum))
b=sum.index(min(sum))
w=[0]*(len(z)*2)
print('\nПолученный массив W: ')
for i in range (k):
    w[i]=f[a][i]
    w[i+k]=f[b][i]

for i in range (k*2):
    print('{:7.3f}'.format(w[i]),end=' ')



                             
                
        
        
