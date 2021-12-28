import pandas as pd
import serial
import datetime
import csv
import os
import matplotlib
import matplotlib.pyplot as plt
import senserlist
import pandas as pd
import matplotlib.animation as animation
import numpy as np
data = pd.read_csv('./test.csv',engine = "python")
xx = np.zeros(168)
for j in range(168):
    for i in range(len(data['0'])-30):
        temp=[]
        for k in range(30):
            temp.append(data[str(j)][i+k])
        if temp==[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
            xx[j]=1

print(xx.reshape(21,8))
# date = ''
# fig = plt.figure()
# def update(i):
#     plt.cla()
#     plt.title(i)
#     # print(data[i:i+1].values.reshape(21,8))
#     plt.imshow((data[i:i+1].values.reshape(21,8)),cmap="RdBu",vmax=1,vmin=0)
# chil='/1'
# path='./testdata/'+date+chil
# data = pd.read_csv('./test.csv',engine = "python")
    # date_data= data['time']
    # for i in index:
    #     data[i]=data[i].rolling(10).mean()
    # data = data[10:]        
    # if not os.path.isdir(path+'/image-s/'):
    #     os.mkdir(path+'/image-s/')
# pl=plt.imshow(data[0:1].values.reshape(21,8),cmap="RdBu",vmax=1,vmin=0)

# plt.colorbar(pl)
# ani = animation.FuncAnimation(fig,update,frames=range(0,len(data)),interval=100)
# plt.rcParams['animation.ffmpeg_path'] = 'F:\\bin\\ffmpeg.exe'
# ffmpeg_writer = animation.FFMpegWriter(fps = 15)
    # Writer= animation.FFMpegWriter()
    # writer=Writer(fps=10,metadata=dict(a
    # rtist='Ming'),bitrate=1800)
# ani.save('./2-dmovie.mp4')
# a = data[20321:20322].values
# print(a.reshape(21,8))