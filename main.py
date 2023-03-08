from tkinter import *
import math

tk = Tk()
tk.title("Complex Calculater")
e = Entry(tk, width=150, borderwidth=10)
e.grid(row=0, columnspan=2, rowspan=5, padx=5, pady=5)

tk.mainloop()



# function start

def thebutton(number):
    the_current = e.get()
    e.delete(0, END)
    e.insert(0, str(the_current) + str(number))


def clear_button():
    e.delete(0, END)


def the_button_adds():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "addition"
    functionnum = int(num1)
    e.delete(0, END)


def equal_to():
    num2 = e.get()
    e.delete(0, END)
    if mathematics == "addition":
        e.insert(0, functionnum+int(num2))
    if mathematics == "subtraction":
        e.insert(0, functionnum - int(num2))
    if mathematics == "multiplication":
        e.insert(0, functionnum * int(num2))
    if mathematics == "division":
        e.insert(0, functionnum / int(num2))




