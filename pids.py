#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

def write(p):
	for val in ['A','B','C']:
		print 'Put %s to Queue...' % val
		p.put(val)
		time.sleep(random.ramdom())

def read(p):
	while True:
		val = p.get(True)
		print 'Get %s from Queue.' % val

if  __name__ == '__main__':
	q = Queue()
	pw = Process(target = write, args = (q,))
	pr = Process(target = read , args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
