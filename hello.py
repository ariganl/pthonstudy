#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print"hello world"
# name  = raw_input("please input your name:")
# print "hello "+ name

# sum = 0
# for x in xrange(1,10):
# 	sum = sum + x
# print sum

# def add(a,b):
# 	return a+b
# print add(10,12)

def count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs

f1 , f2 , f3 = count()
print f1(),f2(),f3()