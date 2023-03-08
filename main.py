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
        e.insert(0, functionnum + int(num2))
    if mathematics == "subtraction":
        e.insert(0, functionnum - int(num2))
    if mathematics == "multiplication":
        e.insert(0, functionnum * int(num2))
    if mathematics == "division":
        e.insert(0, functionnum / int(num2))

    if mathematics == "raisedto":
        e.insert(0, functionnum ** int(num2))
    if mathematics == "squareroot":
        e.insert(0, math.sqrt(functionnum))
    if mathematics == "percentage":
        e.insert(0, functionnum / 100)
    if mathematics == "sin":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.sin(rad))
    if mathematics == "cos":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.cos(rad))
    if mathematics == "tan":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.tan(rad))
    if mathematics == "csc":
        rad = functionnum * (math.pi / 180)
        e.insert(0, 1 / math.sin((rad)))
    if mathematics == "sec":
        rad = functionnum * (math.pi / 180)
        e.insert(0, 1 / math.cos((rad)))
    if mathematics == "cot":
        rad = functionnum * (math.pi / 180)
        e.insert(0, 1 / math.tan((rad)))
    if mathematics == "ave":
        e.insert((functionnum + int(num2)) / 2)
    if mathematics == "square":
        e.insert(0, functionnum ** 2)
    if mathematics == "cube":
        e.insert(0, functionnum ** 3)
    if mathematics == "naturallog":
        e.insert(0, math.log(functionnum))
    if mathematics == "e":
        e.insert(0, math.exp(functionnum))
    if mathematics == "log":
        e.insert(0, math.log10(functionnum))
    if mathematics == "negative":
        e.insert(0, functionnum * -1)
    if mathematics == "absolutevalue":
        e.insert(0, abs(functionnum))
    if mathematics == "factorial":
        e.insert(0, math.factorial(functionnum))
    if mathematics == "2raisedto":
        e.insert(0, 2 ** functionnum)
    if mathematics == "inverse":
        e.insert(0, functionnum ** (-1))
    if mathematics == "sininverse":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.asin(rad))
    if mathematics == "cosinverse":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.acos(rad))
    if mathematics == "taninverse":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.atan(rad))


def thebuttonsubstract():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "substraction"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonmultiplication():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "multiplication"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttondivision():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "division"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonraisedtopowerof():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "raisedto"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonsquareroot():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "squareroot"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonpercent():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "percentage"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonsin():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sin"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttoncos():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cos"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttontan():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "tan"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttoncsc():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "csc"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonsec():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sec"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttoncot():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cot"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonaverage():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "ave"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonsquare():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "square"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttoncube():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cube"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonln():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "naturallog"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonetothex():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "e"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonlog():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "log"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonnegative():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "negative"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonabsoulutevalue():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "absolutevalue"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonfactorial():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "factorial"
    functionnum = int(num1)
    e.delete(0, END)


def thebutton2raisedto():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "2raisedto"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttoninverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "inverse"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttonsininverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sininverse"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttoncosinverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cosinverse"
    functionnum = int(num1)
    e.delete(0, END)


def thebuttontaninverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "taninverse"
    functionnum = int(num1)
    e.delete(0, END)
