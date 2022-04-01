if __name__ != "assets.page.Mainmenu":
    raise RuntimeError("This file must be imported as a module. Please run it from Nekoparaiten.py")

import assets.function.read_write as rw

from PIL import ImageTk, Image
import sys
import winsound

"""Determine which tkinter version to use"""
try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2

dataPath = rw.read_data("dataPath")


class Mainmenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.BGMusic = lambda: winsound.PlaySound(f"{dataPath}/audio/bgm.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        self.BGMusic()

        # --[Background Image]------------------------------------------------
        self.BG = tk.Canvas(self, width=1600, height=900)
        self.BG.pack()
        self.BGimg = ImageTk.PhotoImage(Image.open(f"{dataPath}/img/bg.png"))
        self.BG.create_image(0, 0, anchor="nw", image=self.BGimg)

        # --[Play Button]-----------------------------------------------------
        self.PlayButtonBG = tk.PhotoImage(file=f"{dataPath}/img/game_start.png")
        self.play_button = tk.Button(self, image=self.PlayButtonBG, bd=0, command=lambda: [controller.show_frame("Character"), self.close_diag()])
        self.play_button.place(x=1315, y=176)

        # --[Cloud Sync Button]-----------------------------------------------
        self.CloudSyncButtonBG = tk.PhotoImage(file=f"{dataPath}/img/cloudsync.png")
        self.cloud_sync_button = tk.Button(self, image=self.CloudSyncButtonBG, bd=0, command=lambda: [controller.show_frame("Sync"), self.close_diag()])
        self.cloud_sync_button.place(x=1315, y=290)

        # --[Leaderboard Button]----------------------------------------------
        self.LeaderboardButtonBG = tk.PhotoImage(file=f"{dataPath}/img/leaderboard.png")
        self.Leaderboard_Button = tk.Button(self, image=self.LeaderboardButtonBG, bd=0, command=lambda: [controller.show_frame("Leaderboard"), self.close_diag()])
        self.Leaderboard_Button.place(x=1315, y=404)

        # --[About Button]----------------------------------------------------
        self.AboutButtonBG = tk.PhotoImage(file=f"{dataPath}/img/about.png")
        self.about_button = tk.Button(self, image=self.AboutButtonBG, bd=0, command=lambda: [self.about(), self.close_diag()])
        self.about_button.place(x=1315, y=518)

        # --[Exit Button]--------------------------------- -------------------
        self.ExitButtonBG = tk.PhotoImage(file=f"{dataPath}/img/exit.png")
        self.exit_button = tk.Button(self, image=self.ExitButtonBG, bd=0, command=lambda: self.exit_prompt())
        self.exit_button.place(x=1315, y=632)
    
    def about(self):
        # --[About Dialog]----------------------------------------------------
        self.AboutDiagBG = tk.PhotoImage(file=f"{dataPath}/img/about_diag.png")
        self.about_diag = tk.Label(self, image=self.AboutDiagBG, bd=0)
        self.about_diag.place(x=381, y=249)

        # --[Close Button]----------------------------------------------------
        self.CloseButtonBG = tk.PhotoImage(file=f"{dataPath}/img/close.png")
        self.close_button = tk.Button(self, image=self.CloseButtonBG, bd=0, command=lambda: [
                                      self.about_diag.place_forget(), self.close_button.destroy()])
        self.close_button.place(x=716, y=646)

    def exit_prompt(self):
        # --[Exit Confirmation Dialog]-----------------------------------------
        self.ExitConfirmDiagBg = tk.PhotoImage(file=f"{dataPath}/img/exit_confirm.png")
        self.exit_confirm = tk.Label(self, image=self.ExitConfirmDiagBg, bd=0)
        self.exit_confirm.place(x=479, y=360)

        # --[Exit Yes]--------------------------------------------------------
        self.YesButtonBG = tk.PhotoImage(file=f"{dataPath}/img/yes.png")
        self.yes_button = tk.Button(self, image=self.YesButtonBG, bd=0, command=lambda: sys.exit())
        self.yes_button.place(x=588, y=459)

        # --[Exit No]---------------------------------------------------------
        self.NoButtonBG = tk.PhotoImage(
            file=f"{dataPath}/img/no.png")
        self.no_button = tk.Button(self, image=self.NoButtonBG, bd=0, command=lambda: self.close_diag())
        self.no_button.place(x=852, y=459)

    def close_diag(self):
        try:
            self.exit_confirm.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()
        except AttributeError:  # this exception is intentionally and can be safely ignored
            pass

