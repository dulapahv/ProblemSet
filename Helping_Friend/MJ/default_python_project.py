import time
from tkinter import *
import tkinter.messagebox
import abc
from abc import ABC

total_order = {}


class Menu(ABC):
    def __init__(self):
        self.food_dic = {1: ["bacon", 0], 2: ["Pork loin slice", 0], 3: ["Pork belly slice", 0], 4: ["Shrimp", 0],
                         5: ["Pork Liver", 0], 6: ["Fish dumpling", 0], 7: ["Beef slice", 0], 8: ["Fish tofu", 0],
                         9: ["Fish ball", 0], 10: ["Squid", 0], 11: ["Jelly fish", 0], 12: ["Japanese mushroom", 0],
                         13: ["Egg tofu", 0], 14: ["Sweet corn", 0], 15: ["Grass noodle", 0]}
        self.drink_dic = {1: ["mineral water", 0], 2: ["Chrysanthemum tea", 0], 3: ["hot jasmine tea", 0],
                          4: ["Coke", 0], 5: ["Orange fanta", 0], 6: ["Sprite", 0], 7: ["Lemon tea", 0]}
        self.dessert_dic = {1: ["Thai tea ice cream", 0], 2: ["Mung bean thai custard", 0],
                            3: ["Toddy palm in milk shake", 0], 4: ["Matcha latte ice cream", 0],
                            5: ["coconut milk ice cream", 0]}

    @abc.abstractmethod
    def ordered(self):
        pass


class Menu_food(Menu):
    def __init__(self):
        super().__init__()
        each = 0
        self.each_food = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.food = Tk()
        self.food.config(bg="light green")
        self.food.title("Menu Food")
        self.food.geometry("460x610")
        Label(self.food, text="Fresh Food Menu", bg="orange", width=26, height=3, font="Broadway 20").place(x=0, y=0)
        Label(self.food, text="Menu", fg="red", bg="gold", font="Times 15").place(x=15, y=100)
        Label(self.food, text="Quantity", fg="red", bg="gold", font="Times 15").place(x=340, y=100)
        y_axis = 130
        for menu in self.food_dic:
            current_food = self.food_dic[menu][0]
            Label(self.food, text=f"{current_food}", bg="light green", font="Helvetica 10").place(x=15, y=y_axis)
            self.each_food[each] = Spinbox(self.food, width=5, from_=0, to=10)
            self.each_food[each].place(x=350, y=y_axis)
            each += 1
            y_axis += 30
        Button(self.food, text="Submit", bg="light blue", command=self.ordered).place(x=200, y=580)

    def exit_food(self):
        self.order.destroy()

    def ordered(self):
        if in_time == 0:
            self.order = Tk()
            self.order.title("Ordering Food")
            self.order.config(bg="light blue")
            self.order.geometry("300x370")
            Label(self.order, text="Ordering", fg="blue", bg="yellow green").place(x=125, y=5)
            height = 30
            for i in range(len(self.food_dic)):
                if int(self.each_food[i].get()) != 0:
                    Label(self.order, text=f"{self.food_dic[i + 1][0]}", bg="light blue").place(x=20, y=height)
                    self.food_dic[i + 1][1] = int(self.each_food[i].get())
                    Label(self.order, text=f"{self.food_dic[i + 1][1]}", bg="light blue").place(x=240, y=height)
                    if self.food_dic[i + 1][0] not in total_order:
                        total_order[self.food_dic[i + 1][0]] = int(self.each_food[i].get())
                    else:
                        for each in total_order:
                            if each == self.food_dic[i + 1][0]:
                                total_order[each] += int(self.each_food[i].get())
                    height += 20
            self.food.destroy()
            Button(self.order, text="Close", bg="DarkSeaGreen1", command=self.exit_food).place(x=125, y=340)
        else:
            tkinter.messagebox.showerror(title="Time up!", message="Sorry! Time is already over")
            self.food.destroy()


class Menu_drink(Menu):
    def __init__(self):
        super().__init__()
        each = 0
        self.each_drink = [0, 0, 0, 0, 0, 0, 0]
        self.drink = Tk()
        self.drink.config(bg="light green")
        self.drink.title("Menu Drink")
        self.drink.geometry("460x610")
        Label(self.drink, text="Drink Menu", bg="orange", width=26, height=3, font="Broadway 20").place(x=0, y=0)
        Label(self.drink, text="Menu", fg="purple", bg="light green", font="Times 15").place(x=15, y=100)
        Label(self.drink, text="Quantity", fg="purple", bg="light green", font="Times 15").place(x=340, y=100)
        y_axis = 130
        for menu in self.drink_dic:
            current_drink = self.drink_dic[menu][0]
            Label(self.drink, text=f"{current_drink}", bg="light green", font="Helvetica 10").place(x=15, y=y_axis)
            self.each_drink[each] = Spinbox(self.drink, width=5, from_=0, to=10)
            self.each_drink[each].place(x=350, y=y_axis)
            each += 1
            y_axis += 30
        Button(self.drink, text="Submit", bg="light blue", command=self.ordered).place(x=200, y=580)

    def exit_drink(self):
        self.order2.destroy()

    def ordered(self):
        if in_time == 0:
            self.order2 = Tk()
            self.order2.title("Ordering Drink")
            self.order2.config(bg="pink")
            self.order2.geometry("300x350")
            Label(self.order2, text="Ordering", fg="red", bg="gold").place(x=125, y=5)
            height = 30
            for i in range(len(self.drink_dic)):
                if int(self.each_drink[i].get()) != 0:
                    Label(self.order2, text=f"{self.drink_dic[i + 1][0]}", bg="pink").place(x=20, y=height)
                    self.drink_dic[i + 1][1] = int(self.each_drink[i].get())
                    Label(self.order2, text=f"{self.drink_dic[i + 1][1]}", bg="pink").place(x=240, y=height)
                    if self.drink_dic[i + 1][0] not in total_order:
                        total_order[self.drink_dic[i + 1][0]] = int(self.each_drink[i].get())
                    else:
                        for each in total_order:
                            if each == self.drink_dic[i + 1][0]:
                                total_order[each] += int(self.each_drink[i].get())
                    height += 20
            self.drink.destroy()
            Button(self.order2, text="Close", bg="DarkSeaGreen1", command=self.exit_drink).place(x=125, y=320)
        else:
            tkinter.messagebox.showerror(title="Time up!", message="Sorry! Time is already over")
            self.drink.destroy()


class Menu_dessert(Menu):
    def __init__(self):
        super().__init__()
        each = 0
        self.each_dessert = [0, 0, 0, 0, 0]
        self.dessert = Tk()
        self.dessert.config(bg="light green")
        self.dessert.title("Menu Dessert")
        self.dessert.geometry("460x610")
        Label(self.dessert, text="Dessert Menu", bg="orange", width=26, height=3, font="Broadway 20").place(x=0, y=0)
        Label(self.dessert, text="Menu", fg="purple", bg="light green", font="Times 15").place(x=15, y=100)
        Label(self.dessert, text="Quantity", fg="purple", bg="light green", font="Times 15").place(x=340, y=100)
        y_axis = 130
        for menu in self.dessert_dic:
            current_dessert = self.dessert_dic[menu][0]
            Label(self.dessert, text=f"{current_dessert}", bg="light green", font="Helvetica 10").place(x=15, y=y_axis)
            self.each_dessert[each] = Spinbox(self.dessert, width=5, from_=0, to=10)
            self.each_dessert[each].place(x=350, y=y_axis)
            each += 1
            y_axis += 30
        Button(self.dessert, text="Submit", bg="light blue", command=self.ordered).place(x=200, y=580)

    def exit_dessert(self):
        self.order3.destroy()

    def ordered(self):
        if in_time == 0:
            self.order3 = Tk()
            self.order3.title("Ordering Dessert")
            self.order3.config(bg="light green")
            self.order3.geometry("300x350")
            Label(self.order3, text="Ordering", fg="purple", bg="light blue").place(x=125, y=5)
            height = 30
            for i in range(len(self.dessert_dic)):
                if int(self.each_dessert[i].get()) != 0:
                    Label(self.order3, text=f"{self.dessert_dic[i + 1][0]}", bg="light green").place(x=20, y=height)
                    self.dessert_dic[i + 1][1] = int(self.each_dessert[i].get())
                    Label(self.order3, text=f"{self.dessert_dic[i + 1][1]}", bg="light green").place(x=240, y=height)
                    if self.dessert_dic[i + 1][0] not in total_order:
                        total_order[self.dessert_dic[i + 1][0]] = int(self.each_dessert[i].get())
                    else:
                        for each in total_order:
                            if each == self.dessert_dic[i + 1][0]:
                                total_order[each] += int(self.each_dessert[i].get())
                    height += 20
            self.dessert.destroy()
            Button(self.order3, text="Close", bg="light blue", command=self.exit_dessert).place(x=125, y=320)
        else:
            tkinter.messagebox.showerror(title="Time up!", message="Sorry! Time is already over")
            self.dessert.destroy()


def out_pro():  # exit when finish bill
    exit(0)


in_time = 0


class Main:
    def __init__(self):
        self.time = 0
        self.total_order = {}
        self.main = Tk()
        self.main.config(bg="#4c3723")
        self.seat = StringVar()
        self.main.geometry("875x700")
        self.main.option_add("*Font", "consolas 25")
        self.main.title("Home Page of MuMu Shabu")
        Label(self.main, text="Welcome to MuMu Shabu", fg="#5E454B", bg="#F3F0D7", width=50).pack()
        all_shabu = PhotoImage(file=r'C:\Users\USER\Downloads\Myshabu.gif')
        Label(self.main, image=all_shabu).pack()
        Label(self.main, text="How many person:", fg="light goldenrod", bg="#4c3723").place(x=200, y=600)
        num_seat = Entry(self.main, textvariable=self.seat, width=4, justify="right")
        num_seat.place(x=500, y=600)
        num_seat.focus_set()
        Button(self.main, text="Reserve", fg="#8f512c", bg="light goldenrod", font="20", command=self.Categories).place(
            x=680, y=600)
        Label(self.main, text="Time limit: 2hr.30min", fg="light goldenrod", bg="#4c3723", font="18").place(x=350,
                                                                                                            y=650)
        self.main.mainloop()

    def Bill(self):
        global in_time
        in_time = 1
        self.main.destroy()
        cost = 299 * int(self.seat.get())
        bill = Tk()
        bill.title("Bill of Buffet")
        k = 100 + (20 * len(total_order)) + 100
        bill.geometry(f"370x{k}")
        bill.configure(bg="DarkSeaGreen1")
        Label(bill, text="Payment", fg="deep sky blue", bg="DarkSeaGreen2", font="Times 15").place(x=145, y=10)
        Label(bill, text="Order", fg="brown", bg="DarkSeaGreen1", font="Broadway").place(x=20, y=50)
        Label(bill, text="Quantity", fg="brown", bg="DarkSeaGreen1", font="Broadway").place(x=210, y=50)
        Label(bill, text="Cost", fg="brown", bg="DarkSeaGreen1", font="Broadway").place(x=315, y=50)
        height = 80
        for all_menu in total_order:
            Label(bill, text=f"{all_menu}", fg="black", bg="DarkSeaGreen1").place(x=20, y=height)
            Label(bill, text=f"{total_order[all_menu]}", fg="black", bg="DarkSeaGreen1").place(x=238, y=height)
            Label(bill, text=0, fg="black", bg="DarkSeaGreen1").place(x=325, y=height)
            height += 20
        Label(bill, text="MuMu Shabu", fg="black", bg="DarkSeaGreen1").place(x=20, y=height + 20)
        Label(bill, text=f"{self.seat.get()}", fg="black", bg="DarkSeaGreen1").place(x=238, y=height + 20)
        Label(bill, text=cost, fg="black", bg="DarkSeaGreen1").place(x=323, y=height + 20)
        Label(bill, text="Total Cost", fg="black", bg="DarkSeaGreen1").place(x=20, y=height + 40)
        Label(bill, text=cost, fg="black", bg="DarkSeaGreen1").place(x=323, y=height + 40)
        Button(bill, text="Finish", fg="pink", bg="brown", command=out_pro).place(x=160, y=k - 30)  # finish the bill

    def Categories(self):
        try:
            seat = int(self.seat.get())
            if seat <= 0:
                raise ValueError
        except:
            tkinter.messagebox.showerror(title="Error", message="Invalid input")
            exit(0)
        self.cate_window = Toplevel()
        self.cate_window.configure(bg="#4c3723")
        self.cate_window.title("Categories")
        self.cate_window.geometry("550x740")
        named_tuple = time.localtime()
        time_up = "Your time is end at "
        out_hour = named_tuple[3]
        out_minute = named_tuple[4] + 10
        out_second = named_tuple[5]
        if out_minute >= 60:
            out_hour += 1
            out_minute -= 60
        if out_hour >= 24:
            out_hour -= 24
        time_up += time.strftime(" %d %b %Y ,", named_tuple)
        time_up += f" {out_hour:02d}:{out_minute:02d}:{out_second:02d}"
        Label(self.cate_window, text=time_up, font="15", fg="gold", bg="#4c3723").place(x=10, y=20)
        food = PhotoImage(file=r'C:\Users\USER\Downloads\freshfood.gif')
        Label(self.cate_window, image=food).place(x=40, y=80)
        Button(self.cate_window, text="Food", fg="#8f512c", bg="light goldenrod", borderwidth=4, relief="raised",
               width=7, command=Menu_food).place(x=380, y=140)
        drink = PhotoImage(file=r'C:\Users\USER\Downloads\drink.gif')
        Label(self.cate_window, image=drink).place(x=40, y=275)
        Button(self.cate_window, text="Drink", fg="#8f512c", bg="light goldenrod", borderwidth=4, relief="raised",
               width=7, command=Menu_drink).place(x=380, y=335)
        dessert = PhotoImage(file=r'C:\Users\USER\Downloads\dessert.gif')
        Label(self.cate_window, image=dessert).place(x=40, y=470)
        Button(self.cate_window, text="Dessert", fg="#8f512c", bg="light goldenrod", borderwidth=4, relief="raised",
               width=7, command=Menu_dessert).place(x=380, y=530)
        Label(self.cate_window, text="//This program will close after you pay your bill", fg="yellow", bg="#4c3723",
              font=5).place(x=20, y=700)
        Button(self.cate_window, text="Bill", fg="red", bg="light goldenrod", font=15, borderwidth=4, relief="raised",
               command=self.break_time).place(x=500, y=700)
        while not ((named_tuple[3] == out_hour and named_tuple[4] == out_minute and named_tuple[5] == out_second) or self.time == 1):
            named_tuple = time.localtime()
            Label(self.cate_window, text=f"Local time|{named_tuple[3]:02d}:{named_tuple[4]:02d}:{named_tuple[5]:02d}",
                  font="15", fg="gold", bg="#4c3723").place(x=400, y=20)
            self.cate_window.update()
        self.Bill()

    def break_time(self):
        self.time = 1


Main()
