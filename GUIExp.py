#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# Tkinker库调用Tk构建GUI

from tkinter import *
import tkinter.messagebox as messagebox

class Applicantion(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.quitButton = Button(self, text='Quit', command=self.hello)
		self.quitButton.pack()
		
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' % name)
		
	# 在GUI中，每个控件都是一个Widget， Frame是可以容纳其他Widget的Widget
	# pack()方法把Widget加入到父容器中，并实现布局
	
app = Applicantion()
# 设置窗口标题：
app.master.title('Hello World')
# 主消息循环
app.mainloop()
