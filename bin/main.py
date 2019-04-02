# coding：utf-8
#author：jiguobin
from page.ws_page import WsPage
from page.ks_page import KsPage
import tkinter as tk
from tkinter import messagebox
# if __name__ == '__main__':
#     #网商进件
#     w=WsPage()
#     w.wsIncoming(9)
#     #客商进件
#     k=KsPage()
#     k.ksIncoming(5)
#     pass


window=tk.Tk()
window.title('测试进件助手')
window.geometry('450x300')

tk.Label(window, text='进件类型').place(x=80, y=20)
tk.Label(window, text='行数').place(x=220, y= 20)
tk.Label(window, text='网商进件：').place(x=80, y= 60)
tk.Label(window, text='客商进件： ').place(x=80, y= 100)
#网商的行数
ws_row= tk.StringVar()
ks_row= tk.StringVar()
tk.Entry(window,show=None,textvariable=ws_row).place(x=200,y=60)
tk.Entry(window,show=None,textvariable=ks_row).place(x=200,y=100)
def submit():
    if ws_row.get()==''and ks_row.get()=='' :
        tk.messagebox.showwarning(title='提示', message='请输入行数')  #错误提示
    elif ws_row.get()!='':
        w=WsPage()
        w.wsIncoming(int(ws_row.get()))
        k=KsPage()
        print(type(ks_row.get()))
        k.ksIncoming(int(ks_row.get()))
    # elif ks_row.get()!='':
    #     k=KsPage()
    #     print(type(ks_row.get()))
    #     k.ksIncoming(int(ks_row.get()))
sub=tk.Button(window,text='进件',bg='green',width=5,height=1,command=submit).place(x=160,y=160)

window.mainloop()


