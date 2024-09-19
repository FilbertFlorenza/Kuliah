import tkinter as tk
from tkinter import messagebox

def kalkulasi_belanja():
    try:
        total_belanja = float(entry.get())
        bonus = "-"
        diskon = 0
        diskon_text = "0%"
        total_bayar = total_belanja
        if(total_belanja > 500000):
            bonus = "Mug Cantik"
            diskon_text = '7%'
            diskon = 0.07 * total_belanja
            total_bayar = total_belanja - diskon
        elif(total_belanja >= 100000 and total_belanja <= 499000):
            bonus = "Coca Cola"
            diskon_text = "5%"
            diskon = 0.05 * total_belanja
            total_bayar = total_belanja - diskon
            
        messagebox.showinfo("Total", f'Bonus: {bonus}\nDiskon: {diskon_text}\nTotal Diskon: {diskon:.1f}\nTotal Bayar: {total_bayar}')
    except ValueError:
        messagebox.showerror("Error","Masukkan angka yang valid")

root = tk.Tk()
root.title("Cek Belanjaan")
root.geometry("300x200")

label = tk.Label(root, text="Masukkan Total Belanja")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root,text="Kalkulasi",command=kalkulasi_belanja)
button.pack(pady=20)

root.mainloop()


