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
        fileName = 'single_outside_3'
    elif f==1:
        fileName = 'single_inside_3'
    elif f == 2:
        fileName = 'double_outside'
    elif f==3:
        fileName = 'double_inside'

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

    idx = len(acc_x_mean)-len(gry_x_mean)
    # print idx
    # print len(acc_x_mean)
    # print len(gry_x_mean)
    # print len(label)
    if idx>0:
        matrix = pd.DataFrame({'dT':dT[:-idx-20],'acc_x_max': acc_x_max[:-idx],'acc_y_max': acc_y_max[:-idx],'acc_z_max': acc_z_max[:-idx],
            'acc_x_min': acc_x_min[:-idx],'acc_y_min':acc_y_min[:-idx],'acc_z_min':acc_z_min[:-idx],
            'acc_x_mean': acc_x_mean[:-idx], 'acc_y_mean': acc_y_mean[:-idx],'acc_z_mean': acc_z_mean[:-idx],
            'acc_x_std': acc_x_std[:-idx], 'acc_y_std': acc_y_std[:-idx], 'acc_z_std': acc_z_std[:-idx],
            'gry_x_min': gry_x_min,'gry_y_min': gry_y_min,'gry_z_min': gry_z_min,
            'gry_x_max': gry_x_max,'gry_y_max': gry_y_max,'gry_z_max': gry_z_max,
            'gry_x_mean': gry_x_mean,'gry_y_mean': gry_y_mean,'gry_z_mean':gry_z_mean,
            'gry_x_std': gry_x_std,'gry_y_std': gry_y_std,'gry_z_std': gry_z_std,
            'label':label[:-idx-20]})
    else:
        matrix = pd.DataFrame({'dT':dT[:-20],'acc_x_max': acc_x_max,'acc_y_max': acc_y_max,'acc_z_max': acc_z_max,
            'acc_x_min': acc_x_min,'acc_y_min':acc_y_min,'acc_z_min':acc_z_min,
            'acc_x_mean': acc_x_mean, 'acc_y_mean': acc_y_mean,'acc_z_mean': acc_z_mean,
            'acc_x_std': acc_x_std, 'acc_y_std': acc_y_std, 'acc_z_std': acc_z_std,
            'gry_x_min': gry_x_min[:+idx],'gry_y_min': gry_y_min[:+idx],'gry_z_min': gry_z_min[:+idx],
            'gry_x_max': gry_x_max[:+idx],'gry_y_max': gry_y_max[:+idx],'gry_z_max': gry_z_max[:+idx],
            'gry_x_mean': gry_x_mean[:+idx],'gry_y_mean': gry_y_mean[:+idx],'gry_z_mean':gry_z_mean[:+idx],
            'gry_x_std': gry_x_std[:+idx],'gry_y_std': gry_y_std[:+idx],'gry_z_std': gry_z_std[:+idx],
            'label':label[:-20]})
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
# x = preprocessing.scale(x)
y = np.array(results['label'])
Accuracy = 0
for i in range(10):
    # machine learning
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
    # clf = LinearRegression()
    clf = svm.SVR() # rbf: radial basis function
    # clf = OneVsRestClassifier(LinearSVC(random_state=0))
    # clf = linear_model.LogisticRegressionCV(multi_class= 'multinomial')
    # clf = ensemble.RandomForestClassifier()
    clf.fit(x_train, y_train)
    # train_scores, valid_scores = validation_curve(Ridge(), x_train, y_train, "alpha",np.logspace(-7, 3, 3))
    accuracy = clf.score(x_test, y_test)
    print accuracy
    # scores = cross_validation.cross_val_score(clf, x, y, cv=5)
    # print scores
    # print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    if accuracy>Accuracy:
        Accuracy = accuracy
        with open('gesture_recognizeSVM.pickle','wb') as f:
            pickle.dump(clf,f)

print 'SVM Accuracy: ',Accuracy
# print clf.predict(x_test)
