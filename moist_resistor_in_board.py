import matplotlib.pyplot as plt
import csv

from numpy import number
threshold=800
def get_label_data(name):
    label=[]
    with open(name) as csvfile:  
        time = []
        data= csv.reader(csvfile)
        label=[]
        for i in data:
            time.append(i[0])
            a = []
            for j in i[2:-10] :
                if float(j)<threshold:
                    a.append(1)
                else:
                    a.append(0)
            label.append(a)
    return time[1:],label[1:]
# with open('label.csv','r',newline='') as csvfile:
#     time= []
#     data = csv.reader(csvfile)
#     number= []
#     for i in data:
#         time.append(i[1])
#         number.append(i[2:].count('1.0'))
# plt.figure(figsize=(10,10),dpi=100,linewidth=2)
# plt.plot(time,number)
# plt.show()
if __name__=='__main__':
    print("start!!")
    number=[]
    date ='2021-10-22'
    path = './csv/'
    time,data = get_label_data(path + date + '.csv')
    for i in data:
        number.append(i.count(1))
    plt.figure(figsize=(10,10),dpi=100,linewidth=2)
    plt.plot(time,number)
    plt.ylim([0,250])
    plt.xlabel('time(ms)')
    plt.ylabel('number')
    plt.savefig(path+date+'_humid.png')
    plt.show()
    print("finish!!")