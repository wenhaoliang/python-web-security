#coding: utf-8
from socket import *
import sys


if __name__ == "__main__":
	# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
	c = socket(AF_INET, SOCK_STREAM)
	# �������н��ܶ˿ں�
	port = int(sys.argv[1])
	# ���׽������ӵ���ַ����һ�����������ӵĵ�ַ���ض��������Ƕ˿ں�6666
	c.connect(('127.0.0.1', port))
	# ��ӡ
	print('Connect success.')
	# ��������
	c.send('Yes or no?')
	# ��������
	data = c.recv(1024)
	# ��ӡ
	print(data)
	# �ر�
	c.close()
