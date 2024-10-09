def main():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    even_number = filter(even_numbers,numbers)
    print(list(even_number))

def even_numbers(number):
    if(number % 2 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    main()