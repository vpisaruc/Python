#Бутолин Александр ИУ7-12
#Из целого числа выделить цифры и сформировать из них массив

try:

    x=int(input('Введите число: '))

    q=z=abs(x)
    k=0
    mas=[]

    #Определение количества цифр в числе
    while q>0:
        q//=10
        k+=1
    #print(k)

    #Заполнение массива цифрами числа
    for i in range(k):
        mas.append(z%10)
        z//=10
    mas.reverse()

    #Вывод полученного массива
    for i in range(k):
        print(mas[i],end=' ')

except ValueError:
    print('Введены неправильные значения')
