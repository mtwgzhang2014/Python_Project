#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# 在生产数据报表XML文件中抓取角差历史数据

#from xml.parsers.expat import ParserCreate
from xml.sax import parse,handler,SAXException
import os
import os.path
import pdb

rootDir = r'C:\Users\zhang-384\Desktop\My Works\00 OST\2015\2. 钢自动角差项目\selectXml'

class DefaultSaxHandler(handler.ContentHandler):

	def __init__(self): 
		self.honingData = ''
		self.currentTag = ''

	def endElement(self, name):
		pass
	
	def startElement(self, tag, attrs):
		self.currentTag = tag

	def characters(self, content):
		if self.currentTag == 'DATA':
			self.honingData = content
		else:
			self.honingData = ''


with open(r'C:\TestImages\tmpdata.txt', 'w') as dataFile:
	for xml in os.listdir(rootDir):
		xmlFile = os.path.join(rootDir, xml)
		try:
			saxHandler = DefaultSaxHandler()
			parse(xmlFile, saxHandler)
			print(tmpContent)
		except SAXException as msg:
			print(msg.getException())
		dataFile.writelines(saxHandler.honingData)