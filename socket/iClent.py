#coding: utf-8
from socket import *


if __name__ == "__main__":
	# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
	c = socket(AF_INET, SOCK_STREAM)
	# ���׽������ӵ���ַ����һ�����������ӵĵ�ַ���ض��������Ƕ˿ں�6666
	c.connect(('127.0.0.1', 6666))
	# ��������
	text = c.recv(1024)
	# ��ӡ
	print(text)
	# ��������
	c.send("HELLO!!".encode())
	# �ر�
	c.close()
