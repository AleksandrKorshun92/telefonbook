phone_book={}
path: str='spravochnik.txt'

def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    print(data)
    file.close()
    for contact in data:
        nc =contact.strip().split(':')
        phone_book[int(nc[0])] = {'name':nc[1], 'phone':nc[2], 'commit':nc[3]}
    print('\nТелефонная книга загружена')  
    
def show_contacts(book: dict[int,dict]):
    print('='*200 +'\n')
    for i, cnt in book.items():
        print(f'{i:>3}.{cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("commit"):<20}')
    print('='*200 +'\n')

def add_contact():
    uid = max(list(phone_book.keys()))+1
    name = input("Напишите имя контакта ")
    phone = input("Напишите телефон контакта ")
    commit = input("Напишите комментарий к контакту ")
    phone_book[uid] = {'name': name, 'phone': phone, 'commit': commit}
    print(f'\nКонтакт {name} успешно добавлен в книгу')

def save_file():
    data =[]
    for i, contact in phone_book.items():
        new = ':'.join([str(i),contact.get('name'), contact.get('phone'), contact.get('commit')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print(data)
    print(f'\nКнига сохранена')

def seerch():
    result = {}
    word = input('Введите слова для поиска ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i]=contact
        else:
            print('Контакт не найден, попробуйте повторить поиск по другому содержанию ')
            break
    return result

def remove():
    result = seerch()
    show_contacts(result)
    id_contact = int(input('Напишите id контакта который нужно удалить '))
    del_cnt = phone_book.pop(id_contact)
    print(f'\nКонтакт {del_cnt.get("name")} который удалил')

def change():
    result = seerch()
    show_contacts(result)
    id_contact = int(input('Напишите id контакта который нужно изменить '))
    choice = int(input('Если, поменять весь контакт напишет = 1. Если заменить содержание контакта = 2 '))
    if choice == 1:
        name = input("Напишите имя ИЗМЕНЕННОГО контакта ")
        phone = input("Напишите телефон ИЗМЕНЕННОГО контакта ")
        commit = input("Напишите комментарий к ИЗМЕНЕННОМУ контакту ")
        phone_book[id_contact] = {'name': name, 'phone': phone, 'commit': commit}
        print(f'\nКонтакт {id_contact} изменен на {name} добавлен в книгу')
    elif choice == 2:
        corekt = int(input('Изменить имя, нажмите = 1. Изменить телефон, нажмите = 2. Изменить комментарий, нажмите = 3 '))
        if corekt ==1:
            name = input("Напишите ИЗМЕНЕННОЕ имя контакта ")
            phone_book[id_contact]['name'] = name
            print(f'\nИмя контакта изменено на {name}')
        elif corekt ==2:
            phone = input("Напишите ИЗМЕНЕННЫЙ телефон контакта ")
            phone_book[id_contact]['phone'] = phone
            print(f'\nТелефон изменен на {phone}')
        elif corekt ==3:
            commit = input("Напишите ИЗМЕНЕННЫЙ комментарий к контакту ")
            phone_book[id_contact]['commit'] = commit
            print(f'\Комментарий контакта изменен на {commit}')
        else:
            print('Ошибка ввода. Укажите Цифру из меню')
    else:
            print('Ошибка ввода. Укажите Цифру из меню')
    

def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Закрыть файл
    3. Показать контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
            select = input('Выберите пункт меню: ')
            if select.isdigit() and 0 < int(select) <9:
                  return int(select)
            print('Ошибка ввода, напишите ЧИСЛО от 1 до 8 ')



open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            result = seerch()
            show_contacts(result)
        case 6:
            change()
        case 7:
            remove()
        case 8:
            print("До свидания, до новых встреч")
            break
    print("-"*50)

