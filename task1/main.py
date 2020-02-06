from collections import namedtuple

users = []
user = namedtuple("user",('name','bday','active','films'))
def create_user():
    name =input("\tВведите имя: ")
    bday =input("\tВведите год рождения: ")
    activ = input("\tАктивность (Д/Н): ")
    print("\tДобавте 3 фильма:")
    films = []
    for item in range(1,4):
        films.append(input(f'\t\t{item}>'))
    u = user(name,bday,activ,','.join(films))
    users.append(u)

def help():
    print("1 - Добавить пользователя")
    print("2 - Отобразить всех пользователей")
    print("3 - Экспорт пользователей в файл")
    print("4 - Выход")
    menu=int(input(">"))
    if(menu==1):
        create_user()
        help()
    if(menu==2):
        print("\n\t\t Пользователи:")
        print(f'{"Имя":^10} {"Дата родения":^15} {"Активность":^10} {"Фильмы":^20}')
        for item in users:
            print(f'{item.name:^10} {item.bday:^12} {item.active:^17} {item.films:^20}')
        input(f"{'':-^60}")
        print("\n\n")
        help()
    if(menu==3):
        print(3)
    if(menu==4):
        exit

help()

#     help - команда помощи, описывающая все команды
# create-user - просит ввести информацию о регистрируемом пользователе (см. ниже)
# show-users - отображает всех пользователей
# export {путь к файлу} - экспорт всех пользователей в текстовый файл (каждый пользователь на новой строке, формат csv)
# exit - выход из программы
