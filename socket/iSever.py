#coding: utf-8
from socket import *

s = socket(AF_INET, SOCK_STREAM)
# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
s.bind(('', 6666))
# 将套接字绑定到地址，第一个参数是绑定本机，地二个参数是端口号6666
s.listen(1)
# 开始监听传入连接，参数里面的数字表示最大连接数量
sock, addr = s.accept()
# 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
print('Connect by ', addr)
# 打印
sock.send("Welcome!!".encode())
# 发送信息
text = sock.recv(1024)
# 接受套接字的数据
print(text)
# 打印
sock.close()
# 关闭
s.close()
# 关闭