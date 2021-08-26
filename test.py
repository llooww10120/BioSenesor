import serial
from openpyxl import Workbook
from openpyxl import load_workbook
import time

ser = serial.Serial("COM3",9600)
name="text1.xlsx"
wb=Workbook()
ws=wb.active
localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
rownum=1
while localtime !="2021-08-26 16:47:00":
    localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    # content=str(ser.readline().decode("utf-8")[:-2])
    # if(content=="Setup Finished..."):
    ws.cell(row=rownum,column=1,value=localtime)
    for i in range(2,258):
        ws.cell(row=rownum,column=i,value=str(ser.readline().decode("utf-8")))
    rownum+=1
    # print(str(ser.readline().decode("utf-8")[:-2]))
print("end")
wb.save(name)
