from sklearn import svm
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovr')
clf.fit(X, Y)
# svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovo', degree=3, gamma='auto', kernel='rbf',
#     max_iter=-1, probability=False, random_state=None, shrinking=True,
#     tol=0.001, verbose=False)
dec = clf.decision_function([[1]])
print dec
print clf.predict([[1]])


# clf.decision_function_shape = "ovr"
# dec = clf.decision_function([[1]])
# print dec.shape[1] # 4 classes
