if __name__ != "assets.page.Leaderboard":
    raise RuntimeError("This file must be imported as a module. Please run it from Nekoparaiten.py")

import assets.function.get_leaderboard as leaderboard
import assets.function.read_write as rw

from PIL import ImageTk, Image

"""Determine which tkinter version to use"""
try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2

dataPath = rw.read_data("dataPath")


class Leaderboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # --[Background Image]------------------------------------------------
        self.BG = tk.Canvas(self, width=1600, height=900)
        self.BG.pack()
        self.BGimg = ImageTk.PhotoImage(Image.open(f"{dataPath}/img/leaderboard_bg.png"))
        self.BG.create_image(0, 0, anchor="nw", image=self.BGimg)

        # --[Header Text]-----------------------------------------------------
        self.HeaderTextBG = tk.PhotoImage(file=f"{dataPath}/img/leaderboard_header.png")
        self.header_text = tk.Label(self, image=self.HeaderTextBG, bd=0)
        self.header_text.place(x=0, y=0)

        # --[Back Button]-----------------------------------------------------
        self.BackButtonBG = tk.PhotoImage(file=f"{dataPath}/img/back.png")
        self.back_button = tk.Button(self, image=self.BackButtonBG, bd=0, command=lambda: controller.show_frame("Mainmenu"))
        self.back_button.place(x=27, y=15)

        # --[Refresh Button]--------------------------------------------------
        self.RefreshButtonBG = tk.PhotoImage(file=f"{dataPath}/img/refresh.png")
        self.refresh_button = tk.Button(self, image=self.RefreshButtonBG, bd=0, command=lambda: self.get_leaderboard())
        self.refresh_button.place(x=1507, y=19)

        # --[Leaderboard Text]------------------------------------------------
        self.leaderboardName = tk.Label(self, justify="left", bg="#ffd200", fg="#6d2727", font=("Arial Rounded MT Bold", 30))
        self.leaderboardName.place(x=200, y=100)

        self.leaderboardTime = tk.Label(self, justify="right", bg="#ffd200", fg="#6d2727", font=("Arial Rounded MT Bold", 30))
        self.leaderboardTime.place(x=1170, y=100)

        self.get_leaderboard()

    def get_leaderboard(self):
        stat = leaderboard.getLeaderboard()
        username = [name[0] for name in stat]
        time = [str(f"{time[1]:.6f}") for time in stat]
        for i in range(len(username)):
            username[i] = f"{i + 1}. {username[i]}"
        for i in range(len(time)):
            time[i] = f"{time[i]}s"
        for i in range(int(rw.read_data("scoreboardLimit")), len(username)):
            username.pop(i)
            time.pop(i)
        username.insert(0, "USERNAME")
        time.insert(0, "TIME")
        self.leaderboardName.config(text="\n".join(username))
        self.leaderboardTime.config(text="\n".join(time))
