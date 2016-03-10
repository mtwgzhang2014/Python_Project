#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在面向对象的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
# 而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以
# 用函数实现，也可以用类实现

# decorator增强函数的功能

# 下例中编写一个decorator，能在函数调用的前后打印出‘begin call’和‘end call’的日志
# 并考虑同时支持@log和@log('execute')

import functools

# decorator
def log(para):
	# 判断func是可以调用的函数还是字符串之类的变量
	if callable(para): 
		func = para
		# 经过decorator装饰之后的函数，它们的__name__已经从原来的‘now’变成了‘wrapper’
		# 因为返回的那个wrapper()函数名字就是'wrapper', 所以需要把原始函数的__name__等属性
		# 复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
		@functools.wraps(func)  
		def wrapper(*args, **kw):
			print('begin call %s()' % func.__name__)
			fc = func(*args, **kw)
			print('end call %s()' % func.__name__)
			return fc # 返回函数变量，则可以将原函数返回值返回，否则没有返回值
		#print('end call %s()' % func.__name__)
		return wrapper
	elif isinstance(para, str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*arg, **kw):
				print('begin call %s()' % func.__name__)
				print('%s %s()' % (para, func.__name__))
				fc = func(*arg, **kw)
				print('end call %s()' % func.__name__)
				return fc
			return wrapper
		return decorator
	else:
		print('para is wrong!')
	
# original func

#@log
@log('execute')
def now():
	a = 100;
	print('2016-2-19')
	return a
	
f = now
#f()
print(f())
#print(now.__name__)
print('\n')







