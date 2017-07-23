#coding: utf-8

from socket import *
import sys

clientPort = int(sys.argv[1])
severHost = sys.argv[2]
severPort = int(sys.argv[3])

mainSocket = socket(AF_INET, SOCK_STREAM)
remoteSocket = socket(AF_INET, SOCK_STREAM)


def setMainSocker(port):
	mainSocket.bind(('', port))
	mainSocket.listen(1)

	
def forwardData(Data):
	remoteSocket.connect((severHost, severPort))
	remoteSocket.send(Data)
	remoteData = remoteSocket.recv(1024)
	remoteSocket.close()
	return remoteData
	

def mainHandle():
	mainSock, mainAddr = mainSocket.accept()
	print('Connect by ', mainAddr)
	while True:
		data = mainSock.recv(1024)
		remoteData = forwardData(data)
		mainSock.send(remoteData)

if __name__ == "__main__":
	try:
		setMainSocker(clientPort)
		mainHandle()
	except:
		pass
	