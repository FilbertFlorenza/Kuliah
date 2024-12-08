import tkinter as tk
from tkinter import *
def result():
    try:
        number = int(numberEntry.get())
        if number < 0:
            errorMessage.set('Angka tidak boleh negatif.')
            return
        errorMessage.set('')
        for i in range(10):
            multiplication = (i+1) * number
            label = tk.Label(resultFrame, text=f'{number} x {i+1} = {multiplication}')
            label.grid(row=i,column=0,padx=5,sticky='w')

    except ValueError:
        errorMessage.set('Input tidak valid. Harap masukkan angka.')

window = tk.Tk()
window.title('Soal 2')


frame = tk.Frame(window)
frame.grid(row=0,column=0,padx=10,pady=10)

errorMessage = StringVar()

numberFrame = tk.Frame(frame)
numberFrame.grid(row=1,column=0)
numberLabel = tk.Label(numberFrame, text='Masukkan Angka: ')
numberLabel.grid(row=0,column=0, padx=5, sticky='w')

numberEntry = tk.Entry(numberFrame)
numberEntry.grid(row=0,column=1, padx=5, sticky='w')

errorLabel = tk.Label(frame, textvariable=errorMessage, fg='red')
errorLabel.grid(row=3, column=0, padx=5, sticky='w')

calculateButton = tk.Button(frame, text='Kalkulasi', command=result)
calculateButton.grid(row=4,column=0, padx=5, sticky='w')

resultFrame = tk.Frame(frame)
resultFrame.grid(row=5, column=0, padx=5, pady=5, sticky='w')



window.mainloop()
