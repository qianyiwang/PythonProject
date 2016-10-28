import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import socket
from multiprocessing import Process, Queue

def tcpSocket(q):

    print "tcpSocket"

    host = '0.0.0.0'
    port = 1025

    val = []

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
        val.append(int(str(data)[idx1 + 1:idx2]))
        q.put(val)
        c.send(data)


def myPlot(q):
    print "myPlot"
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    def _update_plot(i):
        ys = q.get()
        xs = []
        for i in range(0,len(ys)):
            xs.append(i+1)
        ax1.clear()
        ax1.plot(xs, ys)
    ani = animation.FuncAnimation(fig, _update_plot, interval=1000)
    plt.show()

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=tcpSocket, args=(q,))
    p1.start()
    p1.join()
    p2 = Process(target=myPlot, args=(q,))
    p2.start()
    p2.join()
    
    

