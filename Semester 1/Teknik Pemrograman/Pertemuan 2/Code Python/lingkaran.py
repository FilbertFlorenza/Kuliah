print("MENGHITUNG LUAS & KELILING LINGKARAN\n")

pi = 3.14
# Get Input from User
jari_jari = float(input("Masukkan Jari Jari: "))


#Calculate Luas
luas = pi * (jari_jari * jari_jari)

# Calculate Keliling
keliling = pi * (jari_jari * 2)

# Print result
print(f"Luas : {luas}" )
print(f"Keliling: {keliling}")