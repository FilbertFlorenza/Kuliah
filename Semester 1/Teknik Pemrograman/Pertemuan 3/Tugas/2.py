import tkinter as tk
from tkinter import messagebox

def check_nilai():
    try:
        nilai = int(entry.get())
        if nilai >=86:
            result = "Sangat Baik"
        elif nilai >= 76:
            result = "Baik"
        elif nilai >= 66:
            result = "Cukup"
        elif nilai >= 56:
            result = "Kurang"
        else:
            result = "Gagal"

        messagebox.showinfo("Evaluasi", f'Nilai: {nilai}\nEvaluasi: {result}\n')
    except ValueError:
        messagebox.showinfo("Error","Masukkan nilai yang valid")

root = tk.Tk()
root.title("Cek Nilai")
root.geometry("300x200")

label = tk.Label(root, text="Masukkan Nilai")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root,text="Evaluasi",command=check_nilai)
button.pack(pady=20)

root.mainloop()