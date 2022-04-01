if __name__ != "assets.page.Story":
    raise RuntimeError("This file must be imported as a module. Please run it from Nekoparaiten.py")

import assets.function.read_write as rw

import winsound

"""Determine which tkinter version to use"""
try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2

dataPath = rw.read_data("dataPath")


class Story(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # --[Previous Button]-------------------------------------------------
        self.PrevButtonBG = tk.PhotoImage(file=f"{dataPath}/img/previous.png")
        self.prev_button = tk.Button(self, image=self.PrevButtonBG, bd=0, command=lambda: decrease_scene())
        self.prev_button.place(x=1285, y=788)

        # --[Forward Button]--------------------------------------------------
        self.ForwardButtonBG = tk.PhotoImage(file=f"{dataPath}/img/forward.png")
        self.forward_button = tk.Button(self, image=self.ForwardButtonBG, bd=0, command=lambda: increase_scene())
        self.forward_button.place(x=1359, y=788)

        # --[Skip Button]-----------------------------------------------------
        self.SkipButtonBG = tk.PhotoImage(file=f"{dataPath}/img/skip.png")
        self.skip_button = tk.Button(self, image=self.SkipButtonBG, bd=0, command=lambda: [controller.show_frame("Game"), 
                                     rw.write_data("sceneNum", 1), self.set_scene()])
        self.skip_button.place(x=1433, y=788)

        # --[Home Button]-----------------------------------------------------
        self.HomeButtonBG = tk.PhotoImage(file=f"{dataPath}/img/home.png")
        self.home_button = tk.Button(self, image=self.HomeButtonBG, bd=0, command=lambda: self.return_prompt())
        self.home_button.place(x=1507, y=788) 

        rw.write_data("character", "None")
        rw.write_data("sceneNum", 1)
        self.set_scene()

        def increase_scene():
            sceneNum = int(rw.read_data("sceneNum"))
            if sceneNum + 1 < 18:
                rw.write_data("sceneNum", sceneNum + 1)
                self.set_scene()
            elif sceneNum + 1 == 18:
                rw.write_data("sceneNum", 1)
                self.set_scene()
                self.controller.show_frame("Game")
        
        def decrease_scene():
            sceneNum = int(rw.read_data("sceneNum"))
            if sceneNum - 1 > 0:
                rw.write_data("sceneNum", sceneNum - 1)
                self.set_scene()

    def set_scene(self):
        num = int(rw.read_data("sceneNum"))
        name = rw.read_data("character")
        if (num > 0 and num < 10) or num == 16:
            self.SceneBG = tk.PhotoImage(file=f"{dataPath}/img/story/{num}.png")
        else:
            self.SceneBG = tk.PhotoImage(file=f"{dataPath}/img/story/{name}/{num}.png")

        self.scene = tk.Label(self, image=self.SceneBG, bd=0)
        self.scene.place(x=0, y=0)

        self.prev_button.lift()
        self.forward_button.lift()
        self.skip_button.lift()
        self.home_button.lift()

        if rw.read_data("character") != "None":
            if num == 5:
                self.knock = lambda: winsound.PlaySound(f"{dataPath}/audio/knock.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
                self.knock()
            elif num == 7:
                self.nya = lambda: winsound.PlaySound(f"{dataPath}/audio/{name}/nya.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
                self.nya()
            elif num == 9:
                self.bell = lambda: winsound.PlaySound(f"{dataPath}/audio/bell.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
                self.bell()
            elif num == 10:
                self.story2 = lambda: winsound.PlaySound(f"{dataPath}/audio/story2.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
                self.story2()
            elif num == 16:
                self.story3 = lambda: winsound.PlaySound(f"{dataPath}/audio/story3.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
                self.story3()
            
            
    def return_prompt(self):
        # --[Return Confirmation Dialog]--------------------------------------
        self.ReturnConfirmDiagBg = tk.PhotoImage(file=f"{dataPath}/img/return_confirm.png")
        self.return_confirm = tk.Label(self, image=self.ReturnConfirmDiagBg, bd=0)
        self.return_confirm.place(x=479, y=360)

        # --[Return Yes]------------------------------------------------------
        self.BGMusic = lambda: winsound.PlaySound(f"{dataPath}/audio/bgm.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        
        self.YesButtonBG = tk.PhotoImage(file=f"{dataPath}/img/yes.png")
        self.yes_button = tk.Button(self, image=self.YesButtonBG, bd=0, command=lambda: [
                                    close_diag(), rw.write_data("sceneNum", 1), self.set_scene(), 
                                    self.controller.show_frame("Mainmenu"), self.BGMusic()])
        self.yes_button.place(x=588, y=459)

        # --[Return No]-------------------------------------------------------
        self.NoButtonBG = tk.PhotoImage(
            file=f"{dataPath}/img/no.png")
        self.no_button = tk.Button(self, image=self.NoButtonBG, bd=0, command=lambda: close_diag())
        self.no_button.place(x=852, y=459)

        def close_diag():
            self.return_confirm.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()
