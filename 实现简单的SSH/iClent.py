#coding: utf-8
from socket import *
from os import *


c = socket(AF_INET, SOCK_STREAM)
# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
c.connect(('127.0.0.1', 6666))
# 将套接字连接到地址，第一个参数是连接的地址，地二个参数是端口号6666
while True:
# 循环
	cmd = raw_input('please input your cmd command:   ')
	# 从键盘输入cmd命令
	c.send(cmd)
	# 发送cmd命令
	if cmd == 'exit':
	# 判断命令是否是exit
		c.close()
		# 断开连接
		break
		# 跳出循环
	data = c.recv(1024)
	# 接收信息
	print(data)
	# 打印出来