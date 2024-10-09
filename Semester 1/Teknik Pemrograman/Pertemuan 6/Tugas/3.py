def main():
    karyawan = ['budi', 'bunga', 'alex', 'mawar', 'dani', 'sultan']
    nama = input("Masukkan nama: ").lower()
    if nama in karyawan:
        print("Karyawan")
    else:
        print("Bukan karyawan")


if __name__ == "__main__":
    main()