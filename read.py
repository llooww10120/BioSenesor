import serial
from openpyxl import Workbook
from openpyxl import load_workbook
import time
import seat as se
ser = serial.Serial("COM3",9600)
name="text1.xlsx"
wb=Workbook()
ws=wb.active
localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
rownum=1
while localtime <="2021-08-27 02:37:00":
    localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    se.moniter(ser.readline().decode("utf-8"))
    
print("end")
wb.save(name)
