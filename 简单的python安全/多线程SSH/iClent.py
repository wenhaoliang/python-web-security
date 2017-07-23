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
		# 从键盘输入cmd命令
		cmd = raw_input('please input your cmd command:   ')
		# 发送cmd命令
		c.send(cmd)
		# 判断命令是否是exit
		if cmd == 'exit':
			# 断开连接
			c.close()
			# 跳出循环
			break
			# 接收信息
		data = c.recv(1024)
		# 打印出来
		print(data)
