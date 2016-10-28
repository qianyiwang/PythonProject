import socket
import pandas as pd
from scipy import signal
import numpy as np
from sklearn import cross_validation
import pickle
from sklearn import tree

gry_x = []
gry_y = []
gry_z = []
acc_x= []
acc_y = []
acc_z = []
label = []
time_acc = []
time_gry = []

# declear features
gry_x_max = []
gry_x_min = []
gry_x_peakNum = []
acc_z_max = []
acc_z_min = []
acc_z_peakNum = []

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
    if('ACC' in data):
        accList = data.split(',')
        for l in accList:
            if '[ACC' not in l and l.count('_')==3:
                line = l.split('_')
                try:

                    time_acc.append(float(line[0].replace(' ','')))
                    acc_x.append(float(line[1]))
                    acc_y.append(float(line[2]))
                    acc_z.append(float(line[3].replace(']','')))
                except ValueError:
                    continue

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
                except ValueError:
                    continue
    # conn.send(data) #echo
conn.close()

acc_z_max.append(max(acc_z))
acc_z_min.append(min(acc_z))
acc_z_peakNum.append(len(signal.find_peaks_cwt(acc_z, np.arange(0.1,1))))
gry_x_max.append(max(gry_x))
gry_x_min.append(min(gry_x))
gry_x_peakNum.append(len(signal.find_peaks_cwt(gry_x, np.arange(0.1,1))))

matrix = pd.DataFrame({'acc_z_max': acc_z_max,'acc_z_min':acc_z_min, 'acc_z_peakNum': acc_z_peakNum,
    'gry_x_min': gry_x_min,'gry_x_max': gry_x_max, 'gry_x_peakNum': gry_x_peakNum})

x = np.array(matrix)
pickle_in = open('gesture_recognize_randomForest.pickle','rb')
clf = pickle.load(pickle_in)
res = clf.predict(x)
print res
