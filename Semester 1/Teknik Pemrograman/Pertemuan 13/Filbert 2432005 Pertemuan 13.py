# run pip install ttkbootstrap di terminal sebelum dijalanin
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

# Image Path
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
image_path = "test.png"
abs_image_path = os.path.join(script_dir, image_path)

#Initialize window
window = tk.Tk()
window.title("Teknik Pemrograman Pertemuan 13")
banner = ImageTk.PhotoImage(Image.open(abs_image_path))  

def login_page():

    def login():
        email = emailEntry.get()
        password = passwordEntry.get()
        if(email == 'admin' and password == 'admin'):
            inputFrame.destroy()
            customer_input()

    #Input Frame
    inputFrame = ttk.Frame(window)
    inputFrame.grid(row=1, column=0, columnspan=2, pady=5)

    #Input Labels
    emailLabel = ttk.Label(inputFrame, text="Email address")
    passwordLabel = ttk.Label(inputFrame, text="Password")

    #Input Entry
    entryWidth = 40
    emailEntry = ttk.Entry(inputFrame, width=entryWidth)
    passwordEntry = ttk.Entry(inputFrame, width=entryWidth, show="*")
    
    emailLabel.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    emailEntry.grid(row=1, column=0, padx=10)
    passwordLabel.grid(row=2, column=0, padx=10, pady=5,sticky='w')
    passwordEntry.grid(row=3, column=0)

    login_button = tk.Button(inputFrame, text="Login", command=login, width=entryWidth-6, fg="#FFFFFF", bg="#3B71CA")
    login_button.grid(row=4, column=0, padx=10, pady=10)

    hintLabel = ttk.Label(inputFrame, text="email: admin | password: admin")
    hintLabel.grid(row=5, column=0, padx=10, pady=5)

def customer_input():
    # Save Data Function
    def save_data():
        # Get entry values
        kodeKategori = kodeCustomerEntry.get().strip()
        nama = namaEntry.get().strip()
        jenisKelamin = jenisKelaminVar.get().strip()
        alamat = alamatCombo.get().strip()
        
        # Check if input is empty
        if(kodeKategori == '' or nama == '' or jenisKelamin == '' or alamat == ''):
            messagebox.show_error("Masukkan input yang benar")
            return False
        
        # Insert values into the treeview
        tree.insert('', 'end', values=(kodeKategori, nama, jenisKelamin, alamat))
        
        # Delete entry values
        kodeCustomerEntry.delete(0, ttk.END)
        namaEntry.delete(0, ttk.END)
        alamatCombo.set("")

    def update_data():
        # Get entry values
        kodeKategori = kodeCustomerEntry.get().strip()
        nama = namaEntry.get().strip()
        alamat = alamatCombo.get().strip()
        jenisKelamin = jenisKelaminVar.get().strip()
        selected = tree.focus()

        # Check if input is empty
        if(kodeKategori == '' or nama == '' or jenisKelamin == '' or alamat == ''):
            messagebox.show_error("Masukkan input yang benar")
            return False
        
        # Check if no list is selected
        if(not selected):
            messagebox.show_error("Pilih value dalam list")
            return False
        
        tree.item(selected,values=(kodeKategori, nama, jenisKelamin, alamat))

        # Delete entry values
        kodeCustomerEntry.delete(0, ttk.END)
        namaEntry.delete(0, ttk.END)
        alamatCombo.set("")

    def delete_data():
        # Get list selection
        selected = tree.focus()
        
        # Check if no list is selected
        if(not selected):
            messagebox.show_error("Pilih value dalam list")
            return False
    
        tree.delete(selected)

    def clear_data():
        tree.delete(*tree.get_children())

    # Banner
    ttk.Label(window,image=banner).grid(row=0, column=0, pady=5,sticky='e')

    #Input Frame
    inputFrame = ttk.Frame(window)
    inputFrame.grid(row=1, column=0, columnspan=2, pady=5, sticky='w')

    #Input Labels
    ttk.Label(inputFrame, text="KODE CUSTOMER").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ttk.Label(inputFrame, text="NAMA CUSTOMER").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    ttk.Label(inputFrame, text="Jenis Kelamin").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    ttk.Label(inputFrame, text="Alamat").grid(row=3, column=0, padx=10, pady=5, sticky="w")

    # Set Variable
    jenisKelaminVar = tk.StringVar()

    #Input Entry
    entryWidth = 40
    alamatComboValues = ("Batam", "Tanjung Pinang", "Bintan")
    kodeCustomerEntry = ttk.Entry(inputFrame, width=entryWidth,)
    namaEntry = ttk.Entry(inputFrame, width=entryWidth, )
    radioFrame = ttk.Frame(inputFrame)
    
    maleRadio = ttk.Radiobutton(radioFrame, text='Pria', value='Pria', variable=jenisKelaminVar)
    femaleRadio = ttk.Radiobutton(radioFrame, text='Wanita', value='Wanita', variable=jenisKelaminVar)
    alamatCombo = ttk.Combobox(inputFrame, width=entryWidth - 2, values=alamatComboValues)

    
    kodeCustomerEntry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    namaEntry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    radioFrame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    maleRadio.grid(row=0, column=1, pady=5, sticky="w")
    femaleRadio.grid(row=0, column=2, pady=5, sticky="w")
    alamatCombo.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    #Tree View
    columns = ("KODE CUSTOMER", "NAMA CUSTOMER", "JENIS KELAMIN", "ALAMAT")
    tree = ttk.Treeview(window, columns=columns, show='headings')
    tree.heading("KODE CUSTOMER", text="KODE CUSTOMER")
    tree.heading("NAMA CUSTOMER", text="NAMA CUSTOMER")
    tree.heading("JENIS KELAMIN", text="JENIS KELAMIN")
    tree.heading("ALAMAT", text="ALAMAT")
    tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    #Button Frame
    buttonFrame = ttk.Frame(window)
    buttonFrame.grid(row=4, column=0, columnspan=2, pady=10,sticky="w")

    saveButton = ttk.Button(buttonFrame, command= save_data, text="SIMPAN")
    updateButton = ttk.Button(buttonFrame, command=update_data, text="EDIT")
    deleteButton = ttk.Button(buttonFrame, command=delete_data, text="DELETE")
    clearButton = ttk.Button(buttonFrame, command=clear_data, text="BERSIH")

    saveButton.grid(row=0, column=0, padx=10)
    updateButton.grid(row=0, column=1, padx=10)
    deleteButton.grid(row=0, column=2, padx=10)
    clearButton.grid(row=0, column=3, padx=10)

login_page()
# customer_input()
# Run the application
window.mainloop()
