# run pip install ttkbootstrap di terminal sebelum dijalanin
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

# Save Data Function
def save_data():
    # Get entry values
    kodeKategori = kodeKategoriEntry.get()
    nama = namaEntry.get()
    jenis = jenisCombo.get()
    
    # Check if input is empty
    if(kodeKategori == '' or nama == '' or jenis == ''):
        Messagebox.show_error("Masukkan input yang benar")
        return False
    
    # Insert values into the treeview
    tree.insert('', 'end', values=(kodeKategori, nama, jenis))
    
    # Delete entry values
    kodeKategoriEntry.delete(0, ttk.END)
    namaEntry.delete(0, ttk.END)
    jenisCombo.set("")

def update_data():
    # Get entry values
    kodeKategori = kodeKategoriEntry.get()
    nama = namaEntry.get()
    jenis = jenisCombo.get()
    selected = tree.focus()

    # Check if input is empty
    if(kodeKategori == '' or nama == '' or jenis == ''):
        Messagebox.show_error("Masukkan input yang benar")
        return False
    
    # Check if no list is selected
    if(not selected):
        Messagebox.show_error("Pilih value dalam list")
        return False
    
    tree.item(selected,values=(kodeKategori, nama, jenis))

    # Delete entry values
    kodeKategoriEntry.delete(0, ttk.END)
    namaEntry.delete(0, ttk.END)
    jenisCombo.set("")
    
def delete_data():
    # Get list selection
    selected = tree.focus()
    
    # Check if no list is selected
    if(not selected):
        Messagebox.show_error("Pilih value dalam list")
        return False
    
    tree.delete(selected)

#Initialize window
window = ttk.Window(themename="darkly")  # Choose a theme like "flatly", "darkly", etc.
window.title("Teknik Pemrograman Pertemuan 10")

#Input Frame
inputFrame = ttk.Frame(window)
inputFrame.grid(row=0, column=0, columnspan=2, pady=5)

#Input Labels
ttk.Label(window, text="Kode Kategori", bootstyle="light").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ttk.Label(window, text="Nama", bootstyle="light").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ttk.Label(window, text="Jenis", bootstyle="light").grid(row=2, column=0, padx=10, pady=5, sticky="w")

#Input Entry
entryWidth = 40
jenisComboValues = ("Buku", "Elektronik", "Fashion", "Makanan & Minuman", "Peralatan Olahraga", "Peralatan Otomotif")
kodeKategoriEntry = ttk.Entry(window, width=entryWidth,)
namaEntry = ttk.Entry(window, width=entryWidth)
jenisCombo = ttk.Combobox(window, width=entryWidth - 2, values=jenisComboValues)

kodeKategoriEntry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
namaEntry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
jenisCombo.grid(row=2, column=1, padx=10, pady=5, sticky="w")

#Button Frame
buttonFrame = ttk.Frame(window)
buttonFrame.grid(row=3, column=0, columnspan=2, pady=10,sticky="w")

saveButton = ttk.Button(buttonFrame, command= save_data, text="Save", bootstyle="success-outline")
updateButton = ttk.Button(buttonFrame, command=update_data, text="Update", bootstyle="warning-outline")
deleteButton = ttk.Button(buttonFrame, command=delete_data, text="Delete", bootstyle="danger-outline")

saveButton.grid(row=0, column=0, padx=10)
updateButton.grid(row=0, column=1, padx=10)
deleteButton.grid(row=0, column=2, padx=10)

#Tree View
columns = ("Kode Kategori", "Nama", "Jenis")
tree = ttk.Treeview(window, columns=columns, show='headings')
tree.heading("Kode Kategori", text="Kode Kategori")
tree.heading("Nama", text="Nama")
tree.heading("Jenis", text="Jenis")
tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
