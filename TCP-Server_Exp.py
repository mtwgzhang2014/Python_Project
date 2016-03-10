#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import socket
import threading, time

# TCP socket based on ipv4
# server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口：
s.bind(('127.0.0.1', 9999))

# 开始监听端口，参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
	
# 每个连接都必须创建新线程来处理，否则单线程在处理连接的过程中，无法接受其他客户端的连接

# UDP 不需要连接，服务器直接bind端口，而Client直接向端口发送数据
# UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，
# 也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
