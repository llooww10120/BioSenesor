import matplotlib.pyplot as plt
from openpyxl import load_workbook
import numpy as np
import pandas as pd


def time_cal(starttime,stoptime):
    endtime=int(stoptime[0:2])*3600+int(stoptime[3:5])*60+int(stoptime[-2:])
    begintime=int(starttime[0:2])*3600+int(starttime[3:5])*60+int(starttime[-2:])
    time_scale=int(endtime)-int(begintime)
    hour=time_scale//3600
    mint=(time_scale%3600)//60
    sec=((time_scale%3600)%60)
    return str(hour)+":"+str(mint)+":"+str(sec)


df = pd.read_csv("2021-10-02.csv")
ax = df["time"]

for i in range(1):
    bx = df[str(11)]
    cx = df[str(25)]
    dx = df[str(50)]
    y_stick = np.arange(400,1023,100)
 
    start_time=ax[0]
    fig = plt.figure()
    axx=fig.add_subplot(111)

    plt.plot(ax,bx,color="blue",linewidth=1,marker="None")
    plt.plot(ax,cx,color="red",linewidth=1,marker="None")
    plt.plot(ax,dx,color="green",linewidth=1,marker="None")
    plt.legend(['drop center:x=25, y=9','beside center:x=23 ,y=6',"dry:x=20 ,y=4"])
    plt.xlabel("time")

    plt.ylabel("Ohm")
    plt.yticks(y_stick)
    filename=str(0)+'.png'
    plt.savefig('./image/'+filename)
    

