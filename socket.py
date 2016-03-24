#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect(('www.sina.com',80))

a.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buf = []
while  true:
	d = a.recv(1024) #每次最多接收1k
	if d:
		buf.append(d)
	else:
		break
data = ''.join(buf)
a.close()

header, html = data.split('\r\n\r\n',1)
print header
