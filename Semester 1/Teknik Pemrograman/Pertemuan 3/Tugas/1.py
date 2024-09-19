import tkinter as tk
from tkinter import messagebox

def check_npm():
    npm = entry.get()
    if npm == "130029":
        messagebox.showinfo("Nama","Dinda")
    elif npm == "130102":
        messagebox.showinfo("Nama","Rino")
    else:
        messagebox.showerror("Error","Tidak terdaftar")

root = tk.Tk()
root.title("Cek NPM")
root.geometry("300x200")

label = tk.Label(root, text="Masukkan NPM")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root,text="Cek",command=check_npm)
button.pack(pady=20)

root.mainloop()






