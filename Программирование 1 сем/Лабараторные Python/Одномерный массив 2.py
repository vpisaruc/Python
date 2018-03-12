#Бутолин Александр ИУ7-12
#Определить и напечатать что больше:
#сумма положительных чисел или модуль суммы отрицательных чисел массива

try:

    sumo=0
    sump=0
    mas=list(map(int,input('Введите элементы массива через пробел: ').split()))
    #print(mas)
    l=len(mas)
    k=True

    #Определение совпадения знаков чисел в массиве
    if mas[0]>0:
        for i in range (1,l):
            if mas[i]<0:
                k=False
    if mas[0]<0:
        for i in range (1,l):
            if mas[i]>0:
                k=False
    if k==True:
        print('Все числа имеют одинаковый знак')
    else:
        #Подсчет суммы чисел разных знаков
        for i in range(l):
            if mas[i]<0:
                sumo=sumo+mas[i]
            if mas[i]>0:
                sump=sump+mas[i]
        if abs(sumo)>sump:
            print('Модуль суммы отрицательных чисел больше суммы положительных чисел ')
        elif abs(sumo)<sump:
            print('Сумма положительных числе больше суммы модуля отрицательных чисел ')
        else:
            print('Cумма положительных чисел равна сумме модуля отрицательных чисел')
      
except ValueError:
    print('Введены неправильные значения')


    
