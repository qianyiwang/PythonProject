import numpy as np
import pandas as pd
from scipy import signal
from sklearn import cross_validation
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO
import pickle
# declear features
gry_x_max = []
gry_x_min = []
gry_x_peakNum = []
acc_z_max = []
acc_z_min = []
acc_z_peakNum = []
label = []

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
    time_acc = []
    time_gry = []

    with open(fileName+'_acc.txt') as fp:
        for line in fp:
            if "ACC complete" in line:
                acc_z_max.append(max(acc_z))
                acc_z_min.append(min(acc_z))
                acc_z_peakNum.append(len(signal.find_peaks_cwt(acc_z, np.arange(0.1,1))))
                acc_z = []

                if f == 0:
                    label.append('single_outside')
                elif f==1:
                    label.append('single_inside')
                elif f==2:
                    label.append('double_outside')
                elif f==3:
                    label.append('double_inside')

            elif line.count('_')==3:
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

                except ValueError:
                        continue

    with open(fileName+'_gyo.txt') as fp:
        for line in fp:
            if "GYO complete" in line:
                gry_x_max.append(max(gry_x))
                gry_x_min.append(min(gry_x))
                gry_x_peakNum.append(len(signal.find_peaks_cwt(gry_x, np.arange(0.1,1))))
                gry_x = []
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

matrix = pd.DataFrame({'acc_z_max': acc_z_max,'acc_z_min':acc_z_min, 'acc_z_peakNum': acc_z_peakNum,
    'gry_x_min': gry_x_min,'gry_x_max': gry_x_max, 'gry_x_peakNum': gry_x_peakNum,
    'label':label})

x = np.array(matrix.drop(['label'],1))
y = np.array(matrix['label'])
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
# print x_train
# machine learning using decision tree
# clf = tree.DecisionTreeClassifier(max_features = 6)
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(x_train, y_train)
# with open("randomForest.dot", 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f)
i_tree = 0
for tree_in_forest in clf.estimators_:
    with open('tree_' + str(i_tree) + '.dot', 'w') as my_file:
        my_file = tree.export_graphviz(tree_in_forest, out_file = my_file)
    i_tree = i_tree + 1

# with open('gesture_recognize_randomForest.pickle','wb') as f:
#     pickle.dump(clf,f)

print clf.score(x_test, y_test)
