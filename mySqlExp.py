#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# 使用前要按照MySQL，以及MySQL驱动（支持Python的MySQL驱动来连接到MySQL服务器）

# 导入MySQL驱动
import mysql.connector
# 注意因为本机安装MySQL初始设置的端口为3000，而默认的为3306，因此要特此注意
conn = mysql.connector.connect(user='root', password='11235813', port = '3000', database='test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table userTable (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s: （这个和SQLLite里面的规范有些不同）
cursor.execute('insert into userTable (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.execute('insert into userTable (id, name) values (%s, %s)', ['2', 'Jack'])
cursor.execute('insert into userTable (id, name) values (%s, %s)', ['3', 'Petson'])
cursor.execute('insert into userTable (id, name) values (%s, %s)', ['4', 'Mason'])
cursor.execute('insert into userTable (id, name) values (%s, %s)', ['5', 'Jimmy'])
cursor.rowcount
# 提交事务(执行INSERT等操作后要调用commit()提交事务)
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from userTable where id = %s', ['3'])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


