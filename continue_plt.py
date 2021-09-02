import matplotlib.pyplot as plt
import seat as se
import read as re
import position as pos
import time


number,ohm  = sensorlist.split(":")
listin = ["☐"]*300
co_ohm = float(ohm)
co_number = int(number)
listin[co_number] = co_ohm
bio =  pos.humidtest(listin)

def in_test(bio,localtime):

    fig = plt.figure()
    plt.ion()
    fig.clf()
    fig.subtitle(localtime)
    plt.imshow(bio,cmap="RdBu",vmax=1,vmin=-1)
    plt.ioff()
    plt.pause(0.2)
    plt.ioff()
    plt.show()

if __name__=="__main__":
    listin=[]

    ser = serial.Serial("COM3",115200)

    localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    while localtime <="2021-09-01 17:17:00":
        localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        
        sensorlist=se.moniter(str(ser.readline().decode().replace('\n','')))
        # for i in sensorlist:
        #     print(i,end='\n')
        # print(("-----------------end------------------"))
        # print(str(ser.readline().decode().replace('\n','')))
        number,ohm  = sensorlist.split(":")
        
        co_ohm = float(ohm)
        co_number = int(number)
        listin[co_number] = co_ohm
        bio =  pos.humidtest(listin)
        in_test(bio,localtime)

      
    # print("end")



