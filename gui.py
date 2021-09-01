import tkinter as tk

import position as pos
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook


def create_label(txt):
    lbl_1 = tk.Label(window, text=txt, bg='yellow', fg='#263238', font=('Arial', 12), width=100, height=2)
    lbl_1.grid(column=0, row=0)

# create_label('Hello World !!!')

def create_button(txt):
    bt_1 = tk.Button(window, text=txt, bg='red', fg='white', font=('Arial', 12))
    bt_1['width'] = 50
    bt_1['height'] = 4
    bt_1['activebackground'] = 'red'        
# 按鈕被按下的背景顏色

    bt_1['activeforeground'] = 'yellow' 
    
    bt_1.grid(column=0, row=0)   


def define_layout(obj, cols=1, rows=1):
    
    def method(trg, cols, rows):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)

def button_event01():
    print(var.get())
    plt.ion()    # 打开交互模式
    # 画第一幅图
    plt.figure(1)
    plt.plot(data1)   #data1为用于画图像的数据
    
    #画第一幅图和第二幅图之间可以继续运行其他程序
    
    plt.figure(2)
    plt.plot(data2)  #data2为用于画图像的数据
    
    plt.ioff()   #需要在显示图像前关闭交互模式，即在plt.show()之前加入这段代码，如果不加这句代码，则所有的图像都只会一闪而过。
    
    plt.show()  #最后同时显示所有图片

def button_event02():
    print(var.get())
    mylabel.configure(text='my favourite fruit is ' + var.get())

def button_event03():
    print(var.get())
    mylabel.configure(text='my favourite fruit is ' + var.get())    


window = tk.Tk()
window.title('Window')
align_mode = 'nswe'
pad = 5

div_size = 200
img_size = div_size * 2
div1 = tk.Frame(window,  width=img_size , height=img_size , bg='blue')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='orange')
div3 = tk.Frame(window,  width=div_size , height=div_size , bg='green')

window.update()
win_size = min( window.winfo_width(), window.winfo_height())

div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)


lbl_title1 = tk.Label(div2, text='hudmiditity', bg='orange', fg='white')
lbl_title2 = tk.Label(div2, text="biosensor", bg='orange', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)

sensorlist,optionList = pos.getdata()


var = tk.StringVar(div1)
var.set(optionList[0])

bt1 = tk.OptionMenu(div3,var,*optionList)
bt1.pack(pady=10)
bt1.config(width=10, font=('Helvetica', 6))
bt1.pack(side="top")

labelTest = tk.Label(text= "", font=('Helvetica', 6), fg='red')
# labelTest.pack()  

# def callback(*args):
#     labelTest.configure(text="The selected item is {}".format(var.get()))

# var.trace("w", callback)

bt2 = tk.Button(div3, text='Button 2', bg='green', fg='white')
bt3 = tk.Button(div3, text='Button 3', bg='green', fg='white')
bt4 = tk.Button(div3, text='Button 4', bg='green', fg='white')

bt1.grid(column=0, row=0, sticky=align_mode)
bt2.grid(column=0, row=1, sticky=align_mode)
bt3.grid(column=0, row=2, sticky=align_mode)
bt4.grid(column=0, row=3, sticky=align_mode)



define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=2)
define_layout(div3, rows=4)

window.mainloop()