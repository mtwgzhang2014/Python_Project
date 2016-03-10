#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成1000以内的质数
# 采用埃氏筛选法

# 注意到 iterator 是惰性计算的序列，所以我们可以用Python表示“全体自然数”
# “全体质数”这样的序列，而代码非常简洁

# generator for odd nums list
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

# 
def _not_divisible(n):
	return lambda x: x%n>0
	
def primes():
	yield 2
	it = _odd_iter() # initial seq
	while True:
		n = next(it) # return the first num of the seq
		yield n
		it = filter(_not_divisible(n), it)
		
# print prime num in 1000
for n in primes():
	if n < 1000:
		print(n)
	else:
		break
