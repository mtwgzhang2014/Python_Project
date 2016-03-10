#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# 检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数

import struct

filePath = input('Please enter the filePaht:\n')

def bmpCheck(filePath):
	with open(filePath, 'rb') as tmpfile:
		keyInfo = tmpfile.read(30) # 参数可以确定读取数据的长度
		info = struct.unpack('<ccIIIIIIHH', keyInfo)
		if info[0] == b'B' and info[1] == b'M':
			print('The size of the picture is: %d * %d' % (info[6], info[7]))
			print('The numbers of color is: %d' % info[9])
			return True
		else:
			print('This isn\'t a bmp file.')
			return False

bmpCheck(filePath)

# class bmpinfo(dict):

    # def __init__(self, filepath):
        # with open(filepath, 'rb') as f:
            # bmp_type = f.read(2)
            # bmp_type = ''.join(map(bytes.decode, struct.unpack('<cc', bmp_type)))
            # if bmp_type not in ('BM', 'BA'):
                # raise FormatError('%s is not bmp format' %filepath)
            # if bmp_type == 'BM':
                # self['windows_bmp'] = True
            # else:
                # self['mac_bmp'] = True
            # bype_contents = f.read(28)
            # self._initial_attributes(bype_contents)

    # def _initial_attributes(self, byte_contents):
        # infos = struct.unpack('<IIIIIIHH', byte_contents)
        # self['size'] = infos[0]
        # self['width'] = infos[4]
        # self['height'] = infos[5]
        # self['depth'] = infos[7]

    # def __getattr__(self, name):
        # if name not in self:
            # return None
        # return self[name]

# info = bmpinfo('test.bmp')
# print('size:%s, dept:%s' %(info.size, info.depth))
