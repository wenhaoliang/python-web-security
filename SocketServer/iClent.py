#coding: utf-8
from socket import *
from os import *


if __name__ == "__main__":
	# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
	c = socket(AF_INET, SOCK_STREAM)
	# ���׽������ӵ���ַ����һ�����������ӵĵ�ַ���ض��������Ƕ˿ں�6666
	c.connect(('127.0.0.1', 6666))
	# ѭ��
	while True:
		msg = raw_input('Message> ')
		c.send(msg)
		data = c.recv(1024)
		print(data)
		c.close()