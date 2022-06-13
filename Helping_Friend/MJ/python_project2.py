import time
from tkinter import *

class Main:
    def __init__(self):
        self.main = Tk()
        self.main.config(bg="light pink")
        self.seat = StringVar()
        self.main.geometry("875x700")
        self.main.option_add("*Font", "consolas 25")
        self.main.title("Home Page")
        Label(self.main, text="Welcome to MBAW Shabu", fg="purple", bg="yellow", width=50).pack()
        # all_shabu = PhotoImage(file=r'C:\Users\USER\Downloads\s_0nm1.gif')
        Label(self.main).pack()
        Label(self.main, text="How many person", fg="orange", bg="light blue").place(x=200, y=600)
        num_seat = Entry(self.main, textvariable=self.seat, width=4, justify="right")
        num_seat.place(x=500, y=600)
        num_seat.focus_set()
        Button(self.main, text="Reserve", fg="pink", bg="yellow", font="20", command=self.Categories).place(x=680, y=600)
        Label(self.main, text="Time limit=> 2hr.30min", fg="red", bg="light pink", font="18").place(x=350, y=650)
        self.main.mainloop()

    def Categories(self):
        try:
            seat = int(self.seat.get())
            if seat <= 0:
                raise ValueError
        except:
            print("Invalid input")
            exit(0)
        self.cate_window = Toplevel()
        self.cate_window.configure(bg="brown")
        self.cate_window.geometry("550x740")
        named_tuple = time.localtime()
        time_up = "Your time is end at "
        out_hour = named_tuple[3]
        out_minute = named_tuple[4]
        out_second = named_tuple[5] + 10
        if out_minute > 60:
            out_hour += 1
            out_minute -= 60
        if out_hour >= 24:
            out_hour -= 24
        time_up += time.strftime(" %d %b %Y ,", named_tuple)
        time_up += f" {out_hour:02d}:{out_minute:02d}:{out_second:02d}"
        Label(self.cate_window, text=time_up, font="15", fg="red", bg="light green").place(x=10, y=20)
        # food = PhotoImage(file=r'C:\Users\USER\Downloads\freshfood.gif')
        Label(self.cate_window).place(x=40, y=80)
        Button(self.cate_window, text="Food", fg="white", bg="black", width=7, command=Menu_food).place(x=380, y=140)
        # drink = PhotoImage(file=r'C:\Users\USER\Downloads\drink.gif')
        Label(self.cate_window).place(x=40, y=275)
        Button(self.cate_window, text="Drink", fg="white", bg="black", width=7).place(x=380, y=335)
        # dessert = PhotoImage(file=r'C:\Users\USER\Downloads\dessert.gif')
        Label(self.cate_window).place(x=40, y=470)
        Button(self.cate_window, text="Dessert", fg="white", bg="black", width=7).place(x=380, y=530)
        Label(self.cate_window, text="//This program will close after you pay your bill", fg="yellow", bg="brown",
              font=5).place(x=20, y=700)
        Button(self.cate_window, text="Bill", fg="red", bg="pink", font=15, command=self.Bill).place(x=500, y=700)
        while not (named_tuple[3] == out_hour and named_tuple[4] == out_minute and named_tuple[5] == out_second):
            named_tuple = time.localtime()
            Label(self.cate_window, text=f"Local time|{named_tuple[3]:02d}:{named_tuple[4]:02d}:{named_tuple[5]:02d}",
                  font="15", fg="black", bg="pink").place(x=400, y=20)
            self.cate_window.update()
        self.Bill()
        # bill button to stop time(close)

    def Bill(self):
        cost = 299 * int(self.seat.get())
        bill = Tk()
        bill.geometry("350x740")
        bill.configure(bg="yellow")
        Label(bill, text="Payment", fg="red", bg="yellow").place(x=150, y=10)
        Label(bill, text="Order", fg="black", bg="yellow").place(x=20, y=50)
        Label(bill, text="Quantity", fg="black", bg="yellow").place(x=220, y=50)
        Label(bill, text="Cost", fg="black", bg="yellow").place(x=300, y=50)
        Label(bill, text="all you can eat", fg="black", bg="yellow").place(x=20, y=80)
        Label(bill, text=f"{self.seat.get()}", fg="black", bg="yellow").place(x=235, y=80)
        Label(bill, text=cost, fg="black", bg="yellow").place(x=300, y=80)
        self.main.destroy()
        self.cate_window.destroy()
        


class Menu(Main):
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


class Menu_food(Menu):
    def __init__(self):
        super().__init__()
        each = 0
        self.each_food = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.food = Tk()
        self.food.config(bg="gold")
        self.food.geometry("460x610")
        Label(self.food, text="Fresh Food Menu", bg="orange", width=26, height=3, font="Broadway 20").place(x=0, y=0)
        Label(self.food, text="Name", fg="red", bg="gold", font="Times 15").place(x=15, y=100)
        Label(self.food, text="Quantity", fg="red", bg="gold", font="Times 15").place(x=350, y=100)
        y_axis = 130
        for menu in self.food_dic:
            current_food = self.food_dic[menu][0]
            Label(self.food, text=f"{current_food}", bg="gold", font="Helvetica 10").place(x=15, y=y_axis)
            self.each_food[each] = Spinbox(self.food, width=5, from_=0, to=10)
            self.each_food[each].place(x=350, y=y_axis)
            each += 1
            y_axis += 30
        Button(self.food, text="Submit", bg="light green", command=self.order_food).place(x=200, y=580)

    def order_food(self):
        self.order = Tk()
        self.order.config(bg="light blue")
        Label(self.order, text="Ordering", fg="red", bg="gold").place(x=130, y=5)
        height = 20
        for i in range(len(self.food_dic)):
            if self.each_food[i].get() != 0:
                Label(self.order, text=f"{self.food_dic[i+1][0]}", bg="light blue").place(x=20, y=height)
                Label(self.order, text=f"{self.food_dic[i+1][1]}", bg="light blue").place(x=200, y=height)
                self.food_dic[i+1][1] = self.each_food[i].get()
                height += 20
        self.food.destroy()
    
    def destroy_order_food(self):
        self.order.destroy()
        self.food.destroy()





Main()
