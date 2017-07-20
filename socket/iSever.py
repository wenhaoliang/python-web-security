#coding: utf-8
from socket import *


if __name__ == "__main__":
	# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
	s = socket(AF_INET, SOCK_STREAM)
	# 将套接字绑定到地址，第一个参数是绑定本机，地二个参数是端口号6666
	s.bind(('', 6666))
	# 开始监听传入连接，参数里面的数字表示最大连接数量
	s.listen(1)
	# 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
	sock, addr = s.accept()
	# 打印
	print('Connect by ', addr)
	# 发送信息
	sock.send("Welcome!!".encode())
	# 接受套接字的数据
	text = sock.recv(1024)
	# 打印
	print(text)
	# 关闭
	sock.close()
	# 关闭
	s.close()
