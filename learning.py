# from tkinter import *
#
# root = Tk()
#
# Label(root, text="Red Sun", bg="red", fg="white").pack()
# Label(root, text="Green Grass", bg="green", fg="black").pack()
# Label(root, text="Blue Sky", bg="blue", fg="white").pack()
#
# mainloop()

# from tkinter import *
#
# root = Tk()
#
# w = Label(root, text="red", bg="red", fg="white")
# w.pack(padx=5, pady=20, side=RIGHT)
# w = Label(root, text="green", bg="green", fg="black")
# w.pack(padx=5, pady=20, side=LEFT)
# w = Label(root, text="blue", bg="blue", fg="white")
# w.pack(padx=5, pady=20, side=RIGHT)
#
# mainloop()

https://www.python-course.eu/tkinter_layout_management.php
http://zetcode.com/gui/tkinter/layout/
http://effbot.org/tkinterbook/pack.htm

import tkinter as tk
import random

root = tk.Tk()
# width x height + x_offset + y_offset:
root.geometry("170x200+30+30")

languages = ['Python','Perl','C++','Java','Tcl/Tk']
labels = range(5)
for i in range(5):
   ct = [random.randrange(256) for x in range(3)]
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = tk.Label(root,
                text=languages[i],
                fg='White' if brightness < 120 else 'Black',
                bg=bg_colour)
   l.place(x = 20, y = 30 + i*30, width=120, height=25)

root.mainloop()
