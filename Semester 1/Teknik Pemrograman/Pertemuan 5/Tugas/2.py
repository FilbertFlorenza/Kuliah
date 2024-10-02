def main():
    for i in range(1,7):
        space = len(range(1,7)) - i
        for j in range(1,7):
            if(space > 0):
                print(' ', end="")
            else:
                print(i, end="")
            space = space - 1
        print('\n', end="")

if __name__ == "__main__":
    main()