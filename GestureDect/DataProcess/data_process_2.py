import matplotlib.pyplot as plt

fileName = 'interval_data'
single_out_acc_y = []
single_in_acc_y = []
double_out_acc_y = []
double_in_acc_y = []

def findPeak(arr):
    res = []
    for i in range(1,len(arr)):
        if i<len(arr)-1:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                res.append(i)
    return res

def findValley(arr):
    res = arr.index(min(arr))
    return res

with open(fileName+'.txt') as fp:
    for line in fp:
        if 'V' in line:
            p = line.index('V')
            singleName = line[p+2:p+4]
            if singleName=='so':
                single_out_acc_y.append(float(line[p+6:]))
            elif singleName == 'si':
                single_in_acc_y.append(float(line[p+6:]))
            elif singleName == 'do':
                double_out_acc_y.append(float(line[p+6:]))
            elif singleName == 'di':
                double_in_acc_y.append(float(line[p+6:]))

plt.subplot(221)
plt.plot(single_out_acc_y,'r')
# peakId = findPeak(single_out_acc_y)
# for p in peakId:
#     plt.plot(p,single_out_acc_y[p],'ro')
valleyId = findValley(single_out_acc_y)
plt.plot(valleyId,single_out_acc_y[valleyId],'bo')

plt.subplot(222)
plt.plot(single_in_acc_y,'r')
# peakId = findPeak(single_in_acc_y)
# for p in peakId:
#     plt.plot(p,single_in_acc_y[p],'ro')
valleyId = findValley(single_in_acc_y)
plt.plot(valleyId,single_in_acc_y[valleyId],'bo')

plt.subplot(223)
plt.plot(double_out_acc_y,'r')
# peakId = findPeak(double_out_acc_y)
# for p in peakId:
#     plt.plot(p,double_out_acc_y[p],'ro')
valleyId = findValley(double_out_acc_y)
plt.plot(valleyId,double_out_acc_y[valleyId],'bo')

plt.subplot(224)
plt.plot(double_in_acc_y,'r')
# peakId = findPeak(double_in_acc_y)
# for p in peakId:
#     plt.plot(p,double_in_acc_y[p],'ro')
valleyId = findValley(double_in_acc_y)
plt.plot(valleyId,double_in_acc_y[valleyId],'bo')

plt.show()
