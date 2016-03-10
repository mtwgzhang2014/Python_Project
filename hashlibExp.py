#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# 注册用户名密码，并用用户名密码登录，MD5

import hashlib

# default user
db = {
    # 'michael': 'e10adc3949ba59abbe56e057f20f883e',
    # 'bob': '878ef96e86145580c38c87f0410ad153',
    # 'alice': '99b1c2188db85afee403b1536010c2c9'
}

# 计算md5码
def get_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

# 用户注册
def register(username, password):
	db[username] = get_md5(password + username + 'the-Salt')	# 增加MD5被识破的难度

# 用户登录账户检查
def login(user, password):
	if user not in db:
		print('%s is no a valid user name!' % user)
	else:
		if db[user] == get_md5(password + username + 'the-Salt'):
			print('Password is right! Welcome to...')
		else:
			print('Password is wrong!')

print('Registe first!')
username = input('Username: ')
password = input('Password: ')
register(username, password)
print('Now please login!')
user = input('User: ')
password = input('Password: ')
login(user, password)		
