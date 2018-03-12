#Бутолин Александр ИУ7-12
#Задана матрица, вычеркнуть строку с максимальным элементом
#В каждой строке подсчитать колечество элементов превысшающих
#Средне арифметическое в этой строке.
#Разместить эти количества в массиве K
imax=-1
T=[]
K=list()
sum=0
l=-1
q=0
k=0 #Количество чисел в строке больше средне арифметического этой строки
n=int(input('Введите количество строк матрицы: '))
if n==1:
    print('Количество строк матрицы равно 1, матрица L и вектор K пусты')
else:
    m=int(input('Введите количество столбцов матрицы: '))
    T=[[0]*m for i in range(n)]
    print('Введити элементы матрицы по 1 числу в строке')
    for i in range(n):
        for j in range(m):
            T[i][j]=float(input())

    
    print('\nВведеная матрица: ')
    for i in range(n):
        for j in range(m):
            print('{:5f}'.format(T[i][j]),' ',end='')
        print()

    #Нахождение максимального элемента в матрице и номера его строки
    max=T[0][0]
    for i in range(n):
        for j in range(m):
            if T[i][j]>max:
                max=T[i][j]
                imax=i
    print()

    print('max=',max)
    

    #Удаление строки содержащей максимальный эллемент 
    del(T[imax])
    

    #Подсчет средне арифметического строки и заполнение вектора K
    for i in range(n-1):
        k=0
        sum=0
        for j in range(m):
            sum=sum+T[i][j]
        sa=sum/m
        for j in range(m):
            if T[i][j]>sa:
                k+=1
        K.append(k)

    l=len(K)


    print('\nПреобразованная матрица ')
    for i in range(n-1):
        for j in range(m):
            print('{:7.3f}'.format(T[i][j]),' ',end='')
        print()
    print()

    print('Вектор K ')
    for i in range(l):
        print(K[i],' ',end='')


    












        





