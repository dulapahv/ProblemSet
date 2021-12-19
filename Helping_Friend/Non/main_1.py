from tkinter import *
from tkinter import messagebox


class Healty:
    # main menu
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x100")
        self.window.title("HEALTH Calculater")
        l1 = Label(
            self.window, text=" Select function ", font=("Bahnschrift", 12)
        ).grid(row=0, column=2, columnspan=1)
        b1 = Button(self.window, text="BMI Cal", command=lambda:BMI.main_bmi(self)).grid(
            row=3, column=0, s="NSEW", columnspan=2
        )
        b2 = Button(self.window, text="Record Activities").grid(
            row=3, column=3, s="NSEW", columnspan=3
        )
        b3 = Button(self.window, text="TDEE Cal").grid(
            row=3, column=2, s="NSEW", columnspan=1
        )
        b4 = Button(self.window, text="Quit", command=self.window.destroy).grid(
            row=4, column=2, s="NSEW", columnspan=1
        )
        self.window.mainloop()


# function of BMI Button
class BMI:
    def main_bmi(self):
        # Storing weight height age
        self.w_var = DoubleVar()
        self.h_var = DoubleVar()
        self.mainbt = Tk()
        self.mainbt.title("BMI_Cal")
        self.mainbt.geometry("400x200")
        l_headline = Label(
            self.mainbt, text="BMI Calculater", font=("Bahnschrift", 10)
        ).grid(row=0, column=1, columnspan=2)
        l2 = Label(self.mainbt, text="Weight(Kg)", font=("Bahnschrift", 10)).grid(
            row=1, column=1, columnspan=1
        )
        self.e_weight = Entry(self.mainbt, textvariable=self.w_var)
        l3 = Label(self.mainbt, text="Height(m)", font=("Bahnschrift", 10)).grid(
            row=2, column=1, columnspan=1
        )
        self.e_height = Entry(self.mainbt, textvariable=self.h_var)
        b1 = Button(self.mainbt, text="Calculate", command=lambda:cal_bmi.bmi_cal(self)).grid(
            row=4, column=2, s="NSEW"
        )
        b2 = Button(self.mainbt, text="Quit", command=self.mainbt.destroy).grid(
            row=5, column=2, s="NSEW"
        )
        self.e_weight.grid(row=1, column=2)
        self.e_height.grid(row=2, column=2)


class cal_bmi(BMI):
    def bmi_cal(self):
        try:
            self.w = float(self.e_weight.get())
            self.h = float(self.e_height.get())
        except:
            print("Invalid value,try again.....")
        self.w = float(self.e_weight.get())
        self.h = float(self.e_height.get())
        print(">>>>Info Input of User<<<<")
        print(f"User weight: {self.w} ")
        print(f"User height: {self.h}")
        try:
            self.result = self.w / (self.h * self.h)
        except:
            print("Invalid value, try again.....")
        self.result = self.w / (self.h * self.h)
        if self.result < 18 and self.result >= 0:
            self.range = "Underweight"
        elif self.result < 18.5 and self.result >= 0:
            self.range = "Thin for height"
        elif self.result >= 18.6 and self.result <= 24.9:
            self.range = "Healthy Weight"
        elif self.result >= 25 and self.result <= 29.9:
            self.range = "Over weight"
        elif self.result > 30 and self.result >= 0:
            self.range = "Obesity"
        print(f"User BMI: {self.result:.2f} ")
        print(f"User range: {self.range} ")
        display_bmi.display_bmi(self)


class display_bmi(cal_bmi):
    def display_bmi(self):
        self.window_result = Tk()
        self.window_result.title("Result")
        l1 = Label(self.window_result, text=self.range, font=("Bahnschrift", 12)).grid(
            row=0, column=2, columnspan=2
        )
        b1 = Button(
            self.window_result, text="Quit", command=self.window_result.destroy
        ).grid(row=4, column=2, columnspan=2, s="NSEW")


d = Healty()
