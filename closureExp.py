#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# exp1: 
# 返回的函数并没有立刻执行，而是直到调用f()才执行
# 返回闭包时要牢记一点是：返回函数不要引用任何循环变量，或者后续会发生变化的变量

def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
	
f1,f2,f3 = count()
print('exp1')

print(f1())

print(f2())

print(f3())

print('\n')

# 结果并非1，4，9，而是9，9，9，
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9。

# exp2: 
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
	
f1, f2, f3 = count()

print('exp2')

print(f1())

print(f2())

print(f3())
