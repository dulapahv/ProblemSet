from tkinter import Entry, Button, Tk, messagebox, IntVar

class Currency_Converter:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        mainWindow.title("Currency Converter")
        self.money = IntVar()
    
        self.input = Entry(mainWindow, textvariable = self.money, width = 48, justify = "right")
        self.input.grid(row = 1, column = 1)

        self.usd_to_thb = Button(mainWindow, text = "USD -> THB", width = 40, command = self.toTHB)
        self.usd_to_thb.grid(row = 2, column = 1)

        self.thb_to_usd = Button(mainWindow, text = "THB -> USD", width = 40, command = self.toUSD)
        self.thb_to_usd.grid(row = 3, column = 1)

    def toTHB(self):
        USD = int(self.input.get())
        THB = int(self.input.get()) * 30
        messagebox.showinfo("USD -> THB", "%.2f USD = %.2f THB" % (USD, THB))
    
    def toUSD(self):
        THB = int(self.input.get())
        USD = int(self.input.get()) / 30
        messagebox.showinfo("THB -> USD", "%.2f THB = %.2f USD" % (THB, USD))


mainWindow = Tk()
app = Currency_Converter(mainWindow)
mainWindow.mainloop()
