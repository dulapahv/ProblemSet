from tkinter import *


class test:
    def __init__(self):
        window1 = Tk()
        window1.title("test")
        b = Button(window1, text="x", height=1, width=10, font=5,
                   bg="lightgreen", command=lambda: self.press_button(12))
        b.pack()
        window1.update()
        window1.mainloop()

    def press_button(self, id):
        window = Tk()
        window.title("income and expenses")
        f1 = Frame(window)
        f2 = Frame(window)
        f3 = Frame(window)
        f3.pack(side=BOTTOM)
        f2.pack(side=BOTTOM)
        f1.pack(side=BOTTOM)
        self.Income = StringVar()
        self.Expenses = StringVar()

        Label(window, text="Please enter the amount", font=7).pack()
        Label(f1, text="Income :", font=7).pack(side=LEFT)
        Label(f2, text="Expenses :", font=7).pack(side=LEFT)
        self.In = Entry(f1)
        self.Ex = Entry(f2)
        b = Button(f3, text="Confirm", height=1, width=10, font=5,
                   bg="lightgreen", command=lambda: self.store_data(id))
        self.In.pack(side=LEFT)
        self.Ex.pack(side=LEFT)
        b.pack()
        window.update()
        window.mainloop()

    def store_data(self, id):
        self.Income = self.In.get()
        self.Expenses = self.Ex.get()
        print(self.Income)
        print(self.Expenses)
        print(id)



test()
