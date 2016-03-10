#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x