import matplotlib.pyplot as plt
from openpyxl import load_workbook
def time_cal(starttime,stoptime):
    endtime=int(stoptime[0:2])*3600+int(stoptime[3:5])*60+int(stoptime[-2:])
    begintime=int(starttime[0:2])*3600+int(starttime[3:5])*60+int(starttime[-2:])
    time_scale=int(endtime)-int(begintime)
    hour=time_scale//3600
    mint=(time_scale%3600)//60
    sec=((time_scale%3600)%60)
    return str(hour)+":"+str(mint)+":"+str(sec)
wb=load_workbook('text.xlsx')
sheet=wb["Sheet"]
a=sheet["A"]
b=sheet["B"]
ax=[]
by=[]
for cell in a:
    ax.append(cell.value[-8:])
for cell in b:
    temp=cell.value
    by.append(temp)
by=by[1:]
ax=ax[1:]
min_index=by.index(min(by))
min_time=ax[min_index]
start_time=ax[0]
fig = plt.figure()
axx=fig.add_subplot(111)
plt.plot(ax,by,color="blue",linewidth=1,marker="None")
plt.plot(by[min_index])
show_min='['+str(by[min_index])+']'+"\nused time :"+time_cal(start_time,min_time)
plt.xlabel("time")
plt.ylabel("Ohm")
plt.annotate(show_min,xytext=(ax[min_index],by[min_index]),xy=(ax[min_index],by[min_index]),color='r')
plt.savefig("test.png")
plt.show()