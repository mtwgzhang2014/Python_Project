#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# 检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数

import struct
import os.path

class bmpinfo(dict):
	
	def __init__(self, filePath):
		with open(filePath, 'rb') as tmpFile:
			bmp_type = tmpFile.read(2)
			bmp_type = ''.join(map(bytes.decode, struct.unpack('<cc', bmp_type)))
			if bmp_type not in ('BM', 'BA'):
				raise FormatError('%s is not bmp format' %filepath)
			elif bmp_type == 'BM':
				self['windows_bmp'] = True
			else:
				self['mac_bmp'] = True
			byte_contents = tmpFile.read(28) # 前面读取2字节后，这里继续向后读28个字节
			self._initial_attributes(byte_contents)
			
	def _initial_attributes(self, byte_contents):
		infoes = struct.unpack('<IIIIIIHH',byte_contents)
		self['size'] = infoes[0]
		self['width'] = infoes[4]
		self['height'] = infoes[5]
		self['depth'] = infoes[7]
	
	def __getattr__(self, name):
		if name not in self:
			return None
		else:
			return self[name]

filePath = input('Please enter the file name: ')
rootdir = r'C:\TestImages'
info = bmpinfo(os.path.join(rootdir,filePath))
print('size:%s, %s * %s dept:%s' %(info.size, info.width, info.height, info.depth))
