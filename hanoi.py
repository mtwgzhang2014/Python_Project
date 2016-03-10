#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hanoi pazzle

def move(n,a,b,c):
	if n==1:
		print(a+'-->'+c)
		return
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
		
def pas_triangles():
	a = [1]
	while True:
		yield a
		a = [sum(i) for i in zip([0]+a, a+[0])]
	
n = input('Please enter the num:')
n = int(n)
move(n,'A','B','C')