'''
Python Program to Create Digital Clock
'''

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital clock")

def clock():
    tick = strftime("%H:%M:%S")
    
   
    label.config(text =tick)
    label.after(1000, clock)


label = Label(root, font = ("segoe", 150), foreground = "blue", background = "black")

label.pack(anchor= "center")

clock()
mainloop()