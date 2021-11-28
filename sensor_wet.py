import matplotlib.pyplot as plt
import csv
from sklearn.model_selection import train_test_split

ax = []
bx = []
cx = []
threshold = 800
def get_label_data(name):
    label=[]
    with open(name) as csvfile:  
        time = []
        data= csv.reader(csvfile)
        label=[]
        for i in data:
            time.append(i[0])
            a = []
            for j in i[2:] :
                if float(j)<threshold:
                    a.append(1)
                else:
                    a.append(0)
            label.append(a)
    return time[1:],label[1:]
date = "./testdata/2021-10-22/1/"
name = date + "2021-10-22.csv"

ax,bx = get_label_data(name)

for i in range(len(bx)):
    for j in range(240):
        if  bx[i][j] == 1: 
            cx.append(1)
            break
        else:
            if j ==239:
                cx.append(0)
            

# print(cx)
fig = plt.figure()
plt.plot(ax,cx,'ro')

plt.legend(['state'])
plt.xlabel("time(ms)")
plt.ylabel("state")
plt.yticks([0,1])
plt.savefig(date+'state.png')