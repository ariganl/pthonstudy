#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import threading
import time

print socket.__file__

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9996))
s.listen(5)
print"Waiting for connect..."

def tcplink(sock, addr):
	print 'accept new connection from %s:%s ... '% addr
	sock.send('Weclcome!')
	recvflag = True
	while  True:
		if(recvflag):
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			sock.send('Hello &DW')
		else:
			sock.send('Hello %s!'% data)
	sock.close()
	print 'connection from %s:%s...'% addr

while  True:
	sock,addr = s.accept()
	print addr
	print sock
	t = threading.Thread(target = tcplink, args = (sock, addr))  # 指明函数入口，
	t.start()



