#coding: utf-8


from scapy.all import *	


def pack_callback(packet):
	if packer[TCP].playload:
		mail_packet = str(packet[TCP].playload)
		
		if "user" in mail_packet.lower() or "pass" in mail_packet.lower()
			print "[']  server: %s " % packet[IP].dst


sniff(filter = 'tcp port 80 or tcp port 25 or tcp port 143', prn = pack_callback, store = 0)