def main():
    numbers = input("Masukkan nomor: ")
    array = numbers.split(',')
    array_number = []
    for i in array:
        array_number.append(int(i))
    array_number.sort()    
    print(array_number)


if __name__ == "__main__":
    main()