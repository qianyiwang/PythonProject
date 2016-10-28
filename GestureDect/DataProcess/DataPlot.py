import matplotlib.pyplot as plt
import numpy
from scipy import signal
import math
fileName = 'double_inside'#raw_input("Select file: ")
stop1 = []
stop2 = []
gry_x = []
gry_y = []
gry_z = []
acc_x= []
acc_y = []
acc_z = []
acc = []
gry = []
time_acc = []
time_gry = []
x = -1
y = -1

with open(fileName+'_acc.txt') as fp:
    for line in fp:
        if "ACC complete" in line:
            stop1.append(x)
        elif line.count('_')==3:
            x = x+1
            line = line[:-1]
            if(']' in line):
                line = line[:-1]
            arr = line.split('_')
            # print arr
            try:
                time_acc.append(float(arr[0]))
                acc_x.append(float(arr[1]))
                acc_y.append(float(arr[2]))
                acc_z.append(float(arr[3]))
                acc.append(math.sqrt(float(arr[1])*float(arr[1])+float(arr[2])*float(arr[2])+float(arr[3])*float(arr[3])))
            except ValueError:
                    continue

with open(fileName+'_gyo.txt') as fp:
    for line in fp:
        if "GYO complete" in line:
            stop2.append(y)
        elif line.count('_')==3:
            y = y+1
            line = line[:-1]
            if ']' in line:
                line = line[:-1]
            arr = line.split('_')
            try:
                time_gry.append(float(arr[0]))
                gry_x.append(float(arr[1]))
                gry_y.append(float(arr[2]))
                gry_z.append(float(arr[3]))
                gry.append(math.sqrt(float(arr[1])*float(arr[1])+float(arr[2])*float(arr[2])+float(arr[3])*float(arr[3])))
            except ValueError:
                    continue

# statistic features
def calculateMean(arr):
    windowSize = 20
    res = []
    for i in range(0,len(arr[:-20])):
        mean = numpy.mean(arr[i:i+20])
        res.append(mean)
    return res

def calculateMax(arr):
    windowSize = 20
    res = []
    for i in range(0,len(arr[:-20])):
        myMax = max(arr[i:i+20])
        res.append(myMax)
    return res

def calculateMin(arr):
    windowSize = 20
    res = []
    for i in range(0,len(arr[:-20])):
        myMin = min(arr[i:i+20])
        res.append(myMin)
    return res

def calculateStd(arr):
    windowSize = 20
    res = []
    for i in range(0,len(arr[:-20])):
        std = numpy.std(arr[i:i+20])
        res.append(std)
    return res

acc_x_mean = calculateMean(acc_x)
acc_y_mean = calculateMean(acc_y)
acc_z_mean = calculateMean(acc_z)
acc_x_max = calculateMax(acc_x)
acc_y_max = calculateMax(acc_y)
acc_z_max = calculateMax(acc_z)
acc_x_min = calculateMin(acc_x)
acc_y_min = calculateMin(acc_y)
acc_z_min = calculateMin(acc_z)
acc_x_std = calculateStd(acc_x)
acc_y_std = calculateStd(acc_y)
acc_z_std = calculateStd(acc_z)

gry_x_mean = calculateMean(gry_x)
gry_y_mean = calculateMean(gry_y)
gry_z_mean = calculateMean(gry_z)
gry_x_max = calculateMax(gry_x)
gry_y_max = calculateMax(gry_y)
gry_z_max = calculateMax(gry_z)
gry_x_min = calculateMin(gry_x)
gry_y_min = calculateMin(gry_y)
gry_z_min = calculateMin(gry_z)
gry_x_std = calculateStd(gry_x)
gry_y_std = calculateStd(gry_y)
gry_z_std = calculateStd(gry_z)

plt.figure('ACC')
plt.subplot(131)
plt.plot(time_acc, acc_x,'yo',time_acc,acc_x,'k')
peakind = signal.find_peaks_cwt(acc_x, numpy.arange(.1,1))
for p in peakind:
    plt.plot(time_acc[p], acc_x[p],'ro')
for s in stop1:
    plt.plot((time_acc[s],time_acc[s]),(min(acc_x),max(acc_x)),'r--')

plt.subplot(132)
plt.plot(time_acc,acc_y,'yo',time_acc,acc_y,'k')
peakind = signal.find_peaks_cwt(acc_y, numpy.arange(.1,1))
for p in peakind:
    plt.plot(time_acc[p], acc_y[p],'ro')
for s in stop1:
    plt.plot((time_acc[s],time_acc[s]),(min(acc_y),max(acc_y)),'r--')

plt.subplot(133)
plt.plot(time_acc,acc_z,'yo',time_acc,acc_z,'k')
peakind = signal.find_peaks_cwt(acc_z, numpy.arange(.1,1))
for p in peakind:
    plt.plot(time_acc[p], acc_z[p],'ro')
for s in stop1:
    plt.plot((time_acc[s],time_acc[s]),(min(acc_z),max(acc_z)),'r--')

plt.figure('GYO')
plt.subplot(131)
plt.plot(time_gry,gry_x,'yo',time_gry,gry_x,'k')
peakind = signal.find_peaks_cwt(gry_x, numpy.arange(.1,1))
for p in peakind:
    plt.plot(time_gry[p], gry_x[p],'ro')
for s in stop2:
    plt.plot((time_gry[s],time_gry[s]),(min(gry_x),max(gry_x)),'r--')

plt.subplot(132)
plt.plot(time_gry,gry_y,'yo',time_gry,gry_y,'k')
peakind = signal.find_peaks_cwt(gry_y, numpy.arange(.1,1))
for p in peakind:
    plt.plot(time_gry[p], gry_y[p],'ro')
for s in stop2:
    plt.plot((time_gry[s],time_gry[s]),(min(gry_y),max(gry_y)),'r--')

plt.subplot(133)
plt.plot(time_gry,gry_z,'yo',time_gry,gry_z,'k')
peakind = signal.find_peaks_cwt(gry_z, numpy.arange(.1,1))
for p in peakind:
    plt.plot(time_gry[p], gry_z[p],'ro')
for s in stop2:
    plt.plot((time_gry[s],time_gry[s]),(min(gry_z),max(gry_z)),'r--')

plt.figure('ACC and GRY')
plt.subplot(1,2,1)
plt.plot(time_acc,acc,'yo',time_acc,acc,'k')
plt.subplot(1,2,2)
plt.plot(time_gry,gry,'yo',time_gry,gry,'k')
peakind = signal.find_peaks_cwt(gry, numpy.arange(.1,.2))
for p in peakind:
    if gry[p]>=6:
        plt.plot(time_gry[p], gry[p],'ro')

# plt.figure('ACC X Feature')
# plt.subplot(4,1,1)
# plt.plot(time_acc[:-20],acc_x_mean)
#
# plt.subplot(4,1,2)
# plt.plot(time_acc[:-20],acc_x_max)
#
# plt.subplot(4,1,3)
# plt.plot(time_acc[:-20],acc_x_min)
#
# plt.subplot(4,1,4)
# plt.plot(time_acc[:-20],acc_x_std)
#
# plt.figure('ACC Y Feature')
# plt.subplot(4,1,1)
# plt.plot(time_acc[:-20],acc_y_mean)
#
# plt.subplot(4,1,2)
# plt.plot(time_acc[:-20],acc_y_max)
#
# plt.subplot(4,1,3)
# plt.plot(time_acc[:-20],acc_y_min)
#
# plt.subplot(4,1,4)
# plt.plot(time_acc[:-20],acc_y_std)
#
# plt.figure('ACC Z Feature')
# plt.subplot(4,1,1)
# plt.plot(time_acc[:-20],acc_z_mean)
#
# plt.subplot(4,1,2)
# plt.plot(time_acc[:-20],acc_z_max)
#
# plt.subplot(4,1,3)
# plt.plot(time_acc[:-20],acc_z_min)
#
# plt.subplot(4,1,4)
# plt.plot(time_acc[:-20],acc_z_std)

plt.show()
