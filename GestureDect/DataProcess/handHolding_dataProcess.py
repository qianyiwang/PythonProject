import matplotlib.pyplot as plt
import math
fileName = 'double_inside_accy'
acc_z = []
with open(fileName+'.txt') as fp:
    for line in fp:
        if 'V' in line:
            p = line.index('V')
            # print line[p+23:];
            acc_z.append(line[p+8:])


fig = plt.figure('acc_magnitude')
plt.plot(acc_z,'bo',acc_z,'k')
plt.show()
