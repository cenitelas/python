import sqlite3
from collections import namedtuple

conn = sqlite3.connect("base.db")
cursor = conn.cursor()

cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')

if cursor.fetchone()[0] != 1:
    cursor.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, bday text, isActive int)""")
    cursor.execute("""CREATE TABLE films (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)""")
    cursor.execute("""CREATE TABLE userFilm (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id int, film_id int)""")
    conn.commit()


user = namedtuple('User', ('name', 'bday','isActive','films'))
users = []


def my_help():
    print(f"\nhelp - помощь"
          f"\ncreate-user - создать пользователя"
          f"\nshow-users - список пользователей"
          f"\nexit - выход")


def show_users():
    for row in cursor.execute("SELECT u.name,bday,isActive, GROUP_CONCAT(f.name) FROM users AS u LEFT JOIN userFilm AS uf ON uf.user_id=u.id LEFT JOIN films AS f ON f.id=uf.film_id GROUP BY u.name"):
        print(f"\nИмя: {row[0]}"
              f"\nГод рождения: {row[1]}"
              f"\nПризнак актичности: {'Активный' if row[2] == 1 else 'Не активный'}"
              f"\nФильмы:")
        for index, film in enumerate(row[3].split(',')):
            print(f"\t{index+1} - {film}")
    conn.commit()


def create_users():
    name = input("Введите имя: ")
    bday = input("Введите дату рождения: ")
    active = input("Активность (1/0): ")
    films = []
    for index in range(3):
        films.append(input(f"Фильм {index+1}: "))
    cursor.execute(f"INSERT INTO users(name,bday,isActive) VALUES ('{name}', '{bday}', '{active}')")
    conn.commit()
    user_id = cursor.lastrowid
    for film in films:
        cursor.execute(f"SELECT count(id) FROM films WHERE name='{film}'")
        if cursor.fetchone()[0] != 1:
            cursor.execute(f"INSERT INTO films(name) VALUES ('{film}')")
            conn.commit()
            film_id = cursor.lastrowid
            cursor.execute(f"INSERT INTO userFilm(user_id,film_id) VALUES ('{user_id}', '{film_id}')")
        else:
            film_id = cursor.execute(f"SELECT id FROM films WHERE name='{film}'").fetchone()[0]
            cursor.execute(f"INSERT INTO userFilm(user_id,film_id) VALUES ('{user_id}', '{film_id}')")
    conn.commit()


def main():
    while True:
        menu = input(">>>")
        if menu == "help":
            my_help()
        elif menu == "create-user":
            create_users()
        elif menu == "show-users":
            show_users()
        elif menu == "exit":
            break
        else:
            print("\nОшибка. Нет такого пункта меню")
    conn.close()


if __name__ == '__main__':
    main()



