#coding: utf-8
from socket import *

s = socket(AF_INET, SOCK_STREAM)
# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
s.bind(('', 6666))
# ���׽��ְ󶨵���ַ����һ�������ǰ󶨱������ض��������Ƕ˿ں�6666
s.listen(1)
# ��ʼ�����������ӣ�������������ֱ�ʾ�����������
sock, addr = s.accept()
# �������Ӳ����أ�conn,address��,����conn���µ��׽��ֶ��󣬿����������պͷ������ݡ�address�����ӿͻ��˵ĵ�ַ��
print('Connect by ', addr)
# ��ӡ
sock.send("Welcome!!".encode())
# ������Ϣ
text = sock.recv(1024)
# �����׽��ֵ�����
print(text)
# ��ӡ
sock.close()
# �ر�
s.close()
# �ر�