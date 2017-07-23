#coding: utf-8 


import SocketServer
import re
from socket import * 


def getHost(dataPack):
	result = re.search(r'Host:\s(.*?)\s', dataPack)
	host = result.group(1)
	return host
	
	
class myProxy(SocketServer.BaseRequestHandler):


	def handle(self):
		self.httpReqst = self.request.recv(1024)
		print(self.httpReqst)
		self.rhost = getHost(self.httpReqst)
		newSock = socket(AF_INET, SOCK_STREAM)
		newSock.connect((str(self.rhost), 80))
		newSock.send(self.httpReqst)
		buffer = []
		while True:
			d = newSock.recv(1024)
			if d:
				buffer.append(d)
			else:
				break
		self.httpReqst = ''.join(buffer)
		self.request.sendall(self.httpReqst)

		
if __name__ == '__main__':
	addr = ('127.0.0.1', 8080)
	server = SocketServer.ThreadingTCPServer(addr, myProxy)
	server.serve_forever()















		