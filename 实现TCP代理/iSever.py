#coding: utf-8
from socket import *


if __name__ == "__main__":
	# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
	s = socket(AF_INET, SOCK_STREAM)
	# ���׽��ְ󶨵���ַ����һ�������ǰ󶨱������ض��������Ƕ˿ں�6666
	s.bind(('', 6666))
	# ��ʼ�����������ӣ�������������ֱ�ʾ�����������
	s.listen(1)
	# ����һ��ѭ��
	while True:
		# �������Ӳ����أ�conn,address��,����conn���µ��׽��ֶ��󣬿����������պͷ������ݡ�address�����ӿͻ��˵ĵ�ַ��
		sock, addr = s.accept()
		# ��ӡ
		print('Connect by ', addr)
		# ������Ϣ
		data = sock.recv(1024)
		# ��ӡ
		print(data)
		# ����
		sock.send('Yes')
