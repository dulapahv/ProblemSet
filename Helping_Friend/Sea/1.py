from tkinter import *
import datetime

window = Tk()
window.title("Age Calculator")
window.geometry("620x780")
image1 = PhotoImage(file=r'Helping_Friend\Sea\agecalc.gif')
Label(window, image= image1).grid()
name = Label(text="Name:")
year = Label(text="Birth's Year(A.D.):")
month = Label(text="Month:")
date = Label(text="Day:")
nameEntry = Entry()
yearEntry = Entry()
monthEntry = Entry()
dateEntry = Entry()
name.grid(column=0, row=1,sticky ="w",padx=256)
year.grid(column=0, row=2,sticky ="w",padx=200)
month.grid(column=0, row=3,sticky ="w",padx=253)
date.grid(column=0, row=4,sticky ="w",padx=269)
nameEntry.grid(column=0, row=1)
yearEntry.grid(column=0, row=2)
monthEntry.grid(column=0, row=3)
dateEntry.grid(column=0, row=4)
def getInput():
    name = nameEntry.get()
    Yourname = Person(name, datetime.date(int(yearEntry.get()),int(monthEntry.get()), int(dateEntry.get())))
    textArea = Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = " !Hello *{Yourname}*!.\n !*You are {age} years old*!".format(Yourname = name, age = Yourname.age())
    textArea.insert(END, answer)

button = Button(window, text="Calculate Age", command=getInput, bg="yellow")
button.grid(column=0, row=5)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age
window.mainloop()