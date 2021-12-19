from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# main menu
class Healty:
    def __init__(self):
        self.window_main = Tk()
        self.window_main.title("Welcome :)")
        self.window_main.geometry("270x100")
        self.window_main.configure(bg="#ffd39b")
        l1 = Label(self.window_main, text="Username", font=("Bahnschrift", 10))
        self.user = StringVar()
        e_user = Entry(self.window_main, textvariable=self.user)
        b_login = Button(
            self.window_main,
            text="Login",
            command=lambda: main_menu.menu_function(self),
        )
        b_quit = Button(self.window_main, text="Quit", command=self.window_main.destroy)
        l1.grid(row=0, column=0, columnspan=1)
        l1.configure(bg="#ffd39b", fg="#cd661d")
        e_user.grid(row=0, column=1)
        e_user.configure(bg="#d6d6d6", fg="#528b8b")
        b_login.grid(row=1, column=1, s="NSEW")
        b_login.configure(bg="#b4eeb4")
        b_quit.grid(row=2, column=1, s="NSEW")
        b_quit.configure(bg="IndianRed2")
        self.window_main.mainloop()


class main_menu(Healty):
    # function menu
    def menu_function(self):
        self.window = Tk()
        self.window.geometry("270x100")
        self.window.title("Main menu")
        self.window.configure(bg="#ffebcd")
        l1 = Label(self.window, text="Welcome!", font=("Bahnschrift", 12))
        l1.grid(row=0, column=1, columnspan=1)
        l1.configure(bg="#ffebcd")
        try:
            user = self.user.get()
        except:
            print("Error, try again.....")
        user = self.user.get()
        l_name = Label(self.window, text=user, font=("Bahnschrift", 12))
        l_name.grid(row=0, column=2, columnspan=2)
        l_name.configure(bg="#ffebcd", fg="#1874cd")
        b1 = Button(
            self.window, text="BMI Calculator", command=lambda: BMI.main_bmi(self)
        )
        b1.grid(row=3, column=1, s="NSEW", columnspan=1)
        b1.configure(bg="#ffb6c1")
        b2 = Button(self.window, text="BAC", command=lambda: BAC.main_bac(self))
        b2.grid(row=4, column=1, s="NSEW", columnspan=1)
        b2.configure(bg="#66cdaa")
        b3 = Button(
            self.window, text="TDEE Calculator", command=lambda: TDEE.main_tdee(self)
        )
        b3.grid(row=3, column=2, s="NSEW", columnspan=2)
        b3.configure(bg="#ffec8b")
        b4 = Button(self.window, text="Quit", command=self.window.destroy)
        b4.grid(row=4, column=2, s="NSEW", columnspan=2)
        b4.configure(bg="IndianRed2")
        print(">>>>Info of user<<<<")
        print(f"Username: {user}")


# function of BMI Button
class BMI:
    def main_bmi(self):
        # Storing weight height age
        self.w_var = DoubleVar()
        self.h_var = DoubleVar()
        self.main_b = Tk()
        self.main_b.title("BMI_Cal")
        self.main_b.geometry("400x200")
        self.main_b.configure(bg="#ffe1ff")
        print(">>>>BMI Calculator<<<<")
        l_headline = Label(self.main_b, text="BMI Calculator", font=("Bahnschrift", 10))
        l_headline.grid(row=0, column=1, columnspan=3)
        l_headline.configure(bg="#ffe1ff", fg="#7a378b")
        l2 = Label(self.main_b, text="Weight(Kg)", font=("Bahnschrift", 10))
        l2.grid(row=1, column=1, columnspan=1)
        l2.configure(bg="#ffe1ff", fg="#7a378b")
        self.e_weight = Entry(self.main_b, textvariable=self.w_var)
        l3 = Label(self.main_b, text="Height(m)", font=("Bahnschrift", 10))
        l3.grid(row=2, column=1, columnspan=1)
        l3.configure(bg="#ffe1ff", fg="#7a378b")
        self.e_height = Entry(self.main_b, textvariable=self.h_var)
        b1 = Button(
            self.main_b, text="Calculate", command=lambda: cal_bmi.bmi_cal(self)
        )
        b1.grid(row=4, column=2, s="NSEW")
        b1.configure(bg="#b4eeb4")
        b2 = Button(self.main_b, text="Quit", command=self.main_b.destroy)
        b2.grid(row=5, column=2, s="NSEW")
        b2.configure(bg="IndianRed2")
        self.e_weight.grid(row=1, column=2)
        self.e_weight.configure(bg="#d8bfd8", fg="#7a378b")
        self.e_height.grid(row=2, column=2)
        self.e_height.configure(bg="#d8bfd8", fg="#7a378b")


class cal_bmi(BMI):
    def bmi_cal(self):
        self.range = StringVar()
        try:
            self.w = float(self.e_weight.get())
            self.h = float(self.e_height.get())
        except ValueError:
            print("Invalid value,try again.....")
        self.w = float(self.e_weight.get())
        self.h = float(self.e_height.get())
        print(f"Weight: {self.e_weight} cm ")
        print(f"Height: {self.e_height} cm")
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
        display_bmi.bmi_display(self)


class display_bmi(cal_bmi):
    def bmi_display(self):
        self.window_result = Tk()
        self.window_result.title("Result")
        self.window_result.configure(bg="#ffe1ff")
        l1 = Label(self.window_result, text=self.range, font=("Bahnschrift", 12))
        l1.grid(row=0, column=2, columnspan=2)
        l1.configure(bg="#ffe1ff", fg="#7a378b")
        b1 = Button(
            self.window_result, text="Close", command=self.window_result.destroy
        )
        b1.grid(row=1, column=2, columnspan=2, s="NSEW")
        b1.configure(bg="IndianRed2")


class TDEE:
    def main_tdee(self):
        self.activity_var = StringVar()
        self.sex_var = StringVar()
        self.age_var = IntVar()
        self.weight_var = IntVar()
        self.height_var = IntVar()
        self.main_t = Tk()
        self.main_t.title("TDEE Calculator")
        self.main_t.geometry("400x200")
        self.main_t.configure(bg="#ffffe0")
        print(">>>>TDEE Calculator<<<<")
        l_headline1 = Label(
            self.main_t, text="TDEE Calculator", font=("Bahnschrift", 12)
        )
        l_sex = Label(self.main_t, text="Sex", font=("Bahnschrift", 10))
        l_age = Label(self.main_t, text="Age", font=("Bahnschrift", 10))
        l_weight = Label(self.main_t, text="Weight(Kg)", font=("Bahnschrift", 10))
        l_height = Label(self.main_t, text="Height(cm)", font=("Bahnschrift", 10))
        l_activity = Label(self.main_t, text="Activities", font=("Bahnschrift", 10))
        self.activities_box = ttk.Combobox(
            self.main_t, width=20, textvariable=self.activity_var
        )
        self.sex_box = ttk.Combobox(self.main_t, width=20, textvariable=self.sex_var)
        self.e_age = Entry(self.main_t, textvariable=self.age_var)
        self.e_weight = Entry(self.main_t, textvariable=self.weight_var)
        self.e_height = Entry(self.main_t, textvariable=self.height_var)
        b_cal = Button(
            self.main_t, text="Calculate", command=lambda: cal_tdee.cal_t(self)
        )
        b_quit = Button(self.main_t, text="Quit", command=self.main_t.destroy)
        self.activities_box["values"] = (
            " Never",
            " 1-2 times per week",
            " 3-5 times per week",
            " 6-7 times per week",
            " 2 times per day",
        )
        self.sex_box["values"] = (" Male", " Female")
        l_activity.grid(row=1, column=0, columnspan=1)
        l_activity.configure(bg="#ffffe0", fg="#8b8b00")
        self.activities_box.grid(row=1, column=1, columnspan=1)
        l_headline1.grid(row=0, column=1, columnspan=2)
        l_headline1.configure(bg="#ffffe0", fg="#8b8b00")
        l_sex.grid(row=2, column=0, columnspan=1)
        l_sex.configure(bg="#ffffe0", fg="#8b8b00")
        self.sex_box.grid(row=2, column=1, columnspan=1)
        l_age.grid(row=3, column=0, columnspan=1)
        l_age.configure(bg="#ffffe0", fg="#8b8b00")
        self.e_age.grid(row=3, column=1, columnspan=1)
        self.e_age.configure(bg="#eeeed1", fg="#8b8b00")
        l_weight.grid(row=4, column=0, columnspan=1)
        l_weight.configure(bg="#ffffe0", fg="#8b8b00")
        self.e_weight.grid(row=4, column=1, columnspan=1)
        self.e_weight.configure(bg="#eeeed1", fg="#8b8b00")
        l_height.grid(row=5, column=0, columnspan=1)
        l_height.configure(bg="#ffffe0", fg="#8b8b00")
        self.e_height.grid(row=5, column=1, columnspan=1)
        self.e_height.configure(bg="#eeeed1", fg="#8b8b00")
        b_cal.grid(row=6, column=1, s="NSEW")
        b_cal.configure(bg="#b4eeb4")
        b_quit.grid(row=7, column=1, s="NSEW")
        b_quit.configure(bg="IndianRed2")


class cal_tdee(TDEE):
    def cal_t(self):
        try:
            self.age_t = int(self.e_age.get())
            self.w_t = int(self.e_weight.get())
            self.h_t = int(self.e_height.get())
        except:
            print("Invalid, try again.....")
        self.activity_t = self.activities_box.get()
        self.sex_t = self.sex_box.get()
        self.age_t = int(self.e_age.get())
        self.w_t = int(self.e_weight.get())
        self.h_t = int(self.e_height.get())
        print(f"Activities: {self.activity_t}")
        print(f"Sex: {self.sex_t}")
        print(f"Age: {self.age_t}")
        print(f"Weight: {self.w_t}")
        print(f"Height: {self.h_t}")
        if self.sex_t == " Male":
            self.result_bmr = (
                66 + (13.7 * self.w_t) + (5 * self.h_t) - (6.8 * self.age_t)
            )
            if self.activity_t == " Never":
                self.result_tdee = self.result_bmr * 1.2
            elif self.activity_t == " 1-2 times per week":
                self.result_tdee = self.result_bmr * 1.375
            elif self.activity_t == " 3-5 times per week":
                self.result_tdee = self.result_bmr * 1.55
            elif self.activity_t == " 6-7 times per week":
                self.result_tdee = self.result_bmr * 1.725
            elif self.activity_t == " 2 times per day":
                self.result_tdee = self.result_bmr * 1.9
        elif self.sex_t == " Female":
            self.result_bmr = (
                655 + (9.6 * self.w_t) + (1.8 * self.h_t) - (4.7 * self.age_t)
            )
            if self.activity_t == " Never":
                self.result_tdee = self.result_bmr * 1.2
            elif self.activity_t == " 1-2 times per week":
                self.result_tdee = self.result_bmr * 1.375
            elif self.activity_t == " 3-5 times per week":
                self.result_tdee = self.result_bmr * 1.55
            elif self.activity_t == " 6-7 times per week":
                self.result_tdee = self.result_bmr * 1.725
            elif self.activity_t == " 2 times per day":
                self.result_tdee = self.result_bmr * 1.9
        print(f"BMI: {self.result_bmr:.2f}")
        print(f"TDEE: {self.result_tdee:.2f}")
        display_tdee.tdee_display(self)


class display_tdee(cal_tdee):
    def tdee_display(self):
        self.tdee_result_display = Tk()
        self.tdee_result_display.title("Result")
        self.tdee_result_display.configure(bg="#eeeed1")
        result = int(self.result_tdee)
        l1 = Label(self.tdee_result_display, text=result, font=("Bahnschrift", 12))
        l1.grid(row=0, column=2, columnspan=2)
        l1.configure(bg="#eeeed1", fg="#8b8b00")
        b1 = Button(
            self.tdee_result_display,
            text="Close",
            command=self.tdee_result_display.destroy,
        )
        b1.grid(row=1, column=2, columnspan=2, s="NSEW")
        b1.configure(bg="IndianRed2")


class BAC:
    def main_bac(self):
        weight_var = IntVar()
        beer_var = IntVar()
        wk_var = IntVar()
        wc_var = IntVar()
        wine_var = IntVar()
        time_var = IntVar()
        sex_var = StringVar()
        self.main_al = Tk()
        self.main_al.title("Blood alcohol concentration")
        self.main_al.geometry("400x400")
        self.main_al.configure(bg="#b4eeb4")
        print(">>>>BAC Calculator<<<<")
        l_headline = Label(
            self.main_al, text="BAC Calculator", font=("Bahnschrift", 12)
        )
        l_sex = Label(self.main_al, text="Sex", font=("Bahnschrift", 10))
        l_weight = Label(self.main_al, text="Weight(Kg)", font=("Bahnschrift", 10))
        l_beer = Label(self.main_al, text="Beer 330 cc(can)", font=("Bahnschrift", 10))
        l_wk = Label(self.main_al, text="Whiskey (shot)", font=("Bahnschrift", 10))
        l_wc = Label(
            self.main_al, text="Wine Cooler(bottle)", font=("Bahnschrift", 10)
        )  # 1 bottle = 5 glass
        l_wine = Label(
            self.main_al, text="Wine 150 cc(glass)", font=("Bahnschrift", 10)
        )
        l_time = Label(self.main_al, text="How long(hr)", font=("Bahnschrift", 10))
        self.s_weight = Scale(
            self.main_al, from_=0, to_=100, orient="horizontal", variable=weight_var
        )
        self.s_beer = Scale(
            self.main_al, from_=0, to_=30, orient="horizontal", variable=beer_var
        )
        self.s_wk = Scale(
            self.main_al, from_=0, to_=30, orient="horizontal", variable=wk_var
        )
        self.s_wc = Scale(
            self.main_al, from_=0, to_=30, orient="horizontal", variable=wc_var
        )
        self.s_wine = Scale(
            self.main_al, from_=0, to_=30, orient="horizontal", variable=wine_var
        )
        self.s_time = Scale(
            self.main_al, from_=0, to_=12, orient="horizontal", variable=time_var
        )
        self.sex_bac = ttk.Combobox(self.main_al, width=20, textvariable=sex_var)
        self.sex_bac["values"] = (" Male", " Female")
        b_cal = Button(
            self.main_al, text="Calculate", command=lambda: cal_bac.bac_cal(self)
        )
        b_quit = Button(self.main_al, text="Quit", command=self.main_al.destroy)
        l_headline.grid(row=0, column=2, columnspan=1)
        l_headline.configure(bg="#b4eeb4", fg="#006400")
        l_sex.grid(row=1, column=0, columnspan=1)
        l_sex.configure(bg="#b4eeb4", fg="#006400")
        l_weight.grid(row=2, column=0, columnspan=1)
        l_weight.configure(bg="#b4eeb4", fg="#006400")
        l_beer.grid(row=3, column=0, columnspan=1)
        l_beer.configure(bg="#b4eeb4", fg="#006400")
        l_wk.grid(row=4, column=0, columnspan=1)
        l_wk.configure(bg="#b4eeb4", fg="#006400")
        l_wc.grid(row=5, column=0, columnspan=1)
        l_wc.configure(bg="#b4eeb4", fg="#006400")
        l_wine.grid(row=6, column=0, columnspan=1)
        l_wine.configure(bg="#b4eeb4", fg="#006400")
        l_time.grid(row=7, column=0, columnspan=1)
        l_time.configure(bg="#b4eeb4", fg="#006400")
        self.sex_bac.grid(row=1, column=1, columnspan=2)
        self.s_weight.grid(row=2, column=1, columnspan=2)
        self.s_weight.configure(
            bg="#8fbc8f",
            fg="#006400",
            troughcolor="#8fbc8f",
            highlightbackground="#8fbc8f",
        )
        self.s_beer.grid(row=3, column=1, columnspan=2)
        self.s_beer.configure(
            bg="#8fbc8f",
            fg="#006400",
            troughcolor="#8fbc8f",
            highlightbackground="#8fbc8f",
        )
        self.s_wk.grid(row=4, column=1, columnspan=2)
        self.s_wk.configure(
            bg="#8fbc8f",
            fg="#006400",
            troughcolor="#8fbc8f",
            highlightbackground="#8fbc8f",
        )
        self.s_wc.grid(row=5, column=1, columnspan=2)
        self.s_wc.configure(
            bg="#8fbc8f",
            fg="#006400",
            troughcolor="#8fbc8f",
            highlightbackground="#8fbc8f",
        )
        self.s_wine.grid(row=6, column=1, columnspan=2)
        self.s_wine.configure(
            bg="#8fbc8f",
            fg="#006400",
            troughcolor="#8fbc8f",
            highlightbackground="#8fbc8f",
        )
        b_cal.grid(row=6, column=3, s="NSEW")
        b_cal.configure(bg="#fafad2")
        self.s_time.grid(row=7, column=1, columnspan=2)
        self.s_time.configure(
            bg="#8fbc8f",
            fg="#006400",
            troughcolor="#8fbc8f",
            highlightbackground="#8fbc8f",
        )
        b_quit.grid(row=7, column=3, s="NSEW")
        b_quit.configure(bg="IndianRed2")


class cal_bac(BAC):
    def bac_cal(self):
        try:
            count_w = int(self.s_weight.get())
            count_b = int(self.s_beer.get())
            count_wk = int(self.s_wk.get())
            count_wc = int(self.s_wc.get())
            count_wine = int(self.s_wine.get())
            count_time = int(self.s_time.get())
        except:
            print("Invalid value, try again....")
        count_w = int(self.s_weight.get())
        count_b = int(self.s_beer.get())
        count_wk = int(self.s_wk.get())
        count_wc = int(self.s_wc.get())
        count_wine = int(self.s_wine.get())
        count_time = int(self.s_time.get())
        sex = self.sex_bac.get()
        print(f"Sex:{sex}")
        print(f"Weight: {count_w} kg")
        print(f"Beer: {count_b}")
        print(f"Whiskey: {count_wk}")
        print(f"Wine Cooler: {count_wc}")
        print(f"Wine: {count_wine}")
        print(f"Time: {count_time} hr.")
        w = count_w  # weight
        try:
            if sex == " Male":
                s = 0.68
                # beer
                al = 16.5
                c = count_b
                self.result_bac = (al * c) / w * s * 10
                # whiskey
                al = 20.25
                c = count_wk
                self.result_bac += (al * c) / w * s * 10
                # wine cooler
                al = 16.5
                c = count_wc
                self.result_bac += (al * c) / w * s * 10
                # wine
                al = 19.5
                c = count_wine
                self.result_bac += (al * c) / w * s * 10
                # result
                self.result_bac -= count_time * 15
            elif sex == " Female":
                s = 0.55
                # beer
                al = 16.5
                c = count_b
                self.result_bac = (al * c) / w * s * 10
                # whiskey
                al = 20.25
                c = count_wk
                self.result_bac += (al * c) / w * s * 10
                # wine cooler
                al = 16.5
                c = count_wc
                self.result_bac += (al * c) / w * s * 10
                # wine
                al = 19.5
                c = count_wine
                self.result_bac += (al * c) / w * s * 10
                # result
                self.result_bac -= count_time * 15
        except:
            print("Error, try again....")
        self.result_bac = 0
        if sex == " Male":
            s = 0.68
            # beer
            al = 16.5
            c = count_b
            self.result_bac += (al * c) / w * s * 10
            # whiskey
            al = 20.25
            c = count_wk
            self.result_bac += (al * c) / w * s * 10
            # wine cooler
            al = 16.5
            c = count_wc
            self.result_bac += (al * c) / w * s * 10
            # wine
            al = 19.5
            c = count_wine
            self.result_bac += (al * c) / w * s * 10
            # result
            self.result_bac -= count_time * 15
            print(f"BAC = {self.result_bac:.2f} %mg")
        elif sex == " Female":
            s = 0.55
            # beer
            al = 16.5
            c = count_b
            self.result_bac = (al * c) / w * s * 10
            # whiskey
            al = 20.25
            c = count_wk
            self.result_bac += (al * c) / w * s * 10
            # wine cooler
            al = 16.5
            c = count_wc
            self.result_bac += (al * c) / w * s * 10
            # wine
            al = 19.5
            c = count_wine
            self.result_bac += (al * c) / w * s * 10
            # result
            self.result_bac -= count_time * 15
            if self.result_bac <= 0:
                self.result_bac = 0
            print(f"BAC = {self.result_bac:.2f} %mg")
        display_bac.bac_display(self)


class display_bac(cal_bac):
    def bac_display(self):
        self.bac_result_display = Tk()
        self.bac_result_display.title("Result")
        self.bac_result_display.geometry("200x100")
        self.bac_result_display.configure(bg="#b4eeb4")
        result = int(self.result_bac)
        if result <= 0:
            result = 0
        l1 = Label(self.bac_result_display, text=result, font=("Bahnschrift", 12))
        l1.grid(row=0, column=2, columnspan=2)
        l1.configure(bg="#b4eeb4", fg="#006400")
        b1 = Button(
            self.bac_result_display,
            text="Quit",
            command=self.bac_result_display.destroy,
        )
        b1.grid(row=4, column=2, columnspan=2, s="NSEW")
        b1.configure(bg="IndianRed2")


d = Healty()
