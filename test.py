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
            for j in i[2:] :
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
    number=[]
    time,data = get_label_data('./testdata/2021-10-14/1/2021-10-14.csv')
    for i in data:
        number.append(i.count(1))
    # print(time)
    plt.figure(figsize=(10,10),dpi=100,linewidth=2)
    plt.plot(time,number)
    plt.show()