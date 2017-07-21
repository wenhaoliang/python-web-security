#coding: utf-8
from socket import *
from os import *


if __name__ == "__main__":
	# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
	c = socket(AF_INET, SOCK_STREAM)
	# 将套接字连接到地址，第一个参数是连接的地址，地二个参数是端口号6666
	c.connect(('127.0.0.1', 6666))
	# 循环
	while True:
		msg = raw_input('Message> ')
		c.send(msg)
		data = c.recv(1024)
		print(data)
		c.close()