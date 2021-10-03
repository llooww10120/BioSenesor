import csv
import matplotlib.animation as animation
from matplotlib import artist, colors
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import senserlist 
import pandas as pd
import matplotlib
import os
from matplotlib import cm

fig = plt.figure(figsize=(10,10))
index=[str(i) for i in range(250)]

# x=[i for i in range(1,26) for j in range(1,11)]
# y=[j for i in range(1,26) for j in range(1,11)]
# def get_Z():
#     Z_list=[]
#     name='1000-1'
#     date='2021-09-28'
#     path='./testdata/'+date+'/'+name
#     data = pd.read_csv(path+'/'+date+'.csv',engine = "python")
#     for i in index:
#         data[i]=1023-data[i].rolling(10).mean()
#     data = data[10:]
    
#     for i in range(len(data)):
#         Z_list.append(senserlist.get_one_dim(data.iloc[i][1:]))

#     return Z_list
# Z_list=get_Z()
# ims=[]
# ax = plt.subplot(projection="3d")
# for i in range(len(Z_list)):
#     im=ax.scatter(x,y,Z_list[i],c=Z_list[i],cmap="seismic").findobj()
#     ims.append(im)
# ani= animation.ArtistAnimation(fig,ims,interval=500,repeat_delay=1000)
# Writer= animation.writers['ffmpeg']
# writer=Writer(fps=10,metadata=dict(artist='Ming'),bitrate=1800)
# ani.save('movie.mp4',writer=writer)
x=[i for i in range(1,11) ]
y=[i for i in range(1,26) ]
X,Y=np.meshgrid(x,y)
ims=[]

ax = fig.add_subplot(projection='3d')
def get_Z(date,name):
    Z_list=[]
    timelist=[]
    path='./testdata/'+date+'/'+name
    data = pd.read_csv(path+'/'+date+'.csv',engine = "python")
    timelist=data['time']
    for i in index:
        data[i]=1023-data[i].rolling(10).mean()
    data = data[10:]
    for i in range(len(data)):
        Z_list.append(np.array((senserlist.get_one_dim(data.iloc[i][1:]))))
    return timelist,Z_list
def update(i):
    plt.cla()
    plt.title(timelist[i+10])
    ax.set_xlabel('x')
    ax.set_ylabel('y') 
    ax.set_zlabel('humid')#
    norm = plt.Normalize(0, 1023)
    colors = cm.RdBu(norm(Z_list[i]))
    rcount, ccount, _ = colors.shape
    ax.set_zlim(0,1050)
    surf=ax.plot_surface(X,Y,Z_list[i],  rcount=rcount, ccount=ccount,facecolors=colors,cmap='RdBu',shade=False,linewidth=1)
    surf.set_facecolor((0,0,0,0))

def animate(date,name):
    ani = animation.FuncAnimation(fig,update,frames=range(0,len(Z_list)),interval=100)
    Writer= animation.writers['ffmpeg']
    writer=Writer(fps=10,metadata=dict(artist='Ming'),bitrate=1800)
    ani.save('./testdata/'+date+'/'+name+'/movie.mp4',writer=writer)
    # update(400)
if __name__=="__main__":
    date='2021-10-02'
    dir=os.listdir(path='./testdata/'+date)
    for i in dir:
        path='./testdata/'+date+'/'+i
        if os.path.isdir(path):
            timelist,Z_list=get_Z(date,i)
            if i == '1':
                norm = plt.Normalize(0, 1023)
                colorsa = cm.RdBu(norm(Z_list[0]))
                rcount, ccount, _ = colorsa.shape
                surf=ax.plot_surface(X,Y,Z_list[0], vmin=0,vmax=1023, rcount=rcount, ccount=ccount,facecolors=colorsa,cmap='RdBu',shade=False,linewidth=1)   
                cbar = plt.colorbar(surf,ticks=[0,0.5,1])
                cbar.ax.set_yticklabels(['0', '512', '1023'])  # vertically oriented colorbar 
            animate(date,i)
            print(i)

    # for i in range()
    # name='7'
    # timelist,Z_list=get_Z(date,name)
    # norm = plt.Normalize(0, 1023)
    # colorsa = cm.RdBu(norm(Z_list[0]))
    # rcount, ccount, _ = colorsa.shape

    # surf=ax.plot_surface(X,Y,Z_list[0], vmin=0,vmax=1023, rcount=rcount, ccount=ccount,facecolors=colorsa,cmap='RdBu',shade=False,linewidth=1)    
    # cbar = plt.colorbar(surf,ticks=[0,0.5,1])
    # cbar.ax.set_yticklabels(['0', '512', '1023'])  # vertically oriented colorbar
    # animate(date,name)