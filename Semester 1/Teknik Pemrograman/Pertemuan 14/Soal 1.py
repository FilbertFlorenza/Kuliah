import tkinter as tk
from tkinter import *
def divide(a,b):
    try:
        a = int(a)
        b = int(b)
        if b == 0:
            raise ZeroDivisionError
        errorMessage.set('')
        result.set(a/b)
    except ValueError:
        errorMessage.set('Input harus berupa angka')
    except ZeroDivisionError:
        errorMessage.set('Tidak bisa bagi dengan 0')

window = tk.Tk()
window.title('Soal 1')

frame = tk.Frame(window)
frame.grid(row=0,column=0,padx=10,pady=10)

input1 = IntVar()
input2 = IntVar()
result = IntVar()
errorMessage = StringVar()

inputFrame = tk.Frame(frame)
inputFrame.grid(row=1,column=0)
inputLabel1 = tk.Label(inputFrame, text='Masukkan A: ')
inputLabel2 = tk.Label(inputFrame, text='Masukkan B: ')
inputLabel1.grid(row=0,column=0, padx=5, sticky='w')
inputLabel2.grid(row=1,column=0, padx=5, sticky='w')

inputEntry1 = tk.Entry(inputFrame, textvariable=input1)
inputEntry2 = tk.Entry(inputFrame, textvariable=input2)
inputEntry1.grid(row=0,column=1, padx=5, sticky='w')
inputEntry2.grid(row=1,column=1, padx=5, sticky='w')

resultLabel = tk.Label(inputFrame, text='Result: ')
resultLabel.grid(row=2, column=0, padx=5, sticky='w')
resultEntry = tk.Entry(inputFrame, textvariable=result, state=DISABLED)
resultEntry.grid(row=2, column=1, padx=5, sticky='w')

errorLabel = tk.Label(frame, textvariable=errorMessage, fg='red')
errorLabel.grid(row=3, column=0, padx=5, sticky='w')

calculateButton = tk.Button(frame, text='Kalkulasi', command=lambda: divide(input1.get(),input2.get()))
calculateButton.grid(row=4,column=0, padx=5, sticky='w')

window.mainloop()
