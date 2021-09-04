import serial
import datetime
import csv
import os
import matplotlib
import matplotlib.pyplot as plt
import senserlist
def gettime():
    dtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    localtime=dtime[11:0]
    date=dtime[:10]
    return date,localtime
def getdata(ser):
    data=[]
    if(str(ser.readline().decode().replace('\n',''))=="ALL DONE\r"):
        for i in range(250):
            data.append(float(str(ser.readline().decode().replace('\n','').replace('\r',''))))
        return data

def writedata(ser,name,min):
    with open(name ,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time'] +[ str(i) for i in range(250)])
        localtime=datetime.datetime.now().strftime("%H:%M:%S")
        time=str((localtime+datetime.timedelta(minutes=min)).strftime("%H:%M:%S"))
        while localtime <= time:
            data=[]
            localtime=datetime.datetime.now().strftime("%H:%M:%S:%f")
            data.append(str(localtime))
            out=getdata(ser)
            if out:
                writer.writerow(data+out)
    print("end")
def picture(name):
    matplotlib.use("Agg")
    with open(name,newline='') as csvfile:
        rows=csv.reader(csvfile)[1:]
        num=1
        for row in rows:
            listin=row[1:]
            test_time=row[0]
            listin=[int(i.replace('.0','')) for i in listin]
            plt.figure()
            filename=str(num)+'.png'
            plt.imshow(senserlist.getsensorlistet(listin),cmap="RdBu",vmax=1023,vmin=0)
            plt.colorbar()
            plt.title(test_time)
            plt.ioff()
            plt.savefig('./image/'+filename)
            plt.close('all')
            plt.clf()
            plt.cla()
            num+=1
if __name__=="__main__":
    ser = serial.Serial("COM3",115200)
    date,localtime=gettime()
    name='./'+date+".csv"
    time=str((datetime.datetime.now()+datetime.timedelta(minutes=3)).strftime("%H:%M:%S"))
    with open(name ,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time'] +[ str(i) for i in range(250)])
        while localtime <= time:
            data=[]
            localtime=datetime.datetime.now().strftime("%H:%M:%S:%f")
            data.append(str(localtime))
            out=getdata(ser)
            if out:
                writer.writerow(data+out)
    print('getdataend')
    picture(name)
    