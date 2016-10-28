import Tkinter as tk
import socket
from multiprocessing import Process, Queue

class MyTcpServer():

	def __init__(self):
		self.val = 70

	def tcpServer(self, q):
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
			q.put(self.val)
			print "Heart Rate: " + str(self.val)
			c.send(self.data)
            
		c.close()

def myPlot(q):
	line1, = ax.plot([], [],'-k',label='black')
	line2, = ax.plot([], [],'-r',label='red')
	
if __name__ == "__main__":
	tcp = MyTcpServer()
	q = Queue()
	Process(target=tcp.tcpServer, args=(q,)).start()

    















ax.legend()
for i in range(0, 100):
	A.append(R1 * i * np.sin(i))
	B.append(R2 * i * np.cos(i))
	line1.set_ydata(A)
	line1.set_xdata(range(len(A)))
	line2.set_ydata(B)
	line2.set_xdata(range(len(B)))
	ax.relim()
	ax.autoscale_view()
	plt.draw() 