import matplotlib.pyplot as plt
from openpyxl import load_workbook
import pandas as pd
import csv

def time_cal(starttime,stoptime):
    endtime=int(stoptime[0:2])*3600+int(stoptime[3:5])*60+int(stoptime[-2:])
    begintime=int(starttime[0:2])*3600+int(starttime[3:5])*60+int(starttime[-2:])
    time_scale=int(endtime)-int(begintime)
    hour=time_scale//3600
    mint=(time_scale%3600)//60
    sec=((time_scale%3600)%60)
    return str(hour)+":"+str(mint)+":"+str(sec)

# with open(name,newline='') as csvfile:
#         rows=csv.reader(csvfile)[1:]
#         for row in rows:
#             a = row[:2]    #選讀哪顆濕敏
#             b = row[:4]    #選讀哪顆施敏

df = pd.read_csv("./testdata/2021-10-01/1/2021-10-01.csv")
ax = df["time"]
for i in range(1):
    bx = df[str(11)]
    # min_index=min(bx)
    # min_time=ax[min_index]
    start_time=ax[0]
    fig = plt.figure()
    axx=fig.add_subplot(111)
    plt.plot(ax,bx,color="blue",linewidth=1,marker="None")
    # plt.plot(bx[min_index])
    # show_min='['+str(bx[min_index])+']'+"\nused time :"+time_cal(start_time,min_time)
    plt.xlabel("time")

    plt.ylabel("Ohm")
    plt.show()
    # plt.annotate(show_min,xytext=(ax[min_index],bx[min_index]),xy=(ax[min_index],bx[min_index]),color='r')
    filename=str(i)+'.png'
    # plt.savefig('./testdata/2021-10-01/2/image/'+filename)
    

# ax=[]
# by=[]
# for cell in a:
#     ax.append(cell.value[-8:])
# for cell in b:
#     temp=float(cell.value.replace('_x000D_','')[3:])
#     by.append(temp)
# by=by[1:]
# ax=ax[1:]

# min_index=by.index(min(by))
# min_time=ax[min_index]
# start_time=ax[0]
# fig = plt.figure()
# axx=fig.add_subplot(111)
# plt.plot(ax,by,color="blue",linewidth=1,marker="None")
# plt.plot(by[min_index])
# show_min='['+str(by[min_index])+']'+"\nused time :"+time_cal(start_time,min_time)
# plt.xlabel("time")

# plt.ylabel("Ohm")
# plt.annotate(show_min,xytext=(ax[min_index],by[min_index]),xy=(ax[min_index],by[min_index]),color='r')
# plt.savefig("test.png")
# plt.show()