if __name__ != "assets.page.Game":
    raise RuntimeError("This file must be imported as a module. Please run it from Nekoparaiten.py")

import assets.function.read_write as rw

from firebase_admin import db
from tkinter.tix import Tk
from PIL import ImageTk, Image
import random
import time
import winsound

"""Determine which tkinter version to use"""
try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2

dataPath = rw.read_data("dataPath")


class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.BGMusic = lambda: winsound.PlaySound(f"{dataPath}/audio/bgm.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        self.startFX = lambda: winsound.PlaySound(f"{dataPath}/audio/start.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
        self.finishMusic = lambda: winsound.PlaySound(f"{dataPath}/audio/finish.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)

        # --[Background Image]------------------------------------------------
        self.InstructionBG = tk.Canvas(self, width=1600, height=900)
        self.InstructionBG.pack()
        self.instruction = ImageTk.PhotoImage(Image.open(f"{dataPath}/img/instruction.png"))
        self.InstructionBG.create_image(0, 0, anchor="nw", image=self.instruction)

        # --[Back Button]-----------------------------------------------------
        self.GameBackButtonBG = tk.PhotoImage(file=f"{dataPath}/img/back.png")
        self.game_back_button = tk.Button(self, image=self.GameBackButtonBG, bd=0, command=lambda: controller.show_frame("Story"))
        self.game_back_button.place(x=27, y=15)

        # --[Start Button]----------------------------------------------------
        self.StartButtonBG = tk.PhotoImage(file=f"{dataPath}/img/start.png")
        self.start_button = tk.Button(self, image=self.StartButtonBG, bd=0, command=lambda: [self.startFX(), self.start_countdown()])
        self.start_button.place(x=720, y=800)

        self.stopwatch = Stopwatch()
        
        self.__timer = int(rw.read_data("countdownTimer"))
        self.__target = int(rw.read_data("targetScore"))
        self.__score = int(rw.read_data("startScore"))

    def start_countdown(self):
        self.InstructionBG.destroy()
        self.start_button.destroy()
        self.game_back_button.destroy()

        # --[Background Image]------------------------------------------------
        self.CountdownBG = tk.Canvas(self, width=1600, height=900)
        self.CountdownBG.pack()
        self.countdown = ImageTk.PhotoImage(Image.open(f"{dataPath}/img/countdown.png"))
        self.CountdownBG.create_image(0, 0, anchor="nw", image=self.countdown)

        #--[Countdown Text]---------------------------------------------------
        self.pre_countdown = tk.Label(self, bg="#f5f5f5", fg="#6d2727", font=("Arial Rounded MT Bold", 80))
        self.pre_countdown.place(x=770, y=380)

        while self.__timer != 0:
            self.pre_countdown.config(text=self.__timer)
            self.__timer -= 1
            time.sleep(1)
            Tk.update(self)
        time.sleep(1)
        self.start_game()
    
    def start_game(self):
        # --[Character Image]-------------------------------------------------
        self.CharButtonBG = tk.PhotoImage(file=f"{dataPath}/img/character/{rw.read_data('character')}.png")
        self.char_button = tk.Button(self, image=self.CharButtonBG, bd=0, command=lambda: click())
        self.char_button.place(x=0, y=0)

        # --[Game Back Button]------------------------------------------------
        self.GameBackButtonBG = tk.PhotoImage(file=f"{dataPath}/img/back.png")
        self.game_back_button = tk.Button(self, image=self.GameBackButtonBG, bd=0, command=lambda: [self.return_prompt(), self.stopwatch.stop(), self.char_button.config(state="disabled")])
        self.game_back_button.place(x=27, y=15)

        # --[Progress]--------------------------------------------------------
        self.progress_message = tk.Label(self, justify = "left", bg="#ca563a", fg="#f5f5f5", font=("Arial Rounded MT Bold", 40))
        self.progress_message.place(x=0, y=800)
        
        self.progress_message.config(text=f"{self.__score}/{self.__target}")

        self.clickFX = lambda: winsound.PlaySound(f"{dataPath}/audio/{rw.read_data('character')}/{random.randint(1, 16)}.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_NOSTOP)
  
        self.stopwatch.restart()

        def click():
            self.__score += 1
            self.progress_message.config(text=f"{self.__score}/{self.__target}")

            try:
                self.clickFX()
            except RuntimeError:
                pass

            if not self.__score + 1 <= self.__target:
                self.stopwatch.stop()
                rw.write_data("time", str(self.stopwatch))
                self.finishMusic()
                database = db.reference().get()
                if rw.read_data("username") != "nan":
                    # --[Finish1 BG]------------------------------------------
                    self.Finish2BG = tk.PhotoImage(file=f"{dataPath}/img/finish1.png")
                    self.finish2_bg = tk.Label(self, image=self.Finish2BG, bd=0)
                    self.finish2_bg.place(x=0, y=0)

                    # --[New Record]------------------------------------------
                    if self.stopwatch.duration < database[rw.read_data("username")]["time"]:
                        print("HI")
                        self.new_record_message = tk.Label(self, bg="#ffd200", fg="#6d2727", font=("Arial Rounded MT Bold", 40))
                        self.new_record_message.place(x=630, y=470)
                        self.new_record_message.config(text="New Record!")

                    db.reference().child(rw.read_data("username")).update({
                        "time": self.stopwatch.duration,
                        "playCount": database[rw.read_data("username")]["playCount"] + 1
                    })
                else:
                    # --[Finish2 BG]------------------------------------------
                    self.Finish2BG = tk.PhotoImage(file=f"{dataPath}/img/finish2.png")
                    self.finish2_bg = tk.Label(self, image=self.Finish2BG, bd=0)
                    self.finish2_bg.place(x=0, y=0)
                
                # --[Time Report]---------------------------------------------
                self.progress_message = tk.Label(self, bg="#ffd200", fg="#6d2727", font=("Arial Rounded MT Bold", 80))
                self.progress_message.place(x=490, y=340)
                self.progress_message.config(text=f"{self.stopwatch.duration:.6f}s")

                # --[Back Button]---------------------------------------------
                self.BackButtonBG = tk.PhotoImage(file=f"{dataPath}/img/back.png")
                self.back_button = tk.Button(self, image=self.BackButtonBG, bd=0, command=lambda: [self.controller.show_frame("Mainmenu"), 
                                             self.BGMusic(), self.reset()])
                self.back_button.place(x=706, y=783)
        
            print(f"Click #{self.__score} at {self.stopwatch.duration} ({str(self.stopwatch)})")  # Log
                  
    def return_prompt(self):
        # --[Return Confirmation Dialog]--------------------------------------
        self.returnBG = tk.PhotoImage(file=f"{dataPath}/img/return_confirm.png")
        self.return_bg = tk.Label(self, image=self.returnBG, bd=0)
        self.return_bg.place(x=479, y=360)

        # --[Return Yes]------------------------------------------------------        
        self.YesButtonBG = tk.PhotoImage(file=f"{dataPath}/img/yes.png")
        self.yes_button = tk.Button(self, image=self.YesButtonBG, bd=0, command=lambda: [
                                    close_diag(), rw.write_data("sceneNum", 1), self.BGMusic(),
                                    self.stopwatch.reset(), self.reset(), self.controller.show_frame("Mainmenu")])
        self.yes_button.place(x=588, y=459)

        # --[Return No]-------------------------------------------------------
        self.NoButtonBG = tk.PhotoImage(
            file=f"{dataPath}/img/no.png")
        self.no_button = tk.Button(self, image=self.NoButtonBG, bd=0, command=lambda: [close_diag(), self.stopwatch.start(), self.char_button.config(state="normal")])
        self.no_button.place(x=852, y=459)

        def close_diag():
            self.return_bg.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()
        
    def reset(self):
        self.__timer = int(rw.read_data("countdownTimer"))
        self.__target = int(rw.read_data("targetScore"))
        self.__score = int(rw.read_data("startScore"))

        # --[Background Image]------------------------------------------------
        self.InstructionBG = tk.Canvas(self, width=1600, height=900)
        self.InstructionBG.pack()
        self.instruction = ImageTk.PhotoImage(Image.open(f"{dataPath}/img/instruction.png"))
        self.InstructionBG.create_image(0, 0, anchor="nw", image=self.instruction)

        # --[Back Button]-----------------------------------------------------
        self.GameBackButtonBG = tk.PhotoImage(file=f"{dataPath}/img/back.png")
        self.game_back_button = tk.Button(self, image=self.GameBackButtonBG, bd=0, command=lambda: self.controller.show_frame("Story"))
        self.game_back_button.place(x=27, y=15)

        # --[Start Button]----------------------------------------------------
        self.StartButtonBG = tk.PhotoImage(file=f"{dataPath}/img/start.png")
        self.start_button = tk.Button(self, image=self.StartButtonBG, bd=0, command=lambda: [self.startFX(), self.start_countdown()])
        self.start_button.place(x=720, y=800)

        self.char_button.destroy()
        self.progress_message.destroy()
        self.CountdownBG.destroy()
        self.pre_countdown.destroy()
                


class Stopwatch:
    def __init__(self):
        self._start = time.perf_counter()
        self._end = None

    @property
    def duration(self):
        return self._end - self._start if self._end else time.perf_counter() - self._start

    @property
    def running(self):
        return not self._end

    def restart(self):
        self._start = time.perf_counter()
        self._end = None
        return self

    def reset(self):
        self._start = time.perf_counter()
        self._end = self._start
        return self

    def start(self):
        if not self.running:
            self._start = time.perf_counter() - self.duration
            self._end = None
        return self

    def stop(self):
        if self.running:
            self._end = time.perf_counter()
        return self

    def __str__(self):
        time = self.duration * 1000
        if time >= 1000:
            return "{:.2f}s".format(time / 1000)
        if time >= 1:
            return "{:.2f}ms".format(time)
        return "{:.2f}μs".format(time * 1000)