import time
from tkinter import *


class Main:
    def __init__(self):
        main = Tk()
        main.configure(bg="light pink")
        self.seat = StringVar()
        main.geometry("875x700")
        main.option_add("*Font", "consolas 25")
        main.title("Home Page")
        Label(main, text="Welcome to MBAW Shabu", fg="purple", bg="yellow", width=50).pack()
        image1 = PhotoImage(file=r'C:\Users\USER\Downloads\s_0nm1.gif')
        Label(main, image=image1).pack()
        Label(main, text="How many person", fg="orange", bg="light blue").place(x=200, y=600)
        num_seat = Entry(main, textvariable=self.seat, width=5)
        num_seat.place(x=500, y=600)
        num_seat.focus_set()
        Button(main, text="Reserve", fg="pink", bg="yellow", font="20", command=self.Categories).place(x=680, y=600)
        Label(main, text="Time limit=> 2hr.30min", fg="red", bg="light pink", font="18").place(x=350, y=650)
        main.mainloop()

    def Categories(self):
        try:
            seat = int(self.seat.get())
            if seat <= 0:
                raise ValueError
        except:
            print("Invalid input")
            exit(0)
        cate_window = Tk()
        cate_window.geometry("550x500")
        named_tuple = time.localtime()
        time_up = "Your time is end at "
        out_hour = named_tuple[3] + 2
        out_minute = named_tuple[4] + 30
        if out_minute > 60:
            out_hour += 1
            out_minute -= 60
        if out_hour >= 24:
            out_hour -= 24
        time_up += time.strftime(" %d %b %Y ,", named_tuple)
        time_up += f" {out_hour:02d}:{out_minute:02d}"
        Label(cate_window, text=time_up, font="15", fg="red", bg="light green").place(x=10, y=20)
        image2 = PhotoImage(file=r'C:\Users\USER\Downloads\drink1.gif')
        Label(cate_window, image=image2).place(x=50, y=100)
        while not (named_tuple[3] == out_hour and named_tuple[4] == out_minute):
            named_tuple = time.localtime()
            Label(cate_window, text=f"Local time|{named_tuple[3]:02d}:{named_tuple[4]:02d}:{named_tuple[5]:02d}",
                  font="15", fg="black", bg="pink").place(x=400, y=20)
            cate_window.update()
        exit(0)  # bill
        # end button


Main()
