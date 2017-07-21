#coding: utf-8

import SocketServer

class testSocket(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024)
		print(self.data)
		self.msg = raw_input('Message> ')
		self.request.send(self.msg)
		

if __name__ == '__main__':
	host = ''
	port = 6666
	addrInfo = (host, port)
	server = SocketServer.ThreadingTCPServer(addrInfo, testSocket)
	server.serve_forever()