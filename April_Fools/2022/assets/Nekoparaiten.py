"""Check for library dependencies"""
import assets.library

"""Import pages from assets"""
import assets.page.Mainmenu as Mainmenu
import assets.page.Character as Character
import assets.page.Story as Story
import assets.page.Game as Game
import assets.page.Sync as Sync
import assets.page.Leaderboard as Leaderboard 

import assets.function.read_write as rw

from firebase_admin import initialize_app, credentials
import random

"""Determine which tkinter version to use"""
try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2

dataPath = rw.read_data("dataPath")

"""Authenticate Firebase database"""
cred = credentials.Certificate(f"{dataPath}/token.json")
initialize_app(cred, {"databaseURL": "https://nekoparaiten-n0miya-default-rtdb.asia-southeast1.firebasedatabase.app/"})


class Nekoparaiten(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        """
        This container is where all the frames (or pages) will be stacked
        on top of each other, then each one that we want visible will be
        raised above the others.
        """
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        pages = (Mainmenu.Mainmenu,
                Character.Character,
                Story.Story,
                Game.Game,
                Leaderboard.Leaderboard,
                Sync.Sync)
        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        """Show the first page based on the first element in the pages list."""
        self.show_frame("Mainmenu")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    Nekoparaiten = Nekoparaiten()

    """App Configuration"""
    Nekoparaiten.iconbitmap(f"{dataPath}/img/nkprt.ico")
    Nekoparaiten.title("Nekoparaiten")
    Nekoparaiten.geometry("1600x900")
    Nekoparaiten.resizable(width=False, height=False)
    Nekoparaiten.config(cursor=f"@{dataPath}/cursor/{random.randint(1, 7)}.cur")

    Nekoparaiten.mainloop()
