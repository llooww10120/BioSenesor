import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib
import senserlist
def humidtest(sensor):
    biosensor = np.zeros([25,10])
    for a in range(25):
        for b in range(10):
            data =float(sensor[a][b])
            if data < 8000 and data >100:            #潮濕
                    biosensor[a][b] = 1 
            elif data > 8000 and data< 300000:          #乾燥
                    biosensor[a][b] = 0
            elif data > 300000 :         #錯誤_開路點
                    biosensor[a][b] = -1 
            
    return biosensor


def getpos(pos):
    cor=[]
    broken = []
    for i in range(25):
        for j in range(10):
            if pos[i-1][j-1]==1:
                cor.append([j,i])
            elif pos[i-1][j-1]==2:
                broken.append([j,i])

    return cor, broken

def plotmap(array,time,num):
    filename=str(num)+'.png'
    plt.imshow(array,cmap="RdBu",vmax=1,vmin=-1)
    plt.title(time)
    plt.ioff()
    plt.savefig('./image/'+filename)
if __name__=="__main__":
    matplotlib.use("Agg")
    name="2021-09-03.csv"
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
         