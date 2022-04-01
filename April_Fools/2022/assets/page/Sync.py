if __name__ != "assets.page.Sync":
    raise RuntimeError("This file must be imported as a module. Please run it from Nekoparaiten.py")

import assets.function.read_write as rw

from firebase_admin import db
from PIL import ImageTk, Image

"""Determine which tkinter version to use"""
try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2

dataPath = rw.read_data("dataPath")


class Sync(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.database = db.reference().get()

        # --[Background Image]------------------------------------------------
        self.BG = tk.Canvas(self, width=1600, height=900)
        self.BG.pack()
        self.BGimg = ImageTk.PhotoImage(Image.open(f"{dataPath}/img/dataload.png"))
        self.BG.create_image(0, 0, anchor="nw", image=self.BGimg)

        # --[Back Button]-----------------------------------------------------
        self.BackButtonBG = tk.PhotoImage(file=f"{dataPath}/img/back.png")
        self.back_button = tk.Button(self, image=self.BackButtonBG, bd=0, command=lambda: controller.show_frame("Mainmenu"))
        self.back_button.place(x=1288, y=15)

        # --[Logout]----------------------------------------------------------
        self.LogoutBG = tk.PhotoImage(file=f"{dataPath}/img/logout.png")
        self.logout_button = tk.Button(self, image=self.LogoutBG, bd=0, command=lambda: self.logout())

        # --[Login Status]----------------------------------------------------
        self.login_status = tk.Label(self, justify = "left", bg="#ca563a", fg="#f5f5f5", font=("Arial Rounded MT Bold", 16))
        self.login_status.place(x=1288, y=760)
        if rw.read_data("username") == "nan":
            self.login_status.config(text=f"Currently not logged in")
        else:
            self.login_status.config(text=f"Logged in as:\n{rw.read_data('username')}\nTimes played: {self.database[rw.read_data('username')]['playCount']}")
            self.logout_button.place(x=1440, y=840)

        # --[Register]--------------------------------------------------------
        self.reg_username = tk.Entry(self, width = 18, bg="#f5f5f5", fg="#6d2727", font=("Arial Rounded MT Bold", 20))
        self.reg_username.place(x=1288, y=190)
        self.reg_username.insert(0, "Username")
        self.reg_username.bind("<1>", lambda _: self.reg_username.delete(0, 'end'))

        self.reg_password = tk.Entry(self, width = 18, show = "*", bg="#f5f5f5", fg="#6d2727", font=("Arial Rounded MT Bold", 20))
        self.reg_password.place(x=1288, y=240)
        self.reg_password.insert(0, "Password")
        self.reg_password.bind("<1>", lambda _: self.reg_password.delete(0, 'end'))

        self.reg_password_confirm = tk.Entry(self, width = 18, show = "*", bg="#f5f5f5", fg="#6d2727", font=("Arial Rounded MT Bold", 20))
        self.reg_password_confirm.place(x=1288, y=290)
        self.reg_password_confirm.insert(0, "Password")
        self.reg_password_confirm.bind("<1>", lambda _: self.reg_password_confirm.delete(0, 'end'))

        self.reg_message = tk.Label(self, justify = "left", bg="#ca563a", fg="#f5f5f5", font=("Arial Rounded MT Bold", 12))
        self.reg_message.place(x=1288, y=340)

        self.RegButtonBG = tk.PhotoImage(file=f"{dataPath}/img/signup.png")
        self.reg_button = tk.Button(self, image=self.RegButtonBG, bd=0, command=lambda: self.sign_up())
        self.reg_button.place(x=1440, y=390)

        # --[Login]-----------------------------------------------------------
        self.login_username = tk.Entry(self, width = 18, bg="#f5f5f5", fg="#6d2727", font=("Arial Rounded MT Bold", 20))
        self.login_username.place(x=1288, y=550)
        self.login_username.insert(0, "Username")
        self.login_username.bind("<1>", lambda _: self.login_username.delete(0, 'end'))

        self.login_password = tk.Entry(self, width = 18, show = "*", bg="#f5f5f5", fg="#6d2727", font=("Arial Rounded MT Bold", 20))
        self.login_password.place(x=1288, y=600)
        self.login_password.insert(0, "Password")
        self.login_password.bind("<1>", lambda _: self.login_password.delete(0, 'end'))

        self.login_message = tk.Label(self, justify = "left", bg="#ca563a", fg="#f5f5f5", font=("Arial Rounded MT Bold", 12))
        self.login_message.place(x=1288, y=650)

        self.LoginButtonBG = tk.PhotoImage(file=f"{dataPath}/img/login.png")
        self.login_button = tk.Button(self, image=self.LoginButtonBG, bd=0, command=lambda: self.login())
        self.login_button.place(x=1440, y=700)
    
    def sign_up(self):
        usernameDB = db.reference().get()
        if len(self.reg_username.get()) < 4 or len(self.reg_username.get()) > 20:
            self.reg_message.config(text="Username must be between 4 and\n20 characters!")
        elif self.reg_password.get() != self.reg_password_confirm.get():
            self.reg_message.config(text="Passwords do not match!")
        elif self.reg_username.get() in usernameDB:
            self.reg_message.config(text="Username already exists!")
        else:
            self.reg_message.config(text="")
            db.reference().child(self.reg_username.get()).set({
            "key": str(self.reg_password.get()),
            "time": 999999999,
            "playCount": 0})
            self.reg_username.delete(0, 'end')
            self.reg_password.delete(0, 'end')
            self.reg_password_confirm.delete(0, 'end')
            self.reg_message.config(text="Successfully registered! Please login\nwith your new credentials.")
    
    def login(self):
        if self.login_username.get() in self.database:
            if str(self.login_password.get()) == self.database[self.login_username.get()]["key"]:
                self.login_message.config(text="You have successfully logged in!")
                self.login_status.config(text=f"Logged in as:\n{self.login_username.get()}\nTimes played: {self.database[self.login_username.get()]['playCount']}")
                self.logout_button.place(x=1440, y=840)
                rw.write_data("username", self.login_username.get())
                self.login_username.delete(0, 'end')
                self.login_password.delete(0, 'end')
            else:
                self.login_message.config(text="Incorrect username or password!")
        else:
            self.login_message.config(text="Incorrect username or password!")
    
    def logout(self):
        self.login_status.config(text="Currently not logged in")
        self.login_message.config(text="")
        self.logout_button.place_forget()
        rw.write_data("username", "nan")