from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from objects.laptop import Brand

class laptopFrame(Frame):
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
        designGUI.showBrand(showFrame)



class designGUI():

    @staticmethod
    def taskbar(frame1, frame2):
        # 3 nút: lọc, tìm, thêm
        # ---------------------
        butt1 = ttk.Button(frame1, text="Lọc",
                           command= lambda: fillBr())
        butt1.pack(side = LEFT, padx= 5)
        entry1 = ttk.Entry(frame1)
        entry1.pack(side=LEFT)
        butt2 = ttk.Button(frame1, text="Tìm",
                           command= lambda: findBr())
        butt2.pack(side = LEFT, padx=5)
        butt3 = ttk.Button(frame1, text="Thêm",
                           command=lambda :addBr())
        butt3.pack(side = LEFT)

        #------------------------------
        def addBr():
            name = entry1.get().replace(" ", "")
            func.addNewBrand(name)
            entry1.delete(0, END)
            #clear frame
            for widgets in frame2.winfo_children():
                widgets.destroy()
            designGUI.showBrand(frame2)
        #------------------------------
        def findBr():
            name = entry1.get().replace(" ", "")
            entry1.delete(0, END)
            # clear frame
            for widgets in frame2.winfo_children():
                widgets.destroy()
            designGUI.showBrand(frame2, func.findBrand(name))
        #------------------------------
        def fillBr():
            # clear frame
            for widgets in frame2.winfo_children():
                widgets.destroy()
            designGUI.showBrand(frame2)

    @staticmethod
    def showBrand(frame, listBrand = None):
        # Hàm tạo frame nhỏ + button + function
        if listBrand is None:
            listBrand = func.getAllBrand()
        #------------
        for name in listBrand:
            f = ttk.LabelFrame(frame)
            ttk.Button(f, text="Xem",
                       command= lambda n=name : viewName(n)).pack(side=LEFT)
            ttk.Label(f, text=name,
                      font=("Times", 20)).pack(side=LEFT, padx = 10)
            ttk.Button(f, text="Xoá",
                       command= lambda n=name : delName(n)).pack(side=RIGHT)
            ttk.Button(f, text="Sửa",
                       command= lambda n=name : changeName(n)).pack(side=RIGHT)
            f.pack(side = TOP, fill = X, padx = 20, pady = 5)

        #--------------------
        #function inside
        def viewName(n):
            for widgets in frame.winfo_children():
                widgets.destroy()
            designGUI.showLaptop(frame, n)

        # ---------------------
        def changeName(n):
            ws = Tk()
            ws.title("Sửa tên")
            ws.geometry("100x100+450+200")
            # ---------------------------------
            Entry = ttk.Entry(ws, width=20)
            Entry.insert(END, n)
            Entry.pack(padx=3, pady=5, fill=BOTH)
            # ------------------------------
            button = ttk.Button(ws, text='Sửa',
                                command=lambda: process())
            button.pack(padx=3, pady=5, fill=BOTH)
            def process():
                func.changeBrand(n, Entry.get())
                ws.destroy()
                for widgets in frame.winfo_children():
                    widgets.destroy()
                designGUI.showBrand(frame)

        # ---------------------
        def delName(n):
            func.delBrand(n)
            for widgets in frame.winfo_children():
                widgets.destroy()
            designGUI.showBrand(frame)

    @staticmethod
    def showLaptop(frame, brand, listlap = None):
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
            if messagebox.askokcancel("Xoá", "Bạn có chắc không?"):
                if Brand.delLap(brand, n):
                    messagebox.showinfo('Chúc mừng',
                                        'Xoá thành công')
                    for widgets in frame.winfo_children():
                        widgets.destroy()
                    designGUI.showLaptop(frame, brand)
                    return True
                else:
                    messagebox.showwarning('Có lỗi',
                                           'Không xoá được')
                    return False



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
        if messagebox.askokcancel("Xoá", "Bạn có chắc không?"):
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

