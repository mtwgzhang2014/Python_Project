#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# debugExp.py

# Example #1

def foo(s):
	n = int(s)
	assert n!=0, 'n is zero!'
	return 10/n
	
def main():
	foo('1')
	
if __name__ == '__main__':
	main()

# assert的意思是，表达式n != 0应该是True，
# 否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError

# $ Python -O debugExp.py 可以关闭assert，所有assert语言被当成pass

# Example #2

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。


# pdb 调试器
# $ Python -m pdb debugExp.py 启动调试器
# 输入命令‘l’来查看代码
# 输入命令‘n’可以单步执行代码
# 输入命令‘p 变量名’来查看变量
# 输入命令‘q’结束调试，退出程序
# pdb.set_trace() 设置断点！！！程序由此处进入pdb模式，输入命令'c'继续运行
