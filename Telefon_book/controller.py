import In
import Prog
import Out



def book():
    while True:
        print('Список команд: \n 1 - добавить контакт \n 2 - удалить контакт \n 3 - посмотреть список контактов \n 4 - найти номер по имени \n 5 - завершить работу \n')
        command = int(input('Введите номер команды: '))
        if command == 1:
            a = In.get_name()
            b = In.get_number()
            In.phone_number(a, b)
            book_new = In.get_data()
            Prog.add_phone_number(book_new)
            print('Данные успешно сохранены \n')                
        elif command == 2:
            x = In.search_kontakt()
            Prog.del_phone_number(x)
            print('Данные успешно удалены \n')  
        elif command == 3:
            print('Телефонная книга: \n')
            Out.look_phone_book()
        elif command == 4:
            x = In.search_kontakt()
            print('Данные по вашему запросу: \n')
            Out.search_view_number(x)
        elif command == 5:
            print('До новых встреч!')
            break
        else:
            print('Введите корректную команду')

        
#book()