import socket
import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import pickle

gry_x = []
gry_y = []
gry_z = []
acc_x= []
acc_y = []
acc_z = []
label = []
time_acc = []
time_gry = []
dT = []
ipAddress = '0.0.0.0'
port = 1025
buffer_size = 2048 # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipAddress, port))
s.listen(1)
conn, addr = s.accept()

def calculateMean(arr):
    windowSize = 10
    res = []
    for i in range(0,len(arr[:-10])):
        mean = np.mean(arr[i:i+10])
        res.append(mean)
    return res

def calculateMax(arr):
    windowSize = 10
    res = []
    for i in range(0,len(arr[:-10])):
        myMax = max(arr[i:i+10])
        res.append(myMax)
    return res

def calculateMin(arr):
    windowSize = 10
    res = []
    for i in range(0,len(arr[:-10])):
        myMin = min(arr[i:i+10])
        res.append(myMin)
    return res

def calculateStd(arr):
    windowSize = 10
    res = []
    for i in range(0,len(arr[:-10])):
        std = np.std(arr[i:i+10])
        res.append(std)
    return res

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
                    if(len(time_acc)==0):
                        dT.append(0)
                    else:
                        dT.append(float(line[0].replace(' ',''))-time_acc[-1])
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

# extraction features
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

lenArray = [len(acc_x_mean), len(acc_x_max), len(acc_x_min), len(acc_x_std),
            len(acc_y_mean), len(acc_y_max), len(acc_y_min), len(acc_y_std),
            len(acc_z_mean), len(acc_z_max), len(acc_z_min), len(acc_z_std),
            len(gry_x_mean), len(gry_x_min), len(gry_x_max), len(gry_x_std),
            len(gry_y_mean), len(gry_y_min), len(gry_y_max), len(gry_y_std),
            len(gry_z_mean), len(gry_z_min), len(gry_z_max), len(gry_z_std)]
minLen = min(lenArray)

matrix = pd.DataFrame({'dT':dT[:minLen],'acc_x_max': acc_x_max[:minLen],'acc_y_max': acc_y_max[:minLen],'acc_z_max': acc_z_max[:minLen],
    'acc_x_min': acc_x_min[:minLen],'acc_y_min':acc_y_min[:minLen],'acc_z_min':acc_z_min[:minLen],
    'acc_x_mean': acc_x_mean[:minLen], 'acc_y_mean': acc_y_mean[:minLen],'acc_z_mean': acc_z_mean[:minLen],
    'acc_x_std': acc_x_std[:minLen], 'acc_y_std': acc_y_std[:minLen], 'acc_z_std': acc_z_std[:minLen],
    'gry_x_min': gry_x_min[:minLen],'gry_y_min': gry_y_min[:minLen],'gry_z_min': gry_z_min[:minLen],
    'gry_x_max': gry_x_max[:minLen],'gry_y_max': gry_y_max[:minLen],'gry_z_max': gry_z_max[:minLen],
    'gry_x_mean': gry_x_mean[:minLen],'gry_y_mean': gry_y_mean[:minLen],'gry_z_mean':gry_z_mean[:minLen],
    'gry_x_std': gry_x_std[:minLen],'gry_y_std': gry_y_std[:minLen],'gry_z_std': gry_z_std[:minLen]})

# idx = len(acc_x_mean)-len(gry_x_mean)
#
# print idx
# print len(acc_x_std)
# print len(gry_x_std)
#
# if idx>0:
#     matrix = pd.DataFrame({'dT':dT[:-idx-10],'acc_x_max': acc_x_max[:-idx],'acc_y_max': acc_y_max[:-idx],'acc_z_max': acc_z_max[:-idx],
#         'acc_x_min': acc_x_min[:-idx],'acc_y_min':acc_y_min[:-idx],'acc_z_min':acc_z_min[:-idx],
#         'acc_x_mean': acc_x_mean[:-idx], 'acc_y_mean': acc_y_mean[:-idx],'acc_z_mean': acc_z_mean[:-idx],
#         'acc_x_std': acc_x_std[:-idx], 'acc_y_std': acc_y_std[:-idx], 'acc_z_std': acc_z_std[:-idx],
#         'gry_x_min': gry_x_min,'gry_y_min': gry_y_min,'gry_z_min': gry_z_min,
#         'gry_x_max': gry_x_max,'gry_y_max': gry_y_max,'gry_z_max': gry_z_max,
#         'gry_x_mean': gry_x_mean,'gry_y_mean': gry_y_mean,'gry_z_mean':gry_z_mean,
#         'gry_x_std': gry_x_std,'gry_y_std': gry_y_std,'gry_z_std': gry_z_std})
# elif idx < 0:
#     matrix = pd.DataFrame({'dT':dT[:-10],'acc_x_max': acc_x_max,'acc_y_max': acc_y_max,'acc_z_max': acc_z_max,
#         'acc_x_min': acc_x_min,'acc_y_min':acc_y_min,'acc_z_min':acc_z_min,
#         'acc_x_mean': acc_x_mean, 'acc_y_mean': acc_y_mean,'acc_z_mean': acc_z_mean,
#         'acc_x_std': acc_x_std, 'acc_y_std': acc_y_std, 'acc_z_std': acc_z_std,
#         'gry_x_min': gry_x_min[:+idx],'gry_y_min': gry_y_min[:+idx],'gry_z_min': gry_z_min[:+idx],
#         'gry_x_max': gry_x_max[:+idx],'gry_y_max': gry_y_max[:+idx],'gry_z_max': gry_z_max[:+idx],
#         'gry_x_mean': gry_x_mean[:+idx],'gry_y_mean': gry_y_mean[:+idx],'gry_z_mean':gry_z_mean[:+idx],
#         'gry_x_std': gry_x_std[:+idx],'gry_y_std': gry_y_std[:+idx],'gry_z_std': gry_z_std[:+idx]})
#
# else:
#     matrix = pd.DataFrame({'dT':dT[:-10],'acc_x_max': acc_x_max,'acc_y_max': acc_y_max,'acc_z_max': acc_z_max,
#         'acc_x_min': acc_x_min,'acc_y_min':acc_y_min,'acc_z_min':acc_z_min,
#         'acc_x_mean': acc_x_mean, 'acc_y_mean': acc_y_mean,'acc_z_mean': acc_z_mean,
#         'acc_x_std': acc_x_std, 'acc_y_std': acc_y_std, 'acc_z_std': acc_z_std,
#         'gry_x_min': gry_x_min,'gry_y_min': gry_y_min,'gry_z_min': gry_z_min,
#         'gry_x_max': gry_x_max,'gry_y_max': gry_y_max,'gry_z_max': gry_z_max,
#         'gry_x_mean': gry_x_mean,'gry_y_mean': gry_y_mean,'gry_z_mean':gry_z_mean,
#         'gry_x_std': gry_x_std,'gry_y_std': gry_y_std,'gry_z_std': gry_z_std})

matrix = matrix[matrix.dT!=0]
x = np.array(matrix)
x = preprocessing.scale(x)
pickle_in = open('gesture_recognizeSVM_SVC.pickle','rb')
clf = pickle.load(pickle_in)
res = clf.predict(x)
print res
so = si = do = di = 0
for r in res:
    if r==1:
        so = so+1
    elif r==2:
        si = si+1
    elif r==3:
        do = do+1
    elif r==4:
        di = di+1
myList = [so,si,do,di]
print myList
if myList.index(max(myList))==0:
    print 'single outside'
elif myList.index(max(myList))==1:
    print 'single inside'
elif myList.index(max(myList))==2:
    print 'double outside'
elif myList.index(max(myList))==3:
    print 'double inside'
