#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import logging


# Example #2

print('Example #1')

try:
    print('try...')
    r = 10 / int('0') # or 'a'
    print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
	print('no error!')
finally:
    print('finally...')
print('END')


# test result

# try...
# except: division by zero
# finally...
# END

# Example #2

print('\nExample #2')

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
		#print('Error:', e)
        logging.exception(e)
    finally:
        print('finally...')
		
if __name__=='__main__': 
	main()
	
# Example #3

print('\nExample #3')

class FooError(ValueError):
	pass
	
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n
	
def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		#raise

bar()