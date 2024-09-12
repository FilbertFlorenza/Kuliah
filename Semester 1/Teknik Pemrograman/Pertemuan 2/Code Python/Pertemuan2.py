print("MENGHITUNG LUAS & KELILING TRAPESIUM\n")

# Get Input from User
sisi_atas = float(input("Masukkan Sisi Atas: "))
sisi_bawah = float(input("Masukkan Sisi Bawah: "))
tinggi = float(input("Masukkan Tinggi: "))
garis_miring_1 = float(input("Masukkan Garis Miring 1: "))
garis_miring_2 = float(input("Masukkan Garis Miring 2: "))

#Calculate Luas
luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi

# Calculate Keliling
keliling = sisi_atas + sisi_bawah + garis_miring_1 + garis_miring_2

# Print result
print(f"Luas : {luas}" )
print(f"Keliling: {keliling}")