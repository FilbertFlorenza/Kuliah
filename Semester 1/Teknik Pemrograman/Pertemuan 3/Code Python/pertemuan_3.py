nilai = int(input("Masukkan Nilai: "))

if nilai >= 85:
    print("Predikat A / Memuaskan")
elif nilai >= 75:
    print("Predikat B / Bagus")
elif nilai >= 65:
    print("Predikat C / Cukup")
elif nilai >= 55:
    print("Predikat D / Kurang")
else:
    print("Predikat E / Sangat Kurang")