import matplotlib.pyplot as plt
import socket

class MyTcpServer():

	def __init__(self):
		self.val = 70
		self.idx = 1

	def tcpServer(self):
		host = '0.0.0.0'
		port = 1025

		s = socket.socket()
		s.bind((host, port))

		s.listen(1)
		c, addr = s.accept()
		print "Connection from: " + str(addr)
		while True:
			self.data = c.recv(1024)
            
			if not self.data:
				break
			idx1 = str(self.data).find(':')
			idx2 = str(self.data).find('_')
			self.val = int(str(self.data)[idx1+1:idx2])
			print "Heart Rate: " + str(self.val)
			c.send(self.data)
			plt.scatter(self.idx, self.val, color='r')
			plt.pause(.1)
			self.idx = self.idx + 1
            
		c.close()
	
if __name__ == "__main__":
	plt.ion()
	tcp = MyTcpServer()
	tcp.tcpServer()

    
