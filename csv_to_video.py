import matplotlib.pyplot as plt
import senserlist
import pandas as pd
import matplotlib.animation as animation
index=[str(i) for i in range(250)]

def update(i):
    plt.cla()
    plt.title(date_data[i+10])
    plt.imshow(senserlist.getsensorlist(data.iloc[i][1:]),cmap="RdBu",vmax=1023,vmin=0)

if __name__=="__main__":
    
    date = '2021-12-06'
    
    fig = plt.figure()
    chil='/3'
    path='./testdata/'+date+chil
    
    # data = pd.read_csv('./test.csv',engine = "python")
    
    data = pd.read_csv(path+'/'+date+'.csv',engine = "python")
    date_data= data['time']
    for i in index:
        data[i]=data[i].rolling(10).mean()
    data = data[10:]        

    pl=plt.imshow(senserlist.getsensorlist(data.iloc[0][1:]),cmap="RdBu",vmax=1023,vmin=0)

    plt.colorbar(pl)
    ani = animation.FuncAnimation(fig,update,frames=range(0,len(data)),interval=100)
    plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python39\\ffmpeg-4.4.1-full_build\\bin\\ffmpeg.exe'
    ffmpeg_writer = animation.FFMpegWriter(fps = 15)
    ani.save('./testdata/'+date+chil+'/'+date+'.mp4')
    print('finished!!')