import random
from tkinter import *

root = Tk()

# here goes the drawing part

root.mainloop()

from tkinter import *

root = Tk()

canvas = Canvas(root, width='200', height='100')
canvas.pack()

teal_line = canvas.create_line(0, 0, 200, 50, fill='light sea green')
lime_box = canvas.create_rectangle(50, 50, 100, 90, fill='lime green')
olive_oval = canvas.create_oval(120, 10, 180, 90, fill='olive drab')
from tkinter import *

root = Tk()

canvas = Canvas(root, width='200', height='100')
canvas.pack()
for i in range(50):
        canvas.create_oval(random,random,random,random,fill=random)
        
root.mainloop()