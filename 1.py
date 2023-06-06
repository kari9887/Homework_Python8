def add_user():
    with open('task1.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(input('введите Фамилия,Имя,Телефон - '))

def read_all_users():
    with open('task1.txt', 'r') as f:
        for line in f:
            print(line.strip())

def search_user():
    with open('task1.txt', 'r') as f:
        search = input("Что ищем? - ")
        for line in f:
            if search in line:
                print(line.strip())
            # else:
            #     print("Таких нет")

def info_func():
    print("\n1. Показать весь справочник ")
    print("2. Добавить пользователя ")
    print("3. Поиск пользователя ")
    print("4. Выход")

info_func()
while (user_action := int(input("\nВыберите функцию, через цифру - "))) != 4:
    match user_action:
        case 1:
            read_all_users()
            info_func()
        case 2:
            add_user()
            info_func()
        case 3:
            search_user()
            info_func()
        case 4:
             break
        case _:
            print("\n!Нет такой функции!")
            info_func()