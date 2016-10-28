import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm, ensemble
from sklearn.linear_model import LinearRegression
import pickle

# from sklearn.multiclass import OneVsRestClassifier
# from sklearn.svm import SVC
# from sklearn.svm import LinearSVC

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

for f in range(0,4):
    if f == 0:
        fileName = 'single_outside_5'
    elif f==1:
        fileName = 'single_inside_5'
    elif f == 2:
        fileName = 'double_outside_5'
    elif f==3:
        fileName = 'double_inside_5'

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

    with open(fileName+'_acc.txt') as fp:
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

                    if(len(time_acc)==0):
                        dT.append(0)
                    else:
                        dT.append(float(arr[0])-time_acc[-1])
                    time_acc.append(float(arr[0]))
                    acc_x.append(float(arr[1]))
                    acc_y.append(float(arr[2]))
                    acc_z.append(float(arr[3]))
                    if f == 0:
                        label.append(1)

                    elif f==1:
                        label.append(2)
                    elif f==2:
                        label.append(3)
                    elif f==3:
                        label.append(4)
                except ValueError:
                        continue

    with open(fileName+'_gyo.txt') as fp:
        for line in fp:
            if "GYO complete" in line:
                continue
            elif line.count('_')==3:
                line = line[:-1]
                if ']' in line:
                    line = line[:-1]
                arr = line.split('_')
                try:
                    time_gry.append(float(arr[0]))
                    gry_x.append(float(arr[1]))
                    gry_y.append(float(arr[2]))
                    gry_z.append(float(arr[3]))
                except ValueError:
                        continue

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
        'gry_x_std': gry_x_std[:minLen],'gry_y_std': gry_y_std[:minLen],'gry_z_std': gry_z_std[:minLen],
        'label':label[:minLen]})
    matrix = matrix[matrix.dT!=0]

    if f==0:
        single_outside = matrix

    elif f==1:
        single_inside = matrix

    elif f==2:
        double_outside = matrix

    elif f==3:
        double_inside = matrix

frames = [single_outside, single_inside, double_outside, double_inside]
results = pd.concat(frames)
x = np.array(results.drop(['label'],1))
x = preprocessing.scale(x)
y = np.array(results['label'])
Accuracy = 0
# machine learning
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
clf = svm.SVC(decision_function_shape='ovr')
clf.fit(x_train, y_train)
# accuracy = clf.score(x_test, y_test)
print clf.predict(x_test)
print y_test
print clf.score(x_test,y_test)
with open('gesture_recognizeSVM_SVC.pickle','wb') as f:
    pickle.dump(clf,f)
