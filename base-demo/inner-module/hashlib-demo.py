# -*- coding: utf-8 -*-
import hashlib


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
