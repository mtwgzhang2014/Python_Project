#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize(name):
	return name[:1].upper()+name[1:].lower()
	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

######################################################

from functools import reduce

def prod(L):
	def multiply(x,y):
		return x*y
	return reduce(multiply, L)
	#return reduce(lambda x,y:x*y,L)
	
print('3*5*7*9 = ', prod([3,5,7,9]))
print('\n')

######################################################

CHAR_TO_INT = {
	'0':0,
	'1':1,
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9
}

def str2int(s):
	ints = map(lambda ch: CHAR_TO_INT[ch], s)
	return reduce(lambda x,y:x*10+y, ints)

print('str2int Test') 
print(str2int('0')) 
print(str2int('12300')) 
print(str2int('0012345')) 
print('\n')

######################################################

CHAR_TO_FLOAT = {
	'0':0,
	'1':1,
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9,
	'.':-1
}

def str2float(s):
	nums = map(lambda ch: CHAR_TO_FLOAT[ch],s)
	point = 0
	def to_float(f,n):
		nonlocal point
		if n == -1:
			point = 1
			return f
		if point == 0:
			return f*10+n
		else:
			point = point * 10
			return f + n / point
	return reduce(to_float,nums,0.0) # 0.0 is initial value for reduce

print('str2int Test') 	
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
	
	
print('str2float(\'123.456\') =', str2float('123.456'))
