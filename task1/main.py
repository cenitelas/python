from collections import namedtuple


user = namedtuple('User', ('name', 'bday','isActive','films'))
users = [user(name='Sasha', bday='20.04.1992', isActive=True, films=['film1', 'film2', 'film3']),
         user(name='Pasha', bday='10.03.2020', isActive=True, films=['film1', 'film2', 'film3']),
         user(name='Kesha', bday='02.02.2000', isActive=False, films=['film1', 'film2', 'film3']),
         ]


def my_help():
    print(f"\nhelp - помощь"
          f"\ncreate-user - создать пользователя"
          f"\nshow-users - список пользователей"
          f"\nexport - экспорт пользователей в файл"
          f"\nexit - выход")


def show_users():
    for us in users:
        print(f"\nИмя: {us.name}"
              f"\nГод рождения: {us.bday}"
              f"\nПризнак актичности: {'Активный' if us.isActive else 'Не активный'}"
              f"\nФильмы:")
        for index, film in enumerate(us.films):
            print(f"\t{index+1} - {film}")


def create_users():
    name = input("Введите имя: ")
    bday = input("Введите дату рождения: ")
    active = input("Активность (1/0): ")
    films = []
    for index in range(3):
        films.append(input(f"Фильм {index+1}: "))
    users.append(user(name=name, bday=bday, isActive=True if active=="1" else False, films=films))


def export():
    f = open('base.txt', 'w')
    for us in users:
        f.write(f"Имя: {us.name}"
                f"\nГод рождения: {us.bday}"
                f"\nПризнак актичности: {'Активный' if us.isActive else 'Не активный'}"
                f"\nФильмы:")
        for index, film in enumerate(us.films):
            f.write(f"\n\t{index+1} - {film}")
        f.write("\n\n")


def main():
    while True:
        menu = input(">>>")
        if menu == "help":
            my_help()
        elif menu == "create-user":
            create_users()
        elif menu == "show-users":
            show_users()
        elif menu == "export":
            export()
        elif menu == "exit":
            break
        else:
            print("\nОшибка. Нет такого пункта меню")


if __name__ == '__main__':
    main()

