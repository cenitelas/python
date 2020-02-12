from collections import namedtuple
import secrets
import string

users = []
user = namedtuple("user",('id','name', 'login','pos','password'))

with open('db.txt') as f:
    for line in f:
        z = line.split(':')
        alphabet = z[0] + z[1] + z[2] + z[3]
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        login = f'{z[1].lower()[0]}{z[2].lower()[0]}{z[3].lower()}'
        name = f'{z[1].upper()[0]}.{z[2].upper()[0]}. {z[3]}'
        pos = z[4].split('\n')[0]
        u = user(z[0],name,login,pos,password)
        users.append(u)


    print(f'{"Full name":.^20}{"id":.^10}{"Position":.^12}{"Login":.^20}{"Password":.^15}')    
for us in users:
    print(f'{us.name:^20}{us.id:^10}{us.pos:^12}{us.login:^20}{us.password:^15}')    