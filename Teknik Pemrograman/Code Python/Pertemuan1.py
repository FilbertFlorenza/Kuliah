def main():
    # Komen / Unkomen aja klo mau run ini
    # get_luas()
    get_luas_trapesium()

def get_luas():
    # Print title
    print("MENGHITUNG LUAS PERSEGI PANJANG\n")

    # Get Input from User
    panjang = float(input("Masukkan Panjang: "))
    lebar = float(input("Masukkan Lebar: "))

    # Calculate luas
    luas = panjang * lebar

    # Print luas
    print(luas)

def get_luas_trapesium():
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

    # Print
    print(luas)
    print(keliling)


if __name__ == "__main__":
    main()