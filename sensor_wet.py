import matplotlib.pyplot as plt
import csv
from sklearn.model_selection import train_test_split

ax = []
bx = []
cx = []

with open('label.csv','r',newline='') as csvfile:
    label=csv.reader(csvfile)
    for i in label:
        ax.append(i[1])
        if "1.0" in i[2:]: 
            cx.append(1)
        else:
            cx.append(0)

fig = plt.figure()
plt.plot(ax,cx,'ro')

plt.legend(['1 : wet','0 : dry'])
plt.xlabel("time")
plt.ylabel("state")
plt.yticks([0,1])
plt.show()