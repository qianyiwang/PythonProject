import socket
def Main():
	host = '0.0.0.0'
	port = 1025

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print "Connection from: " + str(addr)
	while True:
		data = c.recv(1024)
		if not data:
			break
		idx1 = str(data).find(':')
		idx2 = str(data).find('_')
		val = int(str(data)[idx1+1:idx2])
		print val
		c.send(data)

	c.close()

if __name__ == '__main__':
	Main()
