#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9996))
print s.recv(1024)
for data in ['Matrc','LiJie','Cheng']:
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close();
