
# Import module 
from tkinter import *
    
# Create object 
splash_root = Tk() 
    
# Adjust size 
splash_root.geometry("200x200")
  
# Set Label
splash_label = Label(splash_root,text="Splash Screen",font=18)
splash_label.pack()
  
# main window function
def main():  
    # destory splash window
    splash_root.destroy()
  
    # Execute tkinter 
    root = Tk() 
        
    # Adjust size 
    root.geometry("400x400") 
  
# Set Interval
splash_root.after(3000,main)
  
# Execute tkinter 
mainloop()