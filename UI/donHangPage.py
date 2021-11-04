from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from objects.laptop import Brand
from objects.bill import Bill

class donHangFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        Frame.config(self, bg='snow' )
        Frame.pack(self, expand = 'yes', fill=BOTH, pady = 5)
        #-----------------------------
        #Chia frame
        taskFrame = ttk.Frame(self)
        taskFrame.pack(side = TOP, fill= X)
        showFrame = ttk.Frame(self)
        showFrame.pack(side = TOP, fill = BOTH, pady= 5)
        #----------------------------
        designGUI.taskbar(taskFrame, showFrame)
        #designGUI.showBillbyMont(showFrame, 'Tháng 5')


class designGUI():

    @staticmethod
    def taskbar(frame1, frame2):
        #2 nút: lọc theo tháng và thêm
        # ------------------------------
        mon = StringVar()
        month = ["Tháng 5","Tháng 6","Tháng 7","Tháng 8"]
        ttk.Label(frame1, text='Tháng'
                  ).pack(padx=5, side = LEFT)
        monthBox = ttk.OptionMenu(frame1,mon, *month,
                             command= lambda m=mon.get():selected(m))
        monthBox.pack(padx=5, side = LEFT)
        # -------------------------------
        butt1 = ttk.Button(frame1, text="Thêm",
                           command=lambda : addBill())
        butt1.pack(padx = 10, side = RIGHT)
        #------------------------------
        def selected(month):
            # clear frame
            for widgets in frame2.winfo_children():
                widgets.destroy()
            designGUI.showBillbyMont(frame2,month)
        #------------------------------
        def addBill():
            designGUI.addBillFrame()
            #clear frame
            #for widgets in frame2.winfo_children():
                #widgets.destroy()
            #designGUI.showBillbyMont(frame2)

    @staticmethod
    def showBillbyMont(frame, month):
        # Hàm tạo frame nhỏ + button + function
        listBills = Bill.getBillByMonth(month)
        #------------
        for bill in listBills:
            f = ttk.LabelFrame(frame)
            ttk.Label(f, text=bill.day + "." + bill.month,
                      font=("Times", 20)).pack(side=LEFT, padx = 10)
            ttk.Button(f, text="Xoá",
                       command= lambda b=bill : delBill(b)).pack(side=RIGHT)
            ttk.Button(f, text="Sửa",
                       command= lambda b=bill : viewBill(b)).pack(side=RIGHT)
            f.pack(side = TOP, fill = X, padx = 20, pady = 5)

        #--------------------
        #function inside
        def viewBill(n):
            pass

        # ---------------------
        def delBill(n):
            pass

    @staticmethod
    def addBillFrame():
        ws = Tk()
        ws.title('Thêm đơn hàng')
        ws.geometry("500x350+450+200")
        # ---------------------------------
        ttk.Label(ws, text='Tên'
                  ).pack(padx=3, pady=5, fill=BOTH)
        Entry1 = ttk.Entry(ws)
        Entry1.pack(padx=3, pady=5, fill = BOTH)
        # ------------------------------
        ttk.Label(ws, text='Địa chỉ'
                  ).pack(padx=3, pady=5, fill=BOTH)
        Entry2 = ttk.Entry(ws)
        Entry2.pack(padx=3, pady=5, fill=BOTH)
        # ------------------------------
        ttk.Label(ws, text='Số điện thoại'
                  ).pack(padx=3, pady=5, fill=BOTH)
        Entry3 = ttk.Entry(ws)
        Entry3.pack(padx=3, pady=5, fill=BOTH)
        #-------------------------------
        optionBrand = Brand.getAllInfo()
        optionMonth = ["Tháng 5","Tháng 6","Tháng 7","Tháng 8" ]
        b1 = StringVar()
        b2 = StringVar()
        lap1 = StringVar()
        lap2 = StringVar()
        mon = StringVar()

        # ------------------------------
        frame0 = ttk.Frame(ws)
        frame0.pack(padx=3, pady=5, fill=BOTH, side=TOP)
        ttk.Label(frame0, text='Ngày'
                  ).pack(padx=3, pady=5, side = LEFT)
        Entry4 = ttk.Entry(frame0)
        Entry4.pack(padx=3, pady=5, side=LEFT)
        monthBox = ttk.Combobox(frame0, values=optionMonth,
                                state='readonly',
                                textvariable=mon)
        monthBox.pack(padx=3, pady=5, side=LEFT)
        #-------------------------------
        frame1 = ttk.Frame(ws)
        frame1.pack(padx=3, pady=5, fill=BOTH, side=TOP)
        ttk.Label(frame1, text='Hãng'
                  ).pack(padx=3, pady=5, side=LEFT)
        choose1 = ttk.OptionMenu(frame1,b1, *optionBrand,
                             command= lambda brand=b1.get():selected1(brand))
        choose1.pack(side = LEFT, padx= 10)
        choose2 = ttk.Combobox(frame1,
                              state='disabled',
                              textvariable=lap1)
        choose2.pack(padx=3, pady=5, side=LEFT)
        ttk.Label(frame1, text='Số lượng'
                  ).pack(padx=3, pady=5, side=LEFT)
        choose3 = ttk.Entry(frame1, state='disabled')
        choose3.pack(padx=3, pady=5, side=LEFT)
        #================================
        # -------------------------------
        frame2 = ttk.Frame(ws)
        frame2.pack(padx=3, pady=5, fill=BOTH, side=TOP)
        ttk.Label(frame2, text='Hãng'
                  ).pack(padx=3, pady=5, side=LEFT)
        choose4 = ttk.OptionMenu(frame2, b2, *optionBrand,
                                 command=lambda brand=b2.get(): selected2(brand))
        choose4.pack(side=LEFT, padx=10)
        choose5 = ttk.Combobox(frame2,
                               state='disabled',
                               textvariable=lap2)
        choose5.pack(padx=3, pady=5, side=LEFT)
        ttk.Label(frame2, text='Số lượng'
                  ).pack(padx=3, pady=5, side=LEFT)
        choose6 = ttk.Entry(frame2, state='disabled')
        choose6.pack(padx=3, pady=5, side=LEFT)

        # ---------------------------------

        button = ttk.Button(ws, text='Thêm',
                            command=lambda: add())
        button.pack(padx=3, pady=5, fill=BOTH)

        # ---------------------------------
        def selected1(brand):
            laps = Brand.getAllLap(brand)
            choose2.config(values=laps, state='readonly')
            choose3.config(state='normal')

        def selected2(brand):
            laps = Brand.getAllLap(brand)
            choose5.config(values=laps, state='readonly')
            choose6.config(state='normal')

        def add():
            info = {}
            try:
                info["Name"] = Entry1.get()
                info["Loc"] = Entry2.get()
                info["Phone"] = Entry3.get()
                info["day"] = Entry4.get()
                info["month"] = monthBox.get()
                id1 = Brand.getIDLap(b1.get(),lap1.get())
                info["product1"] = id1 + choose3.get()
                if choose6.get() != "":
                    id2 = Brand.getIDLap(b2.get(),lap2.get())
                    info["product2"] = id2 + choose6.get()
                if Bill.addNewBill(info):
                    messagebox.showinfo("","Thêm hoá đơn thành công")
                    ws.destroy()
                    return True
            except:
                messagebox.showwarning('Có lỗi',
                                   'Không thể thêm hoá đơn')
                ws.destroy()
                return False
            ws.destroy()
            return False

    @staticmethod
    def showBill(frame, brand, listlap = None):
        if listlap is None:
            listlap = func.getListLaptop(brand)
        # ------------
        for name in listlap:
            f = ttk.LabelFrame(frame)
            ttk.Label(f, text=name,
                      font=("Times", 20)).pack(side=LEFT, padx=10)
            ttk.Button(f, text="Xoá",
                       command=lambda n=name: delLap(n)).pack(side=RIGHT)
            ttk.Button(f, text="Sửa",
                       command=lambda n=name: changeLap(n)).pack(side=RIGHT)
            f.pack(side=TOP, fill=X, padx=20, pady=5)

        # ---------------------
        def changeLap(n):
            pass
        # ---------------------
        def delLap(n):
            pass

class func():

    @staticmethod
    def addNewBrand(name: str):
        if name == "":
            messagebox.showwarning('Có lỗi',
                                   'Sai cú pháp')
            return False
        if Brand.addBrand(name):
            messagebox.showinfo('Chúc mừng',
                                'Thêm thành công')
            return True
        else:
            messagebox.showwarning('Có lỗi',
                               'Tên hãng đã tồn tại')
        return False

    @staticmethod
    def findBrand(name: str):
        #---------------------
        #Xử lí word search
        n = [name, name.upper(), name.lower(), name[0:2]]
        #---------------------
        listBrand = Brand.getAllInfo()
        result = []
        for brand in listBrand:
            for ni in n:
                if brand.upper().find(ni) != -1:
                    result.append(brand)
                    break
        return result

    @staticmethod
    def getAllBrand():
        return Brand.getAllInfo()

    @staticmethod
    def delBrand(name):
        if Brand.deleteBrand(name):
            messagebox.showinfo('Chúc mừng',
                                'Xoá thành công')
            return True
        else:
            messagebox.showwarning('Có lỗi',
                                   'Không xoá được')
            return False

    @staticmethod
    def changeBrand(oldname, newname):
        if Brand.fixName(oldname, newname):
            messagebox.showinfo('Chúc mừng',
                                'Sửa thành công')
            return True
        messagebox.showwarning('Có lỗi',
                               'Không thể sửa')
        return True

    @staticmethod
    def getListLaptop(brand):
        return Brand.getAllLap(brand)

