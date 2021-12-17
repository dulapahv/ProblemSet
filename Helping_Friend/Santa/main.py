from tkinter import *
import tkinter.messagebox
import abc


class MainProgram(metaclass=abc.ABCMeta):
    def __init__(self):
        self.subject_list = []
        self.daycount_list = []
        self.period_list = []
        self.colorcount_list = []
        self.task_list = []
        self.duedate_list = []
        self.progress_list = []
        # self.imagee1 = Label(window, image=self.image1)
        # self.imagee1.grid(row=5,columnspan= 2,column=1)
    @abc.abstractmethod

    def add(self):
        pass
    def save(self):
        pass
    def edit(self):
        pass
    def delete(self):
        pass
    def change(self):
        pass
    def changed(self):
        pass
    def view(self):
        pass


class Schedule(MainProgram):
    def __init__(self):
        MainProgram.__init__(self)

    def add(self):
        self.addwindow = Tk()
        self.addwindow.title('Add Class')
        self.addwindow.config(bg='gold')

        self.sub = Label(self.addwindow, text="Subject", width=10)
        self.sub.grid(row=1, column=1)
        self.sub.config(fg='white', bg='purple')
        self.subentry = Entry(self.addwindow)
        self.subentry.grid(row=1, column=2, ipadx=5)

        self.day = Label(self.addwindow, text='Day', width=10)
        self.day.grid(row=2, column=1)
        self.day.config(fg='white', bg='purple')
        self.daylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.daysp = Spinbox(self.addwindow, values=self.daylist)
        self.daysp.grid(row=2, column=2, padx=2)

        self.periodlb = Label(self.addwindow, text='Period', width=10)
        self.periodlb.grid(row=3, column=1)
        self.periodlb.config(fg='white', bg='purple')
        self.periodsp = Spinbox(self.addwindow, from_=1, to=6)
        self.periodsp.grid(row=3, column=2, padx=2)

        self.colorlb = Label(self.addwindow, text='Color', width=10)
        self.colorlb.grid(row=4, column=1)
        self.colorlb.config(fg='white', bg='purple')
        self.color_list = ['white', 'yellow', 'orange', 'skyblue', 'green', 'green yellow', 'Salmon', 'hotpink',
                           'khaki']
        self.colorsp = Spinbox(self.addwindow, values=self.color_list)
        self.colorsp.grid(row=4, column=2, padx=2)

        self.savebutton = Button(self.addwindow, text="Save", command=self.save)
        self.savebutton.grid(row=5, column=2)
        self.savebutton.config(fg='white', bg='purple')
        self.subject = self.subentry.get()


    def save(self):
        self.subject_list.append(self.subject)
        self.daycount = self.daylist.index(self.daysp.get()) + 1
        self.daycount_list.append(self.daycount)
        self.period = (int(self.periodsp.get()))
        self.period_list.append(self.period)
        self.colorcount = self.color_list.index(self.colorsp.get())
        self.colorcount_list.append(self.colorcount)
        # check
        print(self.subject_list, self.daycount_list, self.period_list, self.colorcount_list)
        self.addwindow.destroy()

    def edit(self):
        if self.subject_list == []:
            tkinter.messagebox.showinfo("Alert", "There was no class on the schedule right now")
        else:
            self.editschwindow = Tk()
            self.editschwindow.title('Remove Class')
            self.editschwindow.config(bg='gold')
            self.editschlb = Label(self.editschwindow, text='Subject', width=10)
            self.editschlb.grid(row=1, column=1)
            self.editschlb.config(fg='white', bg='purple')
            self.editschsp = Spinbox(self.editschwindow, values=self.subject_list,width=20)
            self.editschsp.grid(row=1, column=2, padx=2)

            self.removeschbutton = Button(self.editschwindow, text="Remove", command=self.delete,width=20)
            self.removeschbutton.grid(row=3, column=2)
            self.removeschbutton.config(fg='white', bg='purple')

            self.editschbutton = Button(self.editschwindow, text="Update Progress", command=self.change,width=20)
            self.editschbutton.grid(row=2, column=2)
            self.editschbutton.config(fg='white', bg='purple')

    def delete(self):
        self.removesub = self.subject_list.index(self.editschsp.get())
        self.subject_list.pop(self.removesub)
        self.editschwindow.destroy()

    def change(self):
        print(self.subject_list.index(self.editschsp.get()))
        self.changeschindex = self.subject_list.index(self.editschsp.get())
        self.changeschprogresswindow = Tk()
        self.changeschprogresswindow.title('Update Task Progress')
        self.changeschprogresswindow.config(bg='gold')

        self.editday = Label(self.changeschprogresswindow, text='Day', width=10)
        self.editday.grid(row=2, column=1)
        self.editday.config(fg='white', bg='purple')
        self.editdaysp = Spinbox(self.changeschprogresswindow, values=self.daylist)
        self.editdaysp.grid(row=2, column=2, padx=2)

        self.editperiodlb = Label(self.changeschprogresswindow, text='Period', width=10)
        self.editperiodlb.grid(row=3, column=1)
        self.editperiodlb.config(fg='white', bg='purple')
        self.editperiodsp = Spinbox(self.changeschprogresswindow, from_=1, to=6)
        self.editperiodsp.grid(row=3, column=2, padx=2)

        self.editcolorlb = Label(self.changeschprogresswindow, text='Color', width=10)
        self.editcolorlb.grid(row=4, column=1)
        self.editcolorlb.config(fg='white', bg='purple')
        self.editcolorsp = Spinbox(self.changeschprogresswindow, values=self.color_list)
        self.editcolorsp.grid(row=4, column=2, padx=2)

        self.changeschbutton = Button(self.changeschprogresswindow, text="Update Class", command=self.changed,width=20)
        self.changeschbutton.grid(row=5, column=2, padx=2)
        self.editschwindow.destroy()

    def changed(self):
        self.daycount_list[self.changeschindex] = self.daylist.index(self.editdaysp.get())+1
        self.period_list[self.changeschindex] = self.editperiodsp.get()
        self.colorcount_list[self.changeschindex] = self.color_list.index(self.editcolorsp.get())
        self.changeschprogresswindow.destroy()

    def view(self):
        self.sw = Tk()
        self.sw.title("Schedule")
        self.sw.config(bg='gold')

        self.initial = Label(self.sw, text=" ", width=10)
        self.initial.grid(row=0, column=0)
        self.initial.config(bg='purple')
        self.firstp = Label(self.sw, text="8:45-10:15", width=10)
        self.firstp.grid(row=0, column=1)
        self.firstp.config(fg='white', bg='purple')
        self.secondp = Label(self.sw, text="10:30-12:00", width=10)
        self.secondp.grid(row=0, column=2)
        self.secondp.config(fg='white', bg='purple')
        self.thirdp = Label(self.sw, text="13:00-14:30", width=10)
        self.thirdp.grid(row=0, column=3)
        self.thirdp.config(fg='white', bg='purple')
        self.fourthp = Label(self.sw, text="14:45-16:15", width=10)
        self.fourthp.grid(row=0, column=4)
        self.fourthp.config(fg='white', bg='purple')
        self.fifthp = Label(self.sw, text="16:30-18:00", width=10)
        self.fifthp.grid(row=0, column=5)
        self.fifthp.config(fg='white', bg='purple')
        self.sixthp = Label(self.sw, text="18:15-19:45", width=10)
        self.sixthp.grid(row=0, column=6)
        self.sixthp.config(fg='white', bg='purple')

        self.mon = Label(self.sw, text="Monday", width=10)
        self.mon.grid(row=1, column=0)
        self.mon.config(bg='yellow')
        self.tue = Label(self.sw, text="Tuesday", width=10)
        self.tue.grid(row=2, column=0)
        self.tue.config(bg='pink')
        self.wed = Label(self.sw, text="Wednesday", width=10)
        self.wed.grid(row=3, column=0)
        self.wed.config(bg='green')
        self.thu = Label(self.sw, text="Thursday", width=10)
        self.thu.grid(row=4, column=0)
        self.thu.config(bg='orange')
        self.fri = Label(self.sw, text="Friday", width=10)
        self.fri.grid(row=5, column=0)
        self.fri.config(bg='lightblue')
        self.sat = Label(self.sw, text="Saturn", width=10)
        self.sat.grid(row=6, column=0)
        self.sat.config(bg='purple')
        self.sun = Label(self.sw, text="Sunday", width=10)
        self.sun.grid(row=7, column=0)
        self.sun.config(bg='red')
        self.quitsch = Button(self.sw, text="Exit", width=73, command=self.sw.destroy)
        self.quitsch.grid(row=8, column=0, columnspan=8)
        self.quitsch.config(fg='white', bg='purple')
        for x in range(len(self.subject_list)):
            self.subb = Label(self.sw, text=self.subject_list[x], width=10)
            self.subb.grid(row=self.daycount_list[x], column=self.period_list[x])
            self.subb.config(bg=self.color_list[(self.colorcount_list[x])])

class Task(MainProgram):
    def __init__(self):
        MainProgram.__init__(self)

    def add(self):
        self.addtwindow = Tk()
        self.addtwindow.title('Add Task')
        self.addtwindow.config(bg='gold')
        self.task = Label(self.addtwindow, text="Task", width=10)
        self.task.grid(row=1, column=1)
        self.task.config(fg='white', bg='purple')
        self.taskentry = Entry(self.addtwindow)
        self.taskentry.grid(row=1, column=2, ipadx=5)
        self.date = Label(self.addtwindow, text="Due Date", width=10)
        self.date.grid(row=2, column=1)
        self.date.config(fg='white', bg='purple')
        self.dateentry = Entry(self.addtwindow)
        self.dateentry.grid(row=2, column=2, ipadx=5)
        self.due = Label(self.addtwindow, text='Status', width=10)
        self.due.grid(row=3, column=1)
        self.due.config(fg='white', bg='purple')
        self.progress = ["TO DO", "In Progress", "Done"]
        self.progresssp = Spinbox(self.addtwindow, values=self.progress)
        self.progresssp.grid(row=3, column=2, padx=2)
        self.savetbutton = Button(self.addtwindow, text="Save", command=self.save)
        self.savetbutton.grid(row=4, column=2)
        self.savetbutton.config(fg='white', bg='purple')

    def save(self):
        print(self.taskentry.get())
        print(self.dateentry.get())
        print(self.progress.index(self.progresssp.get()))

        self.task_list.append(self.taskentry.get())
        self.duedate_list.append(self.dateentry.get())
        self.progress_list.append(self.progress.index(self.progresssp.get()))
        self.addtwindow.destroy()
        print(self.progress_list)

    def edit(self):
        if self.task_list == []:
            tkinter.messagebox.showinfo("Alert", "There was no Task on the list right now")
        else:
            self.edittaskwindow = Tk()
            self.edittaskwindow.title('Remove Task')
            self.edittaskwindow.config(bg='gold')
            self.edittasklb = Label(self.edittaskwindow, text='Task', width=10)
            self.edittasklb.grid(row=1, column=1)
            self.edittasklb.config(fg='white', bg='purple')
            self.edittasksp = Spinbox(self.edittaskwindow, values=self.task_list)
            self.edittasksp.grid(row=1, column=2, padx=2)

            self.removetaskbutton = Button(self.edittaskwindow, text="Remove", command=self.delete, width=20)
            self.removetaskbutton.grid(row=3, column=2)
            self.removetaskbutton.config(fg='white', bg='purple')

            self.changeprogressbutton = Button(self.edittaskwindow, text="Update Progress", command=self.change,width=20)
            self.changeprogressbutton.grid(row=2, column=2)
            self.changeprogressbutton.config(fg='white', bg='purple')

    def delete(self):
        self.removetask = self.task_list.index(self.edittasksp.get())
        self.task_list.pop(self.removetask)
        self.edittaskwindow.destroy()

    def change(self):
        print(self.task_list.index(self.edittasksp.get()))
        self.changetaskprogressindex = self.task_list.index(self.edittasksp.get())
        self.changetaskprogresswindow = Tk()
        self.changetaskprogresswindow.title('Update Task Progress')
        self.changetaskprogresswindow.config(bg='gold')
        self.edittasklb = Label(self.changetaskprogresswindow, text='Update Task Progress', width=20)
        self.edittasklb.grid(row=1, column=1)
        self.edittasklb.config(fg='white', bg='purple')
        self.edittasklb = Label(self.changetaskprogresswindow, text='Update Task Progress', width=20)
        self.edittasklb.grid(row=1, column=1)
        self.edittasklb.config(fg='white', bg='purple')
        self.changetasksp = Spinbox(self.changetaskprogresswindow, values=self.progress)
        self.changetasksp.grid(row=1, column=2, padx=2)
        self.changetaskbutton = Button(self.changetaskprogresswindow, text="Update Progress", command=self.changed,
                                       width=20)
        self.changetaskbutton.grid(row=2, column=2, padx=2)
        self.edittaskwindow.destroy()

    def changed(self):
        print(self.progress_list)
        print(self.changetaskprogressindex)
        print(self.progress.index(self.changetasksp.get()))

        self.progress_list[self.changetaskprogressindex] = self.progress.index(self.changetasksp.get())
        self.changetaskprogresswindow.destroy()

    def view(self):
        self.tw = Tk()
        self.tw.title("Task")
        self.tw.config(bg='gold')
        frame5 = Frame(self.tw)
        frame6 = Frame(self.tw)
        frame5.grid(row=1)
        frame6.grid(row=2)
        self.initial = Label(frame5, text="TO DO", width=10)
        self.initial.grid(row=0, column=0)
        self.initial.config(fg='white', bg='purple')
        self.firstp = Label(frame5, text="In Progress", width=10)
        self.firstp.grid(row=0, column=1)
        self.firstp.config(fg='white', bg='purple')
        self.secondp = Label(frame5, text="Done", width=10)
        self.secondp.grid(row=0, column=2)
        self.secondp.config(fg='white', bg='purple')
        print(self.task_list)
        for x in range(0, len(self.task_list)):
            taskcolor_list = ['red', 'orange', 'green']
            self.taskk = Label(frame5, text=self.task_list[x] + "\n Due:" + self.duedate_list[x])
            self.taskk.config(bg=taskcolor_list[self.progress_list[x]], width=30)
            self.taskk.grid(columnspan=3, row=x + 1, column=0)
        self.quittask = Button(frame6, text="Exit", width=32, command=self.tw.destroy)
        self.quittask.grid(row=0, columnspan=3)
        self.quittask.config(fg='white', bg='purple')

class Final(Task):
    def __init__(self):
        window = Tk()
        window.title('Private Learning Assistant')
        window.config(bg='gold')
        Schedule.__init__(self)
        Task.__init__(self)
        frame1 = Frame(window)
        frame2 = Frame(window)
        frame3 = Frame(window)
        frame4 = Frame(window)

        frame1.grid(row=1)
        frame2.grid(row=2)
        frame3.grid(row=3)
        frame4.grid(row=4)
        self.name = Label(frame1, text='Private Learning Assistant', width=60, height=4)
        self.name.grid(row=1, column=1, columnspan=2)
        self.name.config(bg='gold')
        self.setclassbt = Button(frame2, text="Add Class", width=30, height=5, command=self.schadd)
        self.setclassbt.grid(row=1, column=1)
        self.setclassbt.config(fg='white', bg='purple')
        self.rbt = Button(frame2, text="Edit Schedule", width=30, height=5, command=self.schedit)
        self.rbt.grid(row=2, column=1)
        self.rbt.config(fg='white', bg='purple')
        self.viewbt = Button(frame2, text="View Schedule", width=30, height=5, command=self.schview)
        self.viewbt.grid(row=3, column=1)
        self.viewbt.config(fg='white', bg='purple')

        self.settaskbt = Button(frame2, text="Add Task", width=30, height=5, command=self.taskadd)
        self.settaskbt.grid(row=1, column=2)
        self.settaskbt.config(fg='white', bg='purple')
        self.rtaskbt = Button(frame2, text="Edit Task", width=30, height=5, command=self.taskedit)
        self.rtaskbt.grid(row=2, column=2)
        self.rtaskbt.config(fg='white', bg='purple')
        self.viewtaskbt = Button(frame2, text="View Task", width=30, height=5, command=self.taskview)
        self.viewtaskbt.grid(row=3, column=2)
        self.viewtaskbt.config(fg='white', bg='purple')

        self.exitbutton = Button(frame3, text="Exit", command=window.destroy, width=61, height=5)
        self.exitbutton.grid(columnspan=2, column=1)
        self.exitbutton.config(fg='white', bg='purple')
        # self.image1 = PhotoImage(file=r'/Users/thitiwatsornmanee/Desktop/peach-cat-mochi-peach-cat.gif')
        self.imagee = Label(frame4)
        self.imagee.grid()
        window.mainloop()

    def schadd(self):
        Schedule.add(self)

    def schedit(self):
        Schedule.edit(self)

    def schview(self):
        Schedule.view(self)

    def taskadd(self):
        Task.add(self)

    def taskedit(self):
        Task.edit(self)

    def taskview(self):
        Task.view(self)



Final()