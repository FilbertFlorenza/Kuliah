def main():
    total_belanja = int(input("Belanja: "))

    if(total_belanja > 300):
        total_bayar = total_belanja - (total_belanja * 0.15)
        diskon = "15%"
    else:
        diskon = "Tidak ada diskon"
        total_bayar = total_belanja
    
    print(f'Diskon: {diskon}\nBayar: {total_bayar}')
if __name__ == "__main__":
    main()