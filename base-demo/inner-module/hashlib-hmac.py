# -*- coding: utf-8 -*-
import hashlib
import random


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


print('Leopen', calc_md5('Leopen'))
print('leopen', calc_md5('leopen'))

# login

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    user_md5 = calc_md5(password)
    if user_md5 == db[user]:
        return True
    else:
        return False


print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))

# add salt
print('salt-------------------------------------------')


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(username + password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login2(username, password):
    user = db[username]
    return user.password == get_md5(username + password + user.salt)


print(login2('michael', '123456'))

# hmac
print('hmac------------------------------------------------')
import hmac  # nopep8


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User_hmac(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User_hmac('michael', '123456'),
    'bob': User_hmac('bob', 'abc999'),
    'alice': User_hmac('alice', 'alice2008')
}


def login3(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


print(login3('michael', '123456'))
