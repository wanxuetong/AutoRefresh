#coding:utf-8
#python3.9.0

#__author__ = 'Xuetong Wan'

from tkinter import *
import threading
from selenium import webdriver
import time
from playsound import playsound

def open_url():
    global driver
    driver = webdriver.Chrome('sup/chromedriver.exe')
    url = Entry_Url.get()
    driver.get(url)

def start_refresh():
    keyword = Entry_Key.get()
    logic = radio.get()
    rate = int(Entry_Sleep.get())
    
    global loop_Key 
    loop_Key = 1
    while loop_Key :
        time.sleep(rate)
        try:
            driver.refresh()
            if keyword in driver.page_source:
                if logic == 1:
                    #print('关键字被找到,成功')
                    while loop_Key:
                        playsound('sup/beep.wav')
                    break                    
                else:
                    #print('关键字被找到,失败')
                    pass
            else:
                if logic == 2:
                    #print('关键字未被找到,成功')
                    while loop_Key:
                        playsound('sup/beep.wav')
                    break                    
                else:
                    #print('关键字未被找到,失败')   
                    pass
        except Exception as e:
            #print("Exception found",format(e))
            pass
    Button_Start.config(state = 'normal')         
    
def stop_refresh():
    global loop_Key 
    loop_Key = 0    

def newthird_do():
    Button_Start.config(state = 'disabled') 
    th = threading.Thread(target=start_refresh)
    th.setDaemon(True)#守护线程
    th.start()

def on_closing():   #关闭按钮
    try:
        driver.quit() 
    except Exception as e:
        pass    
    root.destroy()
    
if __name__ == "__main__":
    root = Tk()
    root.title('自动刷新助手')
    root.geometry('320x120')
    root.resizable(width=False, height=False)
    
    l = Label(root, text='', font=('微软雅黑', 2),width=200, height=2)       #TOP
    l.pack(side=TOP)

    frm = Frame(root)       
    Label(frm, text='网站地址：', font=('微软雅黑', 10), width=9).pack(side=LEFT ) 
    var = StringVar() 
    Entry_Url = Entry(frm, textvariable = var, width=22,borderwidth=2)
    var.set('')
    Entry_Url.pack(side=LEFT)
    Label(frm, text=' ', font=('微软雅黑', 1), width=1).pack(side=LEFT ) 
    button = Button(frm, text='打开', command=open_url, width=8, height=0, font=('微软雅黑', 8),borderwidth=1).pack(side=RIGHT)
    frm.pack()  


    frm = Frame(root,borderwidth=2)       
    Label_Key=Label(frm, text='关  键  词:', font=('微软雅黑', 8), width=7)
    Label_Key.pack(side=LEFT ) 
    #var = StringVar() 
    Entry_Key = Entry(frm, width=20,borderwidth=2)
    #var.set('')
    Entry_Key.pack(side=LEFT)
    
    radio = IntVar()
    radio.set(1)
    R1 = Radiobutton(frm,  text="包含", variable=radio, value=1)
    R1.pack( anchor = W ,side=RIGHT)
    R2 = Radiobutton(frm,  text="不包含", variable=radio, value=2)
    R2.pack( anchor = W ,side=RIGHT)     

    frm.pack() 

    frm = Frame(root,borderwidth=2)       
    Label_Sleep=Label(frm, text='刷新频率:', font=('微软雅黑', 8), width=7)
    Label_Sleep.pack(side=LEFT ) 
    var = StringVar() 
    Entry_Sleep = Entry(frm, textvariable = var, width=4,borderwidth=2)
    var.set('')
    Entry_Sleep.pack(side=LEFT)
    Label(frm, text=' ', font=('微软雅黑', 1), width=10).pack(side=LEFT ) 
    Button_Start = Button(frm, text='自动刷新', command=newthird_do, width=8, height=0, font=('微软雅黑', 8),borderwidth=1)
    Button_Start.pack(side=LEFT)     
    Label(frm, text=' ', font=('微软雅黑', 1), width=1).pack(side=LEFT ) 
    Button_Stop = Button(frm, text='关闭刷新', command=stop_refresh, width=8, height=0, font=('微软雅黑', 8),borderwidth=1)
    Button_Stop.pack(side=LEFT)
    Label(frm, text=' ', font=('微软雅黑', 1), width=1).pack(side=LEFT ) 
    button = Button(frm, text='退出工具', command=on_closing, width=8, height=0, font=('微软雅黑', 8),borderwidth=1).pack(side=RIGHT)
    frm.pack() 
    
    root.mainloop()
