#Made by Filbert
import tkinter as tk
from functools import partial
from tkinter import StringVar

root = tk.Tk()

def print_buy(fruit):
    buy.set('You buy 1 ' + fruit)

buy = StringVar()

for f in ['Apple', 'Banana']:
    btn = tk.Button(root, text='Buy ' + f, command= lambda f=f:print_buy(f))
    btn.pack(fill=tk.BOTH,padx=10,pady=5)

label = tk.Label(root,textvariable=buy)
label.pack()

root.mainloop()
    