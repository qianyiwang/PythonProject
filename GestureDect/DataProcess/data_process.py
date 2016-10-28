import matplotlib.pyplot as plt
import math
fileName = 'double_inside'
acc_x = []
acc_y = []
acc_z = []
acc_m = []
acc_magnitude = []
gry_x = []
gry_y = []
gry_z = []
gry_m = []
gry_magnitude = []
with open(fileName+'_sample.txt') as fp:
    for line in fp:
        if 'V' in line:
            p = line.index('V')
            singleName = line[p+2:p+5]
            if singleName=='acc':
                data = line[p+7:].split('_')
                acc_x.append(data[0])
                acc_y.append(data[1])
                acc_z.append(data[2])
                acc_m.append(data[3])
                acc_magnitude.append(math.sqrt(float(data[0])*float(data[0])+float(data[1])*float(data[1])+float(data[2])*float(data[2])))
            elif singleName == 'gry':
                data = line[p+7:].split('_')
                gry_x.append(data[0])
                gry_y.append(data[1])
                gry_z.append(data[2])
                gry_m.append(data[3])
                gry_magnitude.append(math.sqrt(float(data[0])*float(data[0])+float(data[1])*float(data[1])+float(data[2])*float(data[2])))


fig = plt.figure('acc_magnitude')
ax1 = plt.subplot(131)
ax1.set_title('acc_x')
ax1.plot(acc_x,'yo',acc_x,'k')
ax2 = plt.subplot(132)
ax2.set_title('acc_y')
ax2.plot(acc_y,'go',acc_y,'k')
ax3 = plt.subplot(133)
ax3.set_title('acc_z')
ax3.plot(acc_z,'ro',acc_z,'k')
# plt.subplot(224)
# plt.plot(acc_magnitude,'bo',acc_magnitude,'k')

fig2 = plt.figure('gyo_magnitude')
ax4 = plt.subplot(131)
ax4.set_title('gyo_x')
ax4.plot(gry_x,'yo',gry_x,'k')
ax5 = plt.subplot(132)
ax5.set_title('gyo_y')
ax5.plot(gry_y,'go',gry_y,'k')
ax6 = plt.subplot(133)
ax6.set_title('gyo_z')
ax6.plot(gry_z,'ro',gry_z,'k')
# plt.subplot(224)
# plt.plot(gry_magnitude,'go',gry_magnitude,'k')
plt.show()
