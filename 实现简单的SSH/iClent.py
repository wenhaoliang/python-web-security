#coding: utf-8
from socket import *
from os import *


c = socket(AF_INET, SOCK_STREAM)
# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
c.connect(('127.0.0.1', 6666))
# ���׽������ӵ���ַ����һ�����������ӵĵ�ַ���ض��������Ƕ˿ں�6666
while True:
# ѭ��
	cmd = raw_input('please input your cmd command:   ')
	# �Ӽ�������cmd����
	c.send(cmd)
	# ����cmd����
	if cmd == 'exit':
	# �ж������Ƿ���exit
		c.close()
		# �Ͽ�����
		break
		# ����ѭ��
	data = c.recv(1024)
	# ������Ϣ
	print(data)
	# ��ӡ����