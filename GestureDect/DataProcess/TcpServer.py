#!/usr/bin/env python
import socket
accList = []
ipAddress = '0.0.0.0'
port = 1025
buffer_size = 2048 # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipAddress, port))
s.listen(1)
fileName = raw_input("please give a file name: ")
f1 = open(fileName+'_acc.txt','w')
f2 = open(fileName+'_gyo.txt','w')

conn, addr = s.accept()
print 'Connection address:', addr

while 1:
    data = conn.recv(buffer_size)
    if not data:
        break
    if('ACC' in data):
        accList = data.split(',')
        for l in accList:
            if '[ACC' not in l:
                # line = l.split('_')
                print l
                f1.write(l+'\n') # python will convert \n to os.linesep
        print 'ACC complete'
        f1.write('ACC complete'+'\n')
    elif('GYO' in data):
        accList = data.split(',')
        for l in accList:
            if '[GYO' not in l:
                # line = l.split('_')
                print l
                f2.write(l+'\n') # python will convert \n to os.linesep
        print 'GYO complete'
        f2.write('GYO complete'+'\n')
    conn.send(data) #echo

conn.close()
f.close()
