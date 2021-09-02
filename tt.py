import serial
ser = serial.Serial("COM3",115200)
# print('start\n'.encode())
# ser.write('start\r\n'.encode())
# try:
#     while True:
#         print(str(ser.readline().decode().replace('\n','')))
# except KeyboardInterrupt:
#     ser.write(b'2\n')
#     for i in range(251):
#         print(str(ser.readline().decode().replace('\n','')))
a = input()
ser.write((a+'\n').encode())
try:
    while True:
        print(ser.readline())
except KeyboardInterrupt:
    ser.close()