import serial
import time

def readdata():
    listin=[]
def moniter(test):
    if(test!="ALL DONE\r"):
        number,ohm  = test.split(":")
        # listin = ["☐"]*300
        ohm = float(ohm)
        number = int(number)

        if ohm < 8000 and ohm >100:            #潮濕
            print(number,": is wet")

listin=[]

ser = serial.Serial("COM3",115200)

while localtime <="2021-09-01 17:17:00":
    localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            
    sensorlist=moniter(str(ser.readline().decode().replace('\n','')))

