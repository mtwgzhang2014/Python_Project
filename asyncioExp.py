#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# asyncio Example

import threading
import asyncio

# @asyncio.coroutine
# def hello():
    # print('Hello world! (%s)' % threading.currentThread())
    # yield from asyncio.sleep(10)
    # print('Hello again! (%s)' % threading.currentThread())

# 获取EventLoop
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# 执行coroutine
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，
# 然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

