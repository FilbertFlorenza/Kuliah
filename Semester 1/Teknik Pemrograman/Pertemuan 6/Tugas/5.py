def main():
    numbers = input("Masukkan nomor: ")
    numbers_array = numbers.split(',')
    total_number = 0
    for number in numbers_array:
        total_number = total_number + int(number)
    print(total_number)

if __name__ == "__main__":
    main()