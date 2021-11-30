import matplotlib.pyplot as plt
import csv

from numpy.core.fromnumeric import size
import senserlist
import urinepoint as up

from numpy import number
threshold=800

def get_label_data(name, point):
    label=[]
    r_num=0
    with open(name) as csvfile:  
        time = []
        data= csv.reader(csvfile)
        label=[]
        count = 10
        for i in data:
            
            if(count!=0):
                count-=1
            else:
                time.append(i[0])
                
                listin=i[1:]
                listin=[int(j.replace('.0','')) for j in listin]
            
                urinelist = up.getlist(senserlist.getsensorlist(listin),point) 
                r_num = len(urinelist)       
                a = []
                for j in urinelist:
                    if float(j)<threshold:
                        a.append(1)
                    else:
                        a.append(0)
                label.append(a) 
                count=10
                   
    return time[1:],label[1:],r_num 

if __name__=='__main__':
    print("start!!")
    number=[]
    date ='2021-10-22'
    point = 'p2'
    in_path = './csv/'
    out_path = './csv/urine_pic/'
    time,data,r_num = get_label_data(in_path + date + '.csv', date+'-'+point)
    for i in data:
        number.append(i.count(1))
    plt.figure(figsize=(10,10),dpi=100,linewidth=2)
    plt.plot(time,number)
    plt.ylim(0,r_num)
    plt.xlabel('time(ms)')
    plt.ylabel('number')
    plt.savefig(out_path+date+'-'+point+'.png')
    #plt.show()
    print("finish!!")