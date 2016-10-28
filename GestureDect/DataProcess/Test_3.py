import socket
import pandas as pd
from scipy import signal
import numpy as np
from sklearn import cross_validation
import pickle
from sklearn import tree
import math

gry_x = []
gry_y = []
gry_z = []
gry_abs = []
time_gry = []

# declear features
gry_x_max = []
gry_x_min = []
gry_abs_peakNum = []

ipAddress = '0.0.0.0'
port = 1025
buffer_size = 2048 # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipAddress, port))
s.listen(1)
conn, addr = s.accept()

print 'Connection address:', addr

# reading data via TcpIP
while 1:
    data = conn.recv(buffer_size)
    if not data:
        break

    if('GYO' in data):
        accList = data.split(',')
        for l in accList:
            if '[GYO' not in l and l.count('_')==3:
                line = l.split('_')
                try:

                    time_gry.append(float(line[0].replace(' ','')))
                    gry_x.append(float(line[1]))
                    gry_y.append(float(line[2]))
                    gry_z.append(float(line[3].replace(']','')))
                    gry_abs.append(math.sqrt(float(line[1])*float(line[1])+float(line[2])*float(line[2])+float(line[3])*float(line[3])))
                except ValueError:
                    continue
    # conn.send(data) #echo
conn.close()
gry_x_max.append(max(gry_x))
gry_x_min.append(min(gry_x))
peakind = signal.find_peaks_cwt(gry_abs, np.arange(.1,.2))
peakNum = 0
for p in peakind:
    if gry_abs[p]>=6.5:
        peakNum = peakNum + 1
gry_abs_peakNum.append(peakNum)
matrix = pd.DataFrame({'gry_x_min': gry_x_min,'gry_x_max': gry_x_max, 'gry_abs_peakNum': gry_abs_peakNum})
print matrix
x = np.array(matrix)
pickle_in = open('RandomForest1.pickle','rb')
clf = pickle.load(pickle_in)
res = clf.predict(x)
print res
