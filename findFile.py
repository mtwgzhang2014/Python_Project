#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# findFile.py for 操作文件和目录: 查找文件
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
# 并打印出相对路径。

import os
import os.path

targetDir = input('Please enter where you want to search:\n')
key = input('Please enter what you want to search:\n')


def find_file(targetDir, key):
	if targetDir == '':
		targetDir = os.getcwd()
	for parent,dirnames,filenames in os.walk(targetDir):
		for file in filenames:
			tmpFile = file[0:file.find('.')]
			if key in tmpFile:
				print('The file path is: %s'% os.path.join(parent,file))

find_file(targetDir, key)	

