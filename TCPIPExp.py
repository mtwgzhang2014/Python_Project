#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接新浪服务器
s.connect(('www.sina.com.cn', 80))

# 发送数据
# 发送的文本格式必须符合HTTP标准
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据：
buffer = []
while True:
	# 每次最多接收1k字节：
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

# 循环接收服务器发来的数据，直到recv()返回空数据

# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件：
with open('sina.html', 'wb') as f:
	f.write(html)
	
# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，
# 网页内容保存到文件
