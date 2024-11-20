#Made by Aziz
import tkinter as tk

days_of_week = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]


def show_day():
    try:
        day_index = int(entry.get()) - 1 
        if 0 <= day_index < len(days_of_week):
            result_label.config(text=f"Hari ke-{day_index + 1}: {days_of_week[day_index]}")
        else:
            result_label.config(text="Input tidak valid. Masukkan angka 1 hingga 7.")
    except ValueError:
        result_label.config(text="Masukkan angka yang valid.")


root = tk.Tk()
root.title("Aplikasi Hari")


label = tk.Label(root, text="Masukkan angka (1-7):")
label.pack(pady=10)


entry = tk.Entry(root)
entry.pack(pady=5)


button = tk.Button(root, text="Tampilkan Hari", command=show_day)
button.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()
