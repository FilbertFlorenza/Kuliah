def main():
    # A
    bilangan = 2
    addition_times = 0
    addition = 1
    while bilangan <= 16:
        print(bilangan, end='')
        if(bilangan != 16):
            print(',',end='')
        bilangan = bilangan + addition
        addition_times = addition_times + 1
        if(addition_times == 2):
            addition = addition * 2
            addition_times = 0
    print()

    # B
    bilangan = 18
    while bilangan >= 3:
        print(bilangan,end='')
        if(bilangan > 3):
            print(',',end='')
        bilangan = bilangan - 3
    print()

    # C
    for i in range(8):
        print(i*7,end='')
        if(i+1 < len(range(8))):
            print(',',end='')

if __name__ == "__main__":
    main()