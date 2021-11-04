from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class thongKeFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        Frame.config(self, bg='white')
        Frame.pack(self, side = LEFT,  fill=BOTH)
        #-----------------------------
        self.view = ttk.Treeview(self, columns = (1,2,3))
        #-----------------------------
        self.view.column('#0', width=0, stretch=NO)
        self.view.column(1, anchor=CENTER, width=100)
        self.view.column(2, anchor=CENTER, width=150)
        self.view.column(3, anchor=CENTER, width=100)
        #----------------------------
        self.view.heading('#0', text='', anchor=CENTER)
        self.view.heading(1, text="STT", anchor=CENTER)
        self.view.heading(2, text = "Tên tài khoản", anchor=CENTER)
        self.view.heading(3, text = "Quyền hạn", anchor=CENTER)
        #----------------------------
        self.showInfoUser()
        self.view.pack(side = RIGHT, fill = BOTH)

    def showInfoUser(self):
        pass