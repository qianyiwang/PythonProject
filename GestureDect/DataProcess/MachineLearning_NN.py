import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import pickle

# from sklearn.neural_network import MLPClassifier
from sknn.mlp import Classifier, Layer

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

    lenArray = [len(acc_x), len(acc_y), len(acc_z),
                len(gry_x), len(gry_y), len(gry_z),
                len(label), len(dT)]
    minLen = min(lenArray)

    matrix = pd.DataFrame({'dT':dT[:minLen],'acc_x': acc_x[:minLen],'acc_y': acc_y[:minLen],'acc_z': acc_z[:minLen],
        'gry_x': gry_x[:minLen],'gry_y':gry_y[:minLen],'gry_z':gry_z[:minLen],
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
# machine learning
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
# clf = MLPClassifier(solver='lbgfs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
clf = Classifier(
    layers=[
        Layer("Maxout", units=100, pieces=2),
        Layer("Softmax")],
    learning_rate=0.001,
    n_iter=25)
clf.fit(x_train, y_train)
# accuracy = clf.score(x_test, y_test)
print clf.predict(x_test)
print y_test
print clf.score(x_test,y_test)
with open('gesture_recognizeSVM_NN.pickle','wb') as f:
    pickle.dump(clf,f)
