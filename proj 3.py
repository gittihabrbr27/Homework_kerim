import tkinter as tk

root = tk.Tk()

root.config(bg="grey")

entry = tk.Entry()
entry.grid(row=0, column=0, columnspan=2, pady=50, padx=30)

button = tk.Button(text="include capital letters?", bg="cyan2",fg="purple")
button.grid(row=1, column=1, columnspan=1, pady=50, padx=30)

symbols = tk.Button(text="include symbols",bg="cyan2",fg="purple")
symbols.grid(row=1, column=0, columnspan=1, pady=50, padx=30)

small_letters = tk.Button(text="include small letters?", bg="cyan2",fg="purple")
small_letters.grid(row=2, column=0, columnspan=1, pady=50, padx=30)

length = tk.Entry()
length.grid(row=3, column=0, columnspan=2, pady=50, padx=30)
length.insert(0, 'Enter password length')

include_numbers = tk.Button(text="include numbers?", bg="cyan2",fg="purple")
include_numbers.grid(row=2, column=1, columnspan=1, pady=50, padx=30)

start = tk.Button(text="start", width=50, bg="cyan2",fg="purple")
start.grid(row=4, column=0, columnspan=2, pady=20, padx=0)

root.mainloop()


import random


def generate_password(password_length, CL=True, LL=True, numbers=True, symbols=True):
    count = password_length//(CL + LL + numbers + symbols)
    numbers = [chr(random.randint(48, 57)) for i in range(count) if numbers]
    symbols = [chr(random.randint(33, 47)) for i in range(count) if symbols]
    LL =[chr(random.randint(97,122)) for i in range(count) if LL]
    CL= [chr(random.randint(65,90)) for i in range(count) if CL]
    print(numbers, symbols,LL,CL)


generate_password(10, numbers=True)