from tkinter import *
from PIL import ImageTk, Image

class AceMath:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        mainWindow.title('AcΣMαth')
        mainWindow.geometry("1920x1080")

        self.BGFullCanvas = Canvas(mainWindow, width = 1920, height = 1080)
        self.BGFullCanvas.pack()
        self.BGFull = ImageTk.PhotoImage(Image.open("KMITL_Py_Programming\Homework\HW9\BGFull.jpg"))
        self.BGFullCanvas.create_image(0, 0, anchor = "nw", image = self.BGFull)

        #--[Play Button]----------------------------------------------------------
        self.PlayButtonBG = PhotoImage(file = "KMITL_Py_Programming\Homework\HW9\Play.png")
        self.play_button = Button(mainWindow, image = self.PlayButtonBG, borderwidth = 0)
        self.play_button.place(x = 80, y = 425)

        #--[Sync Button]----------------------------------------------------------
        self.SyncButtonBG = PhotoImage(file = "KMITL_Py_Programming\Homework\HW9\Sync.png")
        self.sync_button = Button(mainWindow, image = self.SyncButtonBG, borderwidth = 0)
        self.sync_button.place(x = 80, y = 558)

        #--[Profile Button]-------------------------------------------------------
        self.ProfileButtonBG = PhotoImage(file = "KMITL_Py_Programming\Homework\HW9\Profile.png")
        self.profile_button = Button(mainWindow, image = self.ProfileButtonBG, borderwidth = 0)
        self.profile_button.place(x = 80, y = 690)

        #--[About Button]---------------------------------------------------------
        self.AboutButtonBG = PhotoImage(file = "KMITL_Py_Programming\Homework\HW9\About.png")
        self.about_button = Button(mainWindow, image = self.AboutButtonBG, borderwidth = 0)
        self.about_button.place(x = 80, y = 810)

        #--[Exit Button]----------------------------------------------------------
        self.ExitButtonBG = PhotoImage(file = "KMITL_Py_Programming\Homework\HW9\Exit.png")
        self.exit_button = Button(mainWindow, image = self.ExitButtonBG, borderwidth = 0)
        self.exit_button.place(x = 80, y = 923)

if __name__ == "__main__":
    mainWindow = Tk()
    app = AceMath(mainWindow)
    mainWindow.mainloop()