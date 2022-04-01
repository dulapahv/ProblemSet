if __name__ != "assets.page.Character":
    raise RuntimeError("This file must be imported as a module. Please run it from Nekoparaiten.py")

import assets.function.read_write as rw

import winsound

"""Determine which tkinter version to use"""
try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2

dataPath = rw.read_data("dataPath")


class Character(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.story1 = lambda: winsound.PlaySound(f"{dataPath}/audio/story1.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)

        # --[Header Text]-----------------------------------------------------
        self.HeaderTextBG = tk.PhotoImage(file=f"{dataPath}/img/character.png")
        self.header_text = tk.Label(self, image=self.HeaderTextBG, bd=0)
        self.header_text.place(x=0, y=0)

        # --[Back Button]-----------------------------------------------------
        self.BackButtonBG = tk.PhotoImage(file=f"{dataPath}/img/back.png")
        self.back_button = tk.Button(self, image=self.BackButtonBG, bd=0, command=lambda: controller.show_frame("Mainmenu"))
        self.back_button.place(x=27, y=15)

        # --[Fraise]----------------------------------------------------------
        self.FraiseBG = tk.PhotoImage(file=f"{dataPath}/img/fraise.png")
        self.fraise_button = tk.Button(self, image=self.FraiseBG, bd=0, command=lambda: [
                                       controller.show_frame("Story"), rw.write_data("character", "fraise"), self.story1()])
        self.fraise_button.place(x=0, y=91)

        # --[Chocola]---------------------------------------------------------
        self.ChocolaBG = tk.PhotoImage(file=f"{dataPath}/img/chocola.png")
        self.chocola_button = tk.Button(self, image=self.ChocolaBG, bd=0, command=lambda: [
                                        controller.show_frame("Story"), rw.write_data("character", "chocola"), self.story1()])
        self.chocola_button.place(x=229, y=91)

        # --[Vanilla]---------------------------------------------------------
        self.VanillaBG = tk.PhotoImage(file=f"{dataPath}/img/vanilla.png")
        self.vanilla_button = tk.Button(self, image=self.VanillaBG, bd=0, command=lambda: [
                                        controller.show_frame("Story"), rw.write_data("character", "vanilla"), self.story1()])
        self.vanilla_button.place(x=457, y=91)

        # --[Coconut]---------------------------------------------------------
        self.CoconutBG = tk.PhotoImage(file=f"{dataPath}/img/coconut.png")
        self.coconut_button = tk.Button(self, image=self.CoconutBG, bd=0, command=lambda: [
                                        controller.show_frame("Story"), rw.write_data("character", "coconut"), self.story1()])
        self.coconut_button.place(x=686, y=91)

        # --[Azuki]-----------------------------------------------------------
        self.AzukiBG = tk.PhotoImage(file=f"{dataPath}/img/azuki.png")
        self.azuki_button = tk.Button(self, image=self.AzukiBG, bd=0, command=lambda: [
                                      controller.show_frame("Story"), rw.write_data("character", "azuki"), self.story1()])
        self.azuki_button.place(x=915, y=91)

        # --[Maple]-----------------------------------------------------------
        self.MapleBG = tk.PhotoImage(file=f"{dataPath}/img/maple.png")
        self.maple_button = tk.Button(self, image=self.MapleBG, bd=0, command=lambda: [
                                      controller.show_frame("Story"), rw.write_data("character", "maple"), self.story1()])
        self.maple_button.place(x=1143, y=91)

        # --[Cinnamon]--------------------------------------------------------
        self.CinnamonBG = tk.PhotoImage(file=f"{dataPath}/img/cinnamon.png")
        self.cinnamon_button = tk.Button(self, image=self.CinnamonBG, bd=0, command=lambda: [
                                         controller.show_frame("Story"), rw.write_data("character", "cinnamon"), self.story1()])
        self.cinnamon_button.place(x=1372, y=91)

    
