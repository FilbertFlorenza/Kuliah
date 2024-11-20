#Made by Stanley and Ibnu
import tkinter as tk
from tkinter import messagebox

karyawan = ["budi", "bunga", "alex", "mawar", "dani", "sultan"]

def Cek_Status(event=None):
    nama = entry_nama.get().strip().lower()  
    if nama in karyawan:
        messagebox.showinfo("Status", f"{nama.capitalize()} adalah Karyawan.🙂")
    else:
        messagebox.showinfo("Status", f"{nama.capitalize()} Bukan Karyawan.😎")

root = tk.Tk()
root.title("Status Karyawan")
root.geometry("400x250")

label = tk.Label(root, text="Masukkan Nama:")
label.pack(pady=10)

entry_nama = tk.Entry(root)
entry_nama.pack(pady=10)
entry_nama.bind("<Return>", Cek_Status)

btn_cek = tk.Button(root, text="Cek Status", command=Cek_Status)
btn_cek.pack(pady=10)

root.mainloop()