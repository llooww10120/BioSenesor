import matplotlib.pyplot as plt
import csv
import numpy as np
from numpy.core.fromnumeric import size
import senserlist
import urinepoint as up
from numpy import number

threshold=800
high_threshold=850
low_threshold=750

def get_label_data(name, point):
    label=[]
    number=[]
    r_num=0 #how many resistors covered by the urine point
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
                
        for i in label[1:]:
            number.append(i.count(1))
                   
    return time[1:],number,r_num 

def get_new_label_data(name, point):
    label=[]
    number=[]
    r_num=0 #how many resistors covered by the urine point
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
                
        for i in label[1:]:
            number.append(i.count(1))
                   
    return time[1:],number,r_num 


def get_diff_data(name, point):
    label=[]
    number=[]
    r_num=0 #how many resistors covered by the urine point
    with open(name) as csvfile:  
        time=[]
        data= csv.reader(csvfile)
        label=[]
        medianlist = []
        for i in data:
            
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
        
        time = time[1:] 
        for i in label[1:]:
            medianlist.append(i.count(1))
            if len(medianlist)==10:
                number.append(int(np.median(medianlist)))
                medianlist=[]
                   
    return time,number,r_num 



if __name__=='__main__':
    print("start!!")
    number=[]
    date ='2021-10-19-2'
    point = 'p2'
    in_path = './csv/'
    out_path = './csv/urine_pic/'
    
    #plot resistor to time graph
    time,number,r_num = get_label_data(in_path + date + '.csv', date+'-'+point)
    plt.figure(figsize=(10,10),dpi=100,linewidth=2)
    plt.plot(time,number)
    plt.ylim(0,r_num)
    plt.xlabel('time(ms)')
    plt.ylabel('number')
    plt.savefig(out_path+date+'-'+point+'-('+str(high_threshold)+'-'+str(low_threshold)+')'+'.png')
    #plt.show()
    print("finish!!")
    
    # #plot resistor median to time graph
    # time,number,r_num = get_diff_data(in_path + date + '.csv', date+'-'+point)
    # while len(time) != len(number):
    #     if len(time) > len(number):
    #         time.pop()
    #     else:
    #         number.pop()
    # plt.figure(figsize=(10,10),dpi=100,linewidth=2)
    # plt.plot(time,number)
    # plt.ylim(0,r_num)
    # plt.xlabel('time(ms)')
    # plt.ylabel('number')
    # plt.savefig(out_path+date+'-'+point+'_median_2.png')
    # #plt.show()
    # print("finish!!")
    
    