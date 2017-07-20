#coding: utf-8
from socket import *

c = socket(AF_INET, SOCK_STREAM)
# 第一个参数是"服务器之间网络通信", 第二个参数是"流式socket , for TCP"
c.connect(('127.0.0.1', 6666))
# 将套接字连接到地址，第一个参数是连接的地址，地二个参数是端口号6666
text = c.recv(1024)
# 接受数据
print(text)
# 打印
c.send("HELLO!!".encode())
# 发送数据
c.close()
# 关闭