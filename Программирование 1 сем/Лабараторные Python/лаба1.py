try:
    a1,b1,a2,b2=map(int(input('Введите коэффиценты: ').split('')))
    print('X равен: ')
    print('Y равен: ')
except ValueError:
    print('Неправильное значение')
    
