#coding: utf-8
from socket import *

c = socket(AF_INET, SOCK_STREAM)
# ��һ��������"������֮������ͨ��", �ڶ���������"��ʽsocket , for TCP"
c.connect(('127.0.0.1', 6666))
# ���׽������ӵ���ַ����һ�����������ӵĵ�ַ���ض��������Ƕ˿ں�6666
text = c.recv(1024)
# ��������
print(text)
# ��ӡ
c.send("HELLO!!".encode())
# ��������
c.close()
# �ر�