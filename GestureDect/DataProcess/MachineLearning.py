import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
# fileName1 = raw_input("Select single outside file: ")
# fileName2 = raw_input("Select single inside file: ")
fileName1 = 'single_outside_3'
fileName2 = 'single_inside_3'
single_outside_gry_x = []
single_outside_gry_y = []
single_outside_gry_z = []
single_outside_acc_x= []
single_outside_acc_y = []
single_outside_acc_z = []
single_outside_label = []
time_single_outside_acc = []
time_single_outside_gry = []
dT = []

# statistic features extraction
def calculateMean(arr):
    windowSize = 20
    res = []
    for i in range(0,len(arr[:-20])):
        mean = np.mean(arr[i:i+20])
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
        std = np.std(arr[i:i+20])
        res.append(std)
    return res

# single outside data
with open(fileName1+'_acc.txt') as fp:
    for line in fp:
        if "ACC complete" in line:
            continue
        elif line.count('_')==3:
            line = line[:-1]
            if(']' in line):
                line = line[:-1]
            arr = line.split('_')
            # print arr
            try:

                if(len(time_single_outside_acc)==0):
                    dT.append(0)
                else:
                    dT.append(float(arr[0])-time_single_outside_acc[-1])
                time_single_outside_acc.append(float(arr[0]))
                single_outside_acc_x.append(float(arr[1]))
                single_outside_acc_y.append(float(arr[2]))
                single_outside_acc_z.append(float(arr[3]))
                single_outside_label.append(-1)
            except ValueError:
                    continue

with open(fileName1+'_gyo.txt') as fp:
    for line in fp:
        if "GYO complete" in line:
            continue
        elif line.count('_')==3:
            line = line[:-1]
            if ']' in line:
                line = line[:-1]
            arr = line.split('_')
            try:
                time_single_outside_gry.append(float(arr[0]))
                single_outside_gry_x.append(float(arr[1]))
                single_outside_gry_y.append(float(arr[2]))
                single_outside_gry_z.append(float(arr[3]))
            except ValueError:
                    continue

# idx = len(single_outside_acc_x)-len(single_outside_gry_x)
# if idx>0:
#     single_outside = pd.DataFrame({'dT':dT[:-idx],'acc_x': single_outside_acc_x[:-idx],'acc_y': single_outside_acc_y[:-idx],
#         'acc_z': single_outside_acc_z[:-idx],'gry_x':single_outside_gry_x,
#         'gry_y':single_outside_gry_y,'gry_z':single_outside_gry_z,'label':single_outside_label[:-idx]})
# else:
#     single_outside = pd.DataFrame({'dT':dT,'acc_x': single_outside_acc_x,'acc_y': single_outside_acc_y,
#         'acc_z': single_outside_acc_z,'gry_x':single_outside_gry_x[:-idx],
#         'gry_y':single_outside_gry_y[:-idx],'gry_z':single_outside_gry_z[:-idx],'label':single_outside_label})
#
# single_outside = single_outside[single_outside.dT!=0]

acc_x_mean_singleOutside = calculateMean(single_outside_acc_x)
acc_y_mean_singleOutside = calculateMean(single_outside_acc_y)
acc_z_mean_singleOutside = calculateMean(single_outside_acc_z)
acc_x_max_singleOutside = calculateMax(single_outside_acc_x)
acc_y_max_singleOutside = calculateMax(single_outside_acc_y)
acc_z_max_singleOutside = calculateMax(single_outside_acc_z)
acc_x_min_singleOutside = calculateMin(single_outside_acc_x)
acc_y_min_singleOutside = calculateMin(single_outside_acc_y)
acc_z_min_singleOutside = calculateMin(single_outside_acc_z)
acc_x_std_singleOutside = calculateStd(single_outside_acc_x)
acc_y_std_singleOutside = calculateStd(single_outside_acc_y)
acc_z_std_singleOutside = calculateStd(single_outside_acc_z)

gry_x_mean_singleOutside = calculateMean(single_outside_gry_x)
gry_y_mean_singleOutside = calculateMean(single_outside_gry_y)
gry_z_mean_singleOutside = calculateMean(single_outside_gry_z)
gry_x_max_singleOutside = calculateMax(single_outside_gry_x)
gry_y_max_singleOutside = calculateMax(single_outside_gry_y)
gry_z_max_singleOutside = calculateMax(single_outside_gry_z)
gry_x_min_singleOutside = calculateMin(single_outside_gry_x)
gry_y_min_singleOutside = calculateMin(single_outside_gry_y)
gry_z_min_singleOutside = calculateMin(single_outside_gry_z)
gry_x_std_singleOutside = calculateStd(single_outside_gry_x)
gry_y_std_singleOutside = calculateStd(single_outside_gry_y)
gry_z_std_singleOutside = calculateStd(single_outside_gry_z)

idx = len(acc_x_mean_singleOutside)-len(gry_x_mean_singleOutside)
if idx>0:
    single_outside = pd.DataFrame({'dT':dT[:-idx-20],'acc_x_max': acc_x_max_singleOutside[:-idx],'acc_y_max': acc_y_max_singleOutside[:-idx],'acc_z_max': acc_z_max_singleOutside[:-idx],
        'acc_x_min': acc_x_min_singleOutside[:-idx],'acc_y_min':acc_y_min_singleOutside[:-idx],'acc_z_min':acc_z_min_singleOutside[:-idx],
        'acc_x_mean': acc_x_mean_singleOutside[:-idx], 'acc_y_mean': acc_y_mean_singleOutside[:-idx],'acc_z_mean': acc_z_mean_singleOutside[:-idx],
        'acc_x_std': acc_x_std_singleOutside[:-idx], 'acc_y_std': acc_y_std_singleOutside[:-idx], 'acc_z_std': acc_z_std_singleOutside[:-idx],
        'gry_x_min': gry_x_min_singleOutside,'gry_y_min': gry_y_min_singleOutside,'gry_z_min': gry_z_min_singleOutside,
        'gry_x_max': gry_x_max_singleOutside,'gry_y_max': gry_y_max_singleOutside,'gry_z_max': gry_z_max_singleOutside,
        'gry_x_mean': gry_x_mean_singleOutside,'gry_y_mean': gry_y_mean_singleOutside,'gry_z_mean':gry_z_mean_singleOutside,
        'gry_x_std': gry_x_std_singleOutside,'gry_y_std': gry_y_std_singleOutside,'gry_z_std': gry_z_std_singleOutside,
        'label':single_outside_label[:-idx-20]})
else:
    single_outside = pd.DataFrame({'dT':dT[:-20],'acc_x_max': acc_x_max_singleOutside,'acc_y_max': acc_y_max_singleOutside,'acc_z_max': acc_z_max_singleOutside,
        'acc_x_min': acc_x_min_singleOutside,'acc_y_min':acc_y_min_singleOutside,'acc_z_min':acc_z_min_singleOutside,
        'acc_x_mean': acc_x_mean_singleOutside, 'acc_y_mean': acc_y_mean_singleOutside,'acc_z_mean': acc_z_mean_singleOutside,
        'acc_x_std': acc_x_std_singleOutside, 'acc_y_std': acc_y_std_singleOutside, 'acc_z_std': acc_z_std_singleOutside,
        'gry_x_min': gry_x_min_singleOutside[:-idx],'gry_y_min': gry_y_min_singleOutside[:-idx],'gry_z_min': gry_z_min_singleOutside[:-idx],
        'gry_x_max': gry_x_max_singleOutside[:-idx],'gry_y_max': gry_y_max_singleOutside[:-idx],'gry_z_max': gry_z_max_singleOutside[:-idx],
        'gry_x_mean': gry_x_mean_singleOutside[:-idx],'gry_y_mean': gry_y_mean_singleOutside[:-idx],'gry_z_mean':gry_z_mean_singleOutside[:-idx],
        'gry_x_std': gry_x_std_singleOutside[:-idx],'gry_y_std': gry_y_std_singleOutside[:-idx],'gry_z_std': gry_z_std_singleOutside[:-idx],
        'label':single_outside_label[:-20]})

single_outside = single_outside[single_outside.dT!=0]

# single inside data
single_inside_gry_x = []
single_inside_gry_y = []
single_inside_gry_z = []
single_inside_acc_x= []
single_inside_acc_y = []
single_inside_acc_z = []
single_inside_label = []
time_single_inside_acc = []
dT2 = []

with open(fileName2+'_acc.txt') as fp:
    for line in fp:
        if "ACC complete" in line:
            continue
        elif line.count('_')==3:
            line = line[:-1]
            if(']' in line):
                line = line[:-1]
            arr = line.split('_')
            # print arr
            try:

                if(len(time_single_inside_acc)==0):
                    dT2.append(0)
                else:
                    dT2.append(float(arr[0])-time_single_inside_acc[-1])
                time_single_inside_acc.append(float(arr[0]))
                single_inside_acc_x.append(float(arr[1]))
                single_inside_acc_y.append(float(arr[2]))
                single_inside_acc_z.append(float(arr[3]))
                single_inside_label.append(1)
            except ValueError:
                    continue

with open(fileName2+'_gyo.txt') as fp:
    for line in fp:
        if "GYO complete" in line:
            continue
        elif line.count('_')==3:
            line = line[:-1]
            if ']' in line:
                line = line[:-1]
            arr = line.split('_')
            try:
                single_inside_gry_x.append(float(arr[1]))
                single_inside_gry_y.append(float(arr[2]))
                single_inside_gry_z.append(float(arr[3]))
            except ValueError:
                    continue

# idx2 = len(single_inside_acc_x)-len(single_inside_gry_x)
# if idx2>0:
#     single_inside = pd.DataFrame({'dT':dT2[:-idx2],'acc_x': single_inside_acc_x[:-idx2],'acc_y': single_inside_acc_y[:-idx2],
#         'acc_z': single_inside_acc_z[:-idx2],'gry_x':single_inside_gry_x,
#         'gry_y':single_inside_gry_y,'gry_z':single_inside_gry_z,'label':single_inside_label[:-idx2]})
# else:
#     single_inside = pd.DataFrame({'dT':dT2,'acc_x': single_inside_acc_x,'acc_y': single_inside_acc_y,
#         'acc_z': single_inside_acc_z,'gry_x':single_inside_gry_x[:-idx2],
#         'gry_y':single_inside_gry_y[:-idx2],'gry_z':single_inside_gry_z[:-idx2],'label':single_inside_label})
#
# single_inside = single_inside[single_inside.dT!=0]

acc_x_mean_singleInside = calculateMean(single_inside_acc_x)
acc_y_mean_singleInside = calculateMean(single_inside_acc_y)
acc_z_mean_singleInside = calculateMean(single_inside_acc_z)
acc_x_max_singleInside = calculateMax(single_inside_acc_x)
acc_y_max_singleInside = calculateMax(single_inside_acc_y)
acc_z_max_singleInside = calculateMax(single_inside_acc_z)
acc_x_min_singleInside = calculateMin(single_inside_acc_x)
acc_y_min_singleInside = calculateMin(single_inside_acc_y)
acc_z_min_singleInside = calculateMin(single_inside_acc_z)
acc_x_std_singleInside = calculateStd(single_inside_acc_x)
acc_y_std_singleInside = calculateStd(single_inside_acc_y)
acc_z_std_singleInside = calculateStd(single_inside_acc_z)

gry_x_mean_singleInside = calculateMean(single_inside_gry_x)
gry_y_mean_singleInside = calculateMean(single_inside_gry_y)
gry_z_mean_singleInside = calculateMean(single_inside_gry_z)
gry_x_max_singleInside = calculateMax(single_inside_gry_x)
gry_y_max_singleInside = calculateMax(single_inside_gry_y)
gry_z_max_singleInside = calculateMax(single_inside_gry_z)
gry_x_min_singleInside = calculateMin(single_inside_gry_x)
gry_y_min_singleInside = calculateMin(single_inside_gry_y)
gry_z_min_singleInside = calculateMin(single_inside_gry_z)
gry_x_std_singleInside = calculateStd(single_inside_gry_x)
gry_y_std_singleInside = calculateStd(single_inside_gry_y)
gry_z_std_singleInside = calculateStd(single_inside_gry_z)

idx = len(acc_x_mean_singleInside)-len(gry_x_mean_singleInside)

if idx>0:
    single_inside = pd.DataFrame({'dT':dT2[:-idx-20],'acc_x_max': acc_x_max_singleInside[:-idx],'acc_y_max': acc_y_max_singleInside[:-idx],'acc_z_max': acc_z_max_singleInside[:-idx],
        'acc_x_min': acc_x_min_singleInside[:-idx],'acc_y_min':acc_y_min_singleInside[:-idx],'acc_z_min':acc_z_min_singleInside[:-idx],
        'acc_x_mean': acc_x_mean_singleInside[:-idx], 'acc_y_mean': acc_y_mean_singleInside[:-idx],'acc_z_mean': acc_z_mean_singleInside[:-idx],
        'acc_x_std': acc_x_std_singleInside[:-idx], 'acc_y_std': acc_y_std_singleInside[:-idx], 'acc_z_std': acc_z_std_singleInside[:-idx],
        'gry_x_min': gry_x_min_singleInside,'gry_y_min': gry_y_min_singleInside,'gry_z_min': gry_z_min_singleInside,
        'gry_x_max': gry_x_max_singleInside,'gry_y_max': gry_y_max_singleInside,'gry_z_max': gry_z_max_singleInside,
        'gry_x_mean': gry_x_mean_singleInside,'gry_y_mean': gry_y_mean_singleInside,'gry_z_mean':gry_z_mean_singleInside,
        'gry_x_std': gry_x_std_singleInside,'gry_y_std': gry_y_std_singleInside,'gry_z_std': gry_z_std_singleInside,
        'label':single_inside_label[:-idx-20]})
else:
    single_inside = pd.DataFrame({'dT':dT2[:-20],'acc_x_max': acc_x_max_singleInside,'acc_y_max': acc_y_max_singleInside,'acc_z_max': acc_z_max_singleInside,
        'acc_x_min': acc_x_min_singleInside,'acc_y_min':acc_y_min_singleInside,'acc_z_min':acc_z_min_singleInside,
        'acc_x_mean': acc_x_mean_singleInside, 'acc_y_mean': acc_y_mean_singleInside,'acc_z_mean': acc_z_mean_singleInside,
        'acc_x_std': acc_x_std_singleInside, 'acc_y_std': acc_y_std_singleInside, 'acc_z_std': acc_z_std_singleInside,
        'gry_x_min': gry_x_min_singleInside[:-idx],'gry_y_min': gry_y_min_singleInside[:-idx],'gry_z_min': gry_z_min_singleInside[:-idx],
        'gry_x_max': gry_x_max_singleInside[:-idx],'gry_y_max': gry_y_max_singleInside[:-idx],'gry_z_max': gry_z_max_singleInside[:-idx],
        'gry_x_mean': gry_x_mean_singleInside[:-idx],'gry_y_mean': gry_y_mean_singleInside[:-idx],'gry_z_mean':gry_z_mean_singleInside[:-idx],
        'gry_x_std': gry_x_std_singleInside[:-idx],'gry_y_std': gry_y_std_singleInside[:-idx],'gry_z_std': gry_z_std_singleInside[:-idx],
        'label':single_inside_label[:-20]})

single_inside = single_inside[single_inside.dT!=0]
frames = [single_outside, single_inside]
results = pd.concat(frames)
x = np.array(results.drop(['label'],1))
# x = preprocessing.scale(x)
y = np.array(results['label'])

# machine learning
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
# clf = LinearRegression()
clf = svm.SVR(kernel='rbf') # rbf: radial basis function
clf.fit(x_train, y_train)
accuracy1 = clf.score(x_test, y_test)
print 'SVM accuracy: ',accuracy1
# print clf.predict(x_test)
