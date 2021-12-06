import serial
import datetime
import csv
import os
import matplotlib
import matplotlib.pyplot as plt
import senserlist
import pandas as pd
import matplotlib.animation as animation
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
def update(i):
    plt.cla()
    plt.title(date_data[i+10])
    plt.imshow(senserlist.getsensorlist(data.iloc[i][1:]),cmap="RdBu",vmax=1023,vmin=0)

def rolling(name):
    matplotlib.use("Agg")
    path='./testdata/2021-10-02/'+name
    data = pd.read_csv(path+'/2021-10-02.csv',engine = "python")
    for i in index:
        data[i]=data[i].rolling(10).mean()
    data = data[10:]
    num=1
    if not os.path.isdir(path+'/image-r/'):
        os.mkdir(path+'/image-r/')
    # print(len(data))
    for i in range(len(data)):
        plt.figure()
        filename=str(num)+'.png'
        plt.imshow(senserlist.getsensorlist(data.iloc[i][1:]),cmap="RdBu",vmax=1023,vmin=0)
        plt.colorbar()
        # plt.title(test_time)
        plt.ioff()
        plt.savefig(path+'/image-r/'+filename)
        plt.close('all')
        plt.clf()
        plt.cla()
        num+=1
def picture(name):
    path='./testdata/2021-09-27/'+name
    matplotlib.use("Agg")
    if not os.path.isdir(path+'/image/'):
        os.mkdir(path+'/image/')
    with open(path+'/2021-09-27.csv','r',newline='') as csvfile:
        rows=csv.reader(csvfile)
        num=1
        for row in rows:
            listin=row[1:]
            test_time=row[0]
            listin=[int(i.replace('.0','')) for i in listin]
            plt.figure()
            filename=str(num)+'.png'
            plt.imshow(senserlist.getsensorlist(listin),cmap="RdBu",vmax=1023,vmin=0)
            plt.colorbar()
            plt.title(test_time)
            plt.xlabel("Unit 5mm", fontsize=10) #x軸標題
            plt.ylabel("Unit 10mm", fontsize=10) #y軸標題
            plt.ioff()
            plt.savefig(path+'/image/'+filename)
            plt.close('all')
            plt.clf()
            plt.cla()
            num+=1
def getdata(time):
    ser = serial.Serial("COM3",115200)
    date,localtime=gettime()
    name='./'+date+".csv"
    time=str((datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%H:%M:%S"))
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
    
def save_mpeg4(date):
    fig = plt.figure()

    chil='/1'
    path='./testdata/'+date+chil
    data = pd.read_csv(path+'/'+date+'.csv',engine = "python")
    date_data= data['time']
    for i in index:
        data[i]=data[i].rolling(10).mean()
    data = data[10:]        
    # if not os.path.isdir(path+'/image-s/'):
    #     os.mkdir(path+'/image-s/')
    pl=plt.imshow(senserlist.getsensorlist(data.iloc[0][1:]),cmap="RdBu",vmax=1023,vmin=0)

    plt.colorbar(pl)
    ani = animation.FuncAnimation(fig,update,frames=range(0,len(data)),interval=100)
    plt.rcParams['animation.ffmpeg_path'] = 'F:\\bin\\ffmpeg.exe'
    ffmpeg_writer = animation.FFMpegWriter(fps = 15)
    # Writer= animation.FFMpegWriter()
    # writer=Writer(fps=10,metadata=dict(artist='Ming'),bitrate=1800)
    ani.save('./testdata/'+date+chil+'/2-dmovie.mp4')
if __name__=="__main__":
   
    print('')