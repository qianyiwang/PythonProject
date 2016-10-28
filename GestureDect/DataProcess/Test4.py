import socket
import pandas as pd
from scipy import signal
import numpy as np
import math
import matplotlib.pyplot as plt
gry_x = []
gry_x_abs = []
gry_abs = []

# declear features
gry_abs_peakNum = 0
gry_x_firstPeakVal = 0

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
                    gry_x.append(float(line[1]))
                    gry_x_abs.append(abs(float(line[1])))
                    gry_abs.append(math.sqrt(float(line[1])*float(line[1])+float(line[2])*float(line[2])+float(line[3])*float(line[3])))
                except ValueError:
                    continue
    # conn.send(data) #echo
conn.close()

peakind = signal.find_peaks_cwt(gry_abs, np.arange(.1,.2))
peakNum = 0
for p in peakind:
    if gry_abs[p]>=6.5:
        peakNum = peakNum + 1
gry_abs_peakNum = peakNum

peakind_2 = signal.find_peaks_cwt(gry_x_abs, np.arange(.1,.2))
if gry_x_abs[peakind_2[0]]>5:
    gry_x_firstPeakVal = gry_x[peakind_2[0]]

print gry_abs_peakNum
print gry_x_firstPeakVal
plt.plot(gry_x,'yo',gry_x,'k')
if gry_abs_peakNum <= 2 and gry_x_firstPeakVal < -6:
    print 'single outside'
elif gry_abs_peakNum <= 2 and gry_x_firstPeakVal > 6:
    print 'single inside'
elif gry_abs_peakNum > 2 and gry_x_firstPeakVal < -6:
    print 'double outside'
elif gry_abs_peakNum > 2 and gry_x_firstPeakVal > 6:
    print 'double inside'
else:
    print 'not a defined gesture'
plt.show()
