<<<<<<< HEAD
import serial
import time
import seat as se
listin=[]

ser = serial.Serial("/dev/ttyACM0",9600)

localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

while localtime <="2021-08-30 06:30:00":
    localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    
    sensorlist=se.moniter(str(ser.readline().decode().replace('\n','')))
    # for i in sensorlist:
    #     print(i,end='\n')
    # print(("-----------------end------------------"))
    # print(str(ser.readline().decode().replace('\n','')))
    
print("end")
