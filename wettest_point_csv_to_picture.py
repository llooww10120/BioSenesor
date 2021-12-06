import datetime
import csv
import matplotlib
import matplotlib.pyplot as plt
import senserlist

def gettime():
    dtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    localtime=dtime[11:0]
    date="2021-10-19_1"
    return date,localtime

def picture(name):
    matplotlib.use("Agg")
    with open(name,'r',encoding="utf-8") as csvfile:
        rows=csv.reader(csvfile)
        min=[]
        for row in rows:
            
            listin=row[1:]
            listin=[int(i.replace('.0','')) for i in listin]

            if not min:
                min = listin[:]
            else:
                for i in range(len(listin)):
                    if int(min[i])>int(listin[i]):
                        min[i] = listin[i]
            
        plt.figure()
        filename= name+'_wettest.png'
        plt.imshow(senserlist.getsensorlist(min),cmap="RdBu",vmax=1023,vmin=0)
        plt.colorbar()
        plt.title(name)
        plt.ioff()
        plt.savefig('./'+filename)
        plt.close('all')
        plt.clf()
        plt.cla()
        
        

if __name__=="__main__":
    date,localtime=gettime()
    name='./'+date+".csv"
    picture(name)
    print('finished!!!')