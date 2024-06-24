from tkinter import *

window = Tk()
window.title("Calculator")
window.config(padx=10, pady=10)
expression = ""


def button_click(item):
    global expression
    expression = expression + str(item)
    user_input.config(text=expression)


def button_clear():
    global expression
    expression = ""
    user_input.config(text=expression)


def button_equal():
    global expression
    result = str(eval(expression))
    user_input.config(text=result)


user_input = Label(text="0", bg="white", width=16, anchor="e", font=("Arial", 24))
user_input.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)

one = Button(text="1", command=lambda: button_click(1))
one.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

two = Button(text="2", command=lambda: button_click(2))
two.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")

three = Button(text="3", command=lambda: button_click(3))
three.grid(row=1, column=2, padx=3, pady=3, sticky="nsew")

divide = Button(text="/", command=lambda: button_click("/"))
divide.grid(row=1, column=3, padx=3, pady=3, sticky="nsew")

four = Button(text="4", command=lambda: button_click(4))
four.grid(row=2, column=0, padx=3, pady=3, sticky="nsew")

five = Button(text="5", command=lambda: button_click(5))
five.grid(row=2, column=1, padx=3, pady=3, sticky="nsew")

six = Button(text="6", command=lambda: button_click(6))
six.grid(row=2, column=2, padx=3, pady=3, sticky="nsew")

mul = Button(text="*", command=lambda: button_click("*"))
mul.grid(row=2, column=3, padx=3, pady=3, sticky="nsew")

seven = Button(text="7", command=lambda: button_click(7))
seven.grid(row=3, column=0, padx=3, pady=3, sticky="nsew")

eight = Button(text="8", command=lambda: button_click(8))
eight.grid(row=3, column=1, padx=3, pady=3, sticky="nsew")

nine = Button(text="9", command=lambda: button_click(9))
nine.grid(row=3, column=2, padx=3, pady=3, sticky="nsew")

sub = Button(text="-", command=lambda: button_click("-"))
sub.grid(row=3, column=3, padx=3, pady=3, sticky="nsew")

zero = Button(text="0", command=lambda: button_click(0))
zero.grid(row=4, column=0, padx=3, pady=3, sticky="nsew")

clear = Button(text="C", command=lambda: button_clear())
clear.grid(row=4, column=1, padx=3, pady=3, sticky="nsew")

add = Button(text="+", command=lambda: button_click("+"))
add.grid(row=4, column=2, padx=3, pady=3, sticky="nsew")

equal = Button(text="=", command=lambda: button_equal())
equal.grid(row=4, column=3, padx=3, pady=3, sticky="nsew")

window.mainloop()
