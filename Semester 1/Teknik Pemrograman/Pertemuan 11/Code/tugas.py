# run pip install ttkbootstrap before running the application
import ttkbootstrap as ttk
from ttkbootstrap import StringVar
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

#Calculate total
def calculate_total(*args):
    try:
        # Get entry values
        totalBelanjaInt = int(totalBelanjaEntry.get())

        # Set values
        bonusStr = '-'
        diskonStr = '-'
        diskonFloat = 0
        totalBayarFloat = 0
        # Calculate results
        if totalBelanjaInt >= 500000:
            bonusStr = 'Mug Cantik'
            diskonStr = '7%'
            diskonFloat = totalBelanjaInt * 0.07
            totalBayarFloat = totalBelanjaInt - diskonFloat
        elif totalBelanjaInt >=  100000:
            bonusStr = 'Coca Cola'
            diskonStr = '5%'
            diskonFloat = totalBelanjaInt * 0.05
            totalBayarFloat = totalBelanjaInt - diskonFloat
        else:
            totalBayarFloat = totalBelanjaInt

        # Change label values to results
        totalBelanja.set(f'Rp {totalBelanjaInt}')
        bonusText.set(bonusStr)
        diskonText.set(diskonStr)
        diskon.set(f'Rp {diskonFloat:.0f}')
        totalBayar.set(f'Rp {totalBayarFloat:.0f}')
    except ValueError:
        # Set to default value
        totalBelanja.set('-')
        diskonText.set('-')
        diskon.set('-')
        bonusText.set('-')
        totalBayar.set('-')

        # Show error message
        Messagebox.show_error("Masukkan total belanja yang benar")

#Initialize window
window = ttk.Window(themename="superhero")
window.title("Teknik Pemrograman Pertemuan 11 Tugas Kelompok")

#Input Frame
inputFrame = ttk.Frame(window)
inputFrame.grid(row=0, column=0, columnspan=2, pady=5)

#Input Labels
ttk.Label(window, text="Kalkulasi Diskon Total Belanja",font=('bold', 14)).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
ttk.Label(window, text="Total Belanja").grid(row=1, column=0, padx=10, pady=5, sticky="w")

#Input Entry
entryWidth = 40
totalBelanjaEntry = ttk.Entry(window, width=entryWidth)
totalBelanjaEntry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
totalBelanjaEntry.bind("<Return>", calculate_total)

#Button Frame
buttonFrame = ttk.Frame(window)
buttonFrame.grid(row=3, column=0, columnspan=2, pady=10,sticky="w")

#Buttons
saveButton = ttk.Button(buttonFrame, command= calculate_total, text="Kalkulasi", bootstyle="success-outline")
saveButton.grid(row=0, column=0, padx=10)

#Total Frame
totalFrame = ttk.Frame(window)
totalFrame.grid(row=4, column=0, columnspan=2, pady=10, sticky='w')

#Total Label
ttk.Label(totalFrame, text="Total Belanja\t:").grid(row=0,column=0,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, text="Bonus\t\t:").grid(row=1,column=0,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, text="Diskon\t\t:").grid(row=2,column=0,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, text="Total Diskon\t:").grid(row=3,column=0,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, text="Total Bayar\t:").grid(row=4,column=0,padx=10,pady=5, sticky='w')

#Total Results Label
totalBelanja = StringVar()
diskonText = StringVar()
diskon = StringVar()
bonusText = StringVar()
totalBayar = StringVar()
totalBelanja.set('-')
diskonText.set('-')
diskon.set('-')
bonusText.set('-')
totalBayar.set('-')
ttk.Label(totalFrame, textvariable=totalBelanja).grid(row=0,column=1,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, textvariable=bonusText).grid(row=1,column=1,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, textvariable=diskonText).grid(row=2,column=1,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, textvariable=diskon).grid(row=3,column=1,padx=10,pady=5, sticky='w')
ttk.Label(totalFrame, textvariable=totalBayar).grid(row=4,column=1,padx=10,pady=5, sticky='w')

# Run the application
window.mainloop()

