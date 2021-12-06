import serial
import datetime
import csv
index=[str(i) for i in range(250)]
    
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

if __name__=="__main__":
    print('getdata start')
    ser = serial.Serial("COM3",115200)
    date,localtime=gettime()
    name='./'+date+".csv"
    time=str((datetime.datetime.now()+datetime.timedelta(seconds=10)).strftime("%H:%M:%S"))
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
