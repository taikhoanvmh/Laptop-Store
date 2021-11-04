from tkinter import *
from tkinter import ttk

from UI.laptopPage import laptopFrame
from UI.donHangPage import donHangFrame
from UI.thongKePage import thongKeFrame

class App(Tk):
    def __init__(self):
        super().__init__()
        self.root = self._root()
        self.geometry("600x600+400+50")
        self.title("Laptop")
        self.configure(background='white')
        #-------------------------
        self.pixelVirtual = PhotoImage(width=1, height=1)

        # ------------------------
        self.buttonFunc()
        # ------------------------
        self.now_frame = Label(self.root, font=('Roboto', 18),
                               text = "\n\n\nHệ thống quản lí \n"
                                      "cửa hàng bán laptop\n\n"
                                      "1712445 - Vũ Minh Hiếu", bg = "snow")
        self.now_frame.pack(side=TOP, fill=BOTH)

    def buttonFunc(self):

        # Khung chứa các button
        left_frame = LabelFrame(self.root, width=200, bg='gold', bd=0)
        left_frame.pack(side=TOP, fill=X)
        # ---------------------------------
        # Tạo Button
        self.b_laptop = Button(left_frame, text='Latop',
                                      command=lambda num=0: self.clickEvent(num))
        self.b_donHang = Button(left_frame, text='Đơn hàng',
                                     command=lambda num=1: self.clickEvent(num))
        self.b_thongKe = Button(left_frame, text='Thống kê',
                                         command=lambda num=2: self.clickEvent(num))
        self.b_exit = Button(left_frame, text='Thoát',
                               command=lambda : self.root.destroy())
        self.Buttons = [self.b_laptop, self.b_donHang,
                        self.b_thongKe, self.b_exit]
        for i, button in enumerate(self.Buttons):
            button.config(bd=0, image=self.pixelVirtual, font=('Roboto', 13),
                        bg='gold', activebackground='snow',
                        disabledforeground='white', activeforeground='black',
                        height=50, anchor='c', padx=10, fg='black', compound='c')
            button.pack(expand="yes", side = LEFT, fill = X)


    def clickEvent(self, num):

        # Button đc chọn sẽ đổi màu, các button còn lại set về mặc định
        for button in self.Buttons:
            button.config(bg='gold', state=NORMAL)
        self.Buttons[num].config(bg='snow', state=NORMAL)

        # Mở frame mới, huỷ frame cũ
        self.now_frame.destroy()
        if num == 0:
            self.now_frame = laptopFrame(self.root)
        elif num == 1:
            self.now_frame = donHangFrame(self.root)
        elif num == 2:
            self.now_frame = thongKeFrame(self.root)
        return True


