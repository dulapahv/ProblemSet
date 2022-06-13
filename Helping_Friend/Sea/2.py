import tkinter as tk

app = tk.Tk()

value = list(range(1950, 2050))

storeVar = tk.IntVar(value=2003)

year = tk.OptionMenu(app, storeVar, *value)
year.config(width=20)
year.grid()

app.mainloop()
