import sys

def main():
    firstNumber, secondNumber = get_numbers()
    print(f"Please think of a number between {firstNumber} and {secondNumber}!")
    correctGuess = get_guess(firstNumber,secondNumber)
    print(f"\nGame over. Your secret number was: {correctGuess:.0f}")

# Get first and second number
def get_numbers():
    while True:
        try:
            firstNumber = int(input("Input first number: "))
            secondNumber = int(input("Input second number: "))
            if(firstNumber > secondNumber):
                print("First number cannot be higher than second number")
                continue
            break
        except ValueError:
            print("Input must be a number")
            pass
        except KeyboardInterrupt:
            sys.exit()
    return firstNumber,secondNumber

# Binary Search
def get_guess(low,high):
    guess = (low+high)/2
    while(True):
        try:
            print(f"\nIs your secret number {guess:.0f}?")
            print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
            indicator = str(input()).lower()
            if(indicator != 'h' and indicator != 'l' and indicator != 'c'):
                print("Input must h, l, or c")
                continue
            if(indicator == 'h'):
                high = guess
                guess = (low+high)/2
            elif(indicator == 'l'):
                low = guess
                guess = (low+high)/2
            else:
                return guess
        except ValueError:
            print("Input must be a string")
            pass
        except KeyboardInterrupt:
            sys.exit()
    

if __name__ == "__main__":
    main()