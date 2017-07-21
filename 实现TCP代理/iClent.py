#coding: utf-8
from socket import *
import sys


if __name__ == "__main__":
	# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
	c = socket(AF_INET, SOCK_STREAM)
	# 从输入中接受端口号
	port = int(sys.argv[1])
	# 将套接字连接到地址，第一个参数是连接的地址，地二个参数是端口号6666
	c.connect(('127.0.0.1', port))
	# 打印
	print('Connect success.')
	# 发送数据
	c.send('Yes or no?')
	# 接受数据
	data = c.recv(1024)
	# 打印
	print(data)
	# 关闭
	c.close()
