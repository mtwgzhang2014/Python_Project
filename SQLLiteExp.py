#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

# 返回指定分数区间的名字，按分数从低到高排序
def get_score_in(low, high):
	try:
		conn = sqlite3.connect('test.db')
		cursor = conn.cursor()
		cursor.execute('select name from user where score between ? and ? order by score', (low, high))
		values = cursor.fetchall()
		if len(values) == 0:
			print('输入有误，没有这个分数段的学生！')
			values = ['']
	except:
		print('Something is wrong!')
		values = ['']
	finally:
		cursor.close()
		conn.close()
	return list(map(lambda x:x[0], values)) # 直接返回values每个元素中带有一个逗号

# 测试:
#assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
