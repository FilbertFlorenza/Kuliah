import tkinter as tk
from tkinter import ttk
from tkinter import *
def calculate():
    vehicle = vehicleCombo.get().lower()
    duration = durationEntry.get()
    if not vehicle == '' and not duration == '': 
        try:
            duration = int(duration)
            if duration < 0:
                result.set('Output: Durasi tidak boleh negatif.')
                return
            if vehicle == 'motor':
                resultTotal = 2000 * duration
            elif vehicle == 'mobil':
                resultTotal = 5000 * duration
            else:
                resultTotal = 10000 * duration
            result.set(f'Output: Total tarif parkir: Rp {resultTotal:,}')
        except ValueError as message:
            result.set('Output: Durasi parkir harus berupa angka positif.')

window = tk.Tk()
window.title('Soal 3')


frame = tk.Frame(window)
frame.grid(row=0,column=0,padx=10,pady=10)

errorMessage = StringVar()
result = StringVar()
result.set('Output: ')

inputFrame = tk.Frame(frame)
inputFrame.grid(row=1,column=0)
vehicleLabel = tk.Label(inputFrame, text='Masukkan jenis kendaraan: ')
vehicleLabel.grid(row=0,column=0, padx=5, sticky='w')
durationLabel = tk.Label(inputFrame, text='Masukkan durasi parkir (jam): ')
durationLabel.grid(row=1,column=0, padx=5, sticky='w')

vehicles = ('Motor','Mobil','Bus')
vehicleCombo = ttk.Combobox(inputFrame, values=vehicles)
vehicleCombo.grid(row=0, column=1, padx=5, sticky='w')
durationEntry = tk.Entry(inputFrame)
durationEntry.grid(row=1,column=1, padx=5, pady=5, sticky='w')

calculateButton = tk.Button(frame, text='Kalkulasi', command=calculate)
calculateButton.grid(row=2,column=0, padx=5, sticky='w')

resultLabel = tk.Label(frame, textvariable=result)
resultLabel.grid(row=3, column=0, padx=5, pady=5, sticky='w')



window.mainloop()
