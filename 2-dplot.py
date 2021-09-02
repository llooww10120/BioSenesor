import serial
import datetime
import csv
import os
def gettime():
    dtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    localtime=dtime[11:0]
    date=dtime[:10]
    return date,localtime
def getdata(ser):
    data=[]
    if(str(ser.readline().decode().replace('\n',''))=="ALL DONE\r"):
        for i in range(250):
            data.append(str(ser.readline().decode().replace('\n','').replace('\r','')))
    return data

def writedata(ser,name,time):
    with open(name ,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time'] +[ str(i) for i in range(250)])
        localtime=datetime.datetime.now().strftime("%H:%M:%S")
        while localtime <= time:
            data=[]
            localtime=datetime.datetime.now().strftime("%H:%M:%S.%f")
            # print(localtime)
            data.append(str(localtime))
            writer.writerow(data+getdata(ser))
                # print(data)
    print("end")
if __name__=="__main__":
    ser = serial.Serial("COM3",115200)
    date,localtime=gettime()
    name='./'+date+".csv"
    print(str((datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%H:%M:%S")))
    writedata(ser,name,(datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%H:%M:%S"))
    