import matplotlib.pyplot as plt
plt.ion()    # 打开交互模式
# 画第一幅图
plt.figure(1)
plt.plot([2,3,4])   #data1为用于画图像的数据

#画第一幅图和第二幅图之间可以继续运行其他程序
    
plt.figure(2)
plt.plot([2,3,4,1])  #data2为用于画图像的数据
    
plt.ioff()   #需要在显示图像前关闭交互模式，即在plt.show()之前加入这段代码，如果不加这句代码，则所有的图像都只会一闪而过。
    
plt.show()  #最后同时显示所有图片
