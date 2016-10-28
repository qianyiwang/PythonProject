import matplotlib.pyplot as plt
import numpy
from scipy import signal
import math
import socket
ipAddress = '0.0.0.0'
port = 1025
buffer_size = 2048 # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipAddress, port))
s.listen(1)
conn, addr = s.accept()

gry_x = []
gry_y = []
gry_z = []
acc_x= []
acc_y = []
acc_z = []
acc_z_abs = []
acc_abs = []
gry_abs = []

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
                    gry_x.append(float(line[1]))
                    gry_y.append(float(line[2]))
                    gry_z.append(float(line[3]))
                    gry_abs.append(math.sqrt(float(line[1])*float(line[1])+float(line[2])*float(line[2])+float(line[3])*float(line[3])))
                except ValueError:
                        continue

    if('ACC' in data):
        accList = data.split(',')
        for l in accList:
            if '[ACC' not in l and l.count('_')==3:
                line = l.split('_')
                try:
                    acc_x.append(float(line[1]))
                    acc_y.append(float(line[2]))
                    acc_z.append(float(line[3]))
                    acc_z_abs.append(abs(float(line[3])))
                    acc_abs.append(math.sqrt(float(line[1])*float(line[1])+float(line[2])*float(line[2])+float(line[3])*float(line[3])))
                except ValueError:
                        continue

plt.figure('ACC')
plt.subplot(131)
plt.plot(acc_x,'yo',acc_x,'k')
# peakind = signal.find_peaks_cwt(acc_x, numpy.arange(.1,1))
# for p in peakind:
#     plt.plot(time_acc[p], acc_x[p],'ro')

plt.subplot(132)
plt.plot(acc_z_abs,'yo',acc_z_abs,'k')
# peakind = signal.find_peaks_cwt(acc_y, numpy.arange(.1,1))
# for p in peakind:
#     plt.plot(time_acc[p], acc_y[p],'ro')

plt.subplot(133)
plt.plot(acc_z,'yo',acc_z,'k')
# peakind = signal.find_peaks_cwt(acc_z, numpy.arange(.1,1))
# for p in peakind:
#     plt.plot(time_acc[p], acc_z[p],'ro')

plt.figure('GYO')
plt.subplot(131)
plt.plot(gry_x,'yo',gry_x,'k')
# peakind = signal.find_peaks_cwt(gry_x, numpy.arange(.1,1))
# for p in peakind:
#     plt.plot(time_gry[p], gry_x[p],'ro')

plt.subplot(132)
plt.plot(gry_y,'yo',gry_y,'k')
# peakind = signal.find_peaks_cwt(gry_y, numpy.arange(.1,1))

plt.subplot(133)
plt.plot(gry_z,'yo',gry_z,'k')
# peakind = signal.find_peaks_cwt(gry_z, numpy.arange(.1,1))
# for p in peakind:
#     plt.plot(time_gry[p], gry_z[p],'ro')

plt.figure('ACC and GRY')
plt.subplot(1,2,1)
plt.plot(acc_abs,'yo',acc_abs,'k')
plt.subplot(1,2,2)
plt.plot(gry_abs,'yo',gry_abs,'k')
# peakind = signal.find_peaks_cwt(gry, numpy.arange(.1,.2))
# for p in peakind:
#     if gry[p]>=6:
#         plt.plot(time_gry[p], gry[p],'ro')

plt.show()
