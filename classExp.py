#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

#from moduleExp import hello

# Example 1

class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('Bad score!')
	
	def get_name(self):
		return self.__name
		
	def get_score(self):
		return self.__score
	
	def set_name(self, name):
		self.__name = name
	
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('Bad score!')
		
	def print_score(self):
		print('%s, %s' % (self.__name, self.__score))
	
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

			
# test code
print('Example #1')
bart = Student('Bart Simpson', 90)
bart.print_score()
print('%s get %s!' % (bart.get_name(), bart.get_grade()))

print('\nnext case:')

bart.score = 59
bart.set_score(70)
bart.print_score()
print('%s get %s!' % (bart.get_name(), bart.get_grade()))
print('====================\n')

# Example 2

class Animal(object):
	def run(self):
		print('Animal is runing...')
		
class Dog(Animal):
	def run(self):
		print('Dog is runing...')
		
class Cat(Animal):
	def run(self):
		print('Cat is runing...')
		
class Tortoise(Animal):
	def run(self):
		print('Tortoises is runing slowly...')
		
class Timer(object):
	def run(self):
		print('Timer start!')
		
def run_twice(animal):
	animal.run()
	animal.run()
	
# test code
print('Example #2')
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
run_twice(Timer())
print('====================\n')

# 多态的开闭原则
# 对扩展开放：允许新增Animal子类
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
# 对于Python这样的动态语言，不一定需要传入Animal类型，只要保证传入的对象有一个run()方法

# Example 3

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))

# Example 4 

# 给实例绑定属性和方法，动态语言可以给实例绑定任何属性和方法

class Student(object):
	pass
	
s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 动态地将函数绑定给实例
s.set_age(25) # 调用实例方法
print(s.age)

# 但是给一个实例绑定的方法，对另一个实例不起作用
# 为了给所有实例都绑定方法，可以给class绑定方法

def set_score(self, score):
	self.score = score
	
Student.set_score = MethodType(set_score, Student)

# 通常情况下，上面的set_score方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# Example 5 

# 使用特殊变量__slots__，来限制class实例能增加的属性，但对继承的子类不起作用

class Frident(object):
	__slots__ = ('name', 'age')
	
# Example 6

# 限制属性的读写（类似C#中将字段重写为属性）

class Student(object):
	
	@property # getter 方法
	def score(self):
		return self.__score

	@score.setter # setter 方法
	def score(self, value)
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self.__score

# 只读属性age，只定义getter方法，不定义setter		
class personInf(object):
	
	@property
	def birth(self):
		return self.__birth
		
	@birth.setter
	def birth(self, value):
		self.__birth = value
	
	@property
	def age(self):
		return 2016 - self.birth
		