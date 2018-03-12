#Бутолин Александр ИУ7-22
#Работа с файлами. Создание меню.

try:
    #Шапка меню
    print('0 - Выход ')
    print('1 - Создание файла ')
    print('2 - Добавление записей в файл ')
    print('3 - Поиск ')
    print('4 - Вывести данные ')
    

    #Проверка на корректность ввода
    print()
    Znak_Menu = input('Выберите пункт меню: ')
    while Znak_Menu != '0':
        while Znak_Menu != '1' and Znak_Menu != '2' and Znak_Menu != '3' and Znak_Menu != '4' and Znak_Menu != '0':
            print('Введен неправильный пункт меню')
            Znak_Menu = input('Выберите пункт меню: ')

        #Создание файла
        if Znak_Menu == '1':
            New_File = input('Введите название нового файла и его расширение: ')
            file = open(New_File,'w')
            file.close()
            Znak_Menu = input('Выберите пункт меню: ')


        #Добавление записей в файл
        if Znak_Menu == '2':
            New_File = input('Введите название файла и его расширение в который хотите добавить данные: ')
            file = open(New_File,'a')
            Marka = input('Введите название Марку машины: ')
            Strana = input('Введите название страны производителя: ')
            file.write(Marka)
            file.write(' ')
            file.write(Strana)
            file.write('\n')
            file.close()
            Znak_Menu = input('Выберите пункт меню: ')

        #Поиск по файлу
        if Znak_Menu == '3':
            New_File = input('Введите название файла и его расширение в котором хотите совершиь поиск: ')
            Poisk = input('Введите ключевое слово для поиска: ')
            file = open(New_File,'r')
            Find = input('Введите название файла и его расширение в который будут сохранены результаты поиска: ')
            Findfile = open(Find,'a')
            spisok = [line for line in file]
            for i in range(len(spisok)):
                spisok[i]=spisok[i].split()
            for i in range(len(spisok)):
                for j in range(len(spisok[i])):
                    if spisok[i][j] == Poisk:
                        if j == 1:
                            Findfile.write(spisok[i][j-1])
                            Findfile.write(' ')
                            Findfile.write(spisok[i][j])
                            Findfile.write('\n')
                        if j == 0:
                            Findfile.write(spisok[i][j])
                            Findfile.write(' ')
                            Findfile.write(spisok[i][j+1])
                            Findfile.write('\n')
                        
            file.close()
            Findfile.close()
            Znak_Menu = input('Введите пункт меню: ')

        #Вывод содержимого файла
        if Znak_Menu == '4':
            New_File = input('Введите название файла и его расширение содержимое которого хотите вывести на экран: ')
            file = open(New_File,'r')
            print(file.read())
            file.close()
            Znak_Menu = input('Введите пункт меню: ')
                        
                    
                    
    print()
    print('Программа завершена')

except ValueError:
    print('Неправильный ввод данных')
