import sys

def main():
    firstNumber, secondNumber = get_numbers()
    print(f"Please think of a number between {firstNumber} and {secondNumber}!")
    correctGuess = get_guess(firstNumber,secondNumber)
    print(f"\nGame over. Your secret number was: {correctGuess:.0f}")

# Get first and second number
def get_numbers():
    '''
        Function to get number range, looping if the user input invalid number

        Input:
            string: the string to be the user's response based on the guess number. Accept: h, l, or c
        
        Returns:
            firstNumber (int): number to be the floor of the number range
            secondNumber (int) : number to tbe ceiling of the number range
    '''
    while True:
        try:
            firstNumber = int(input("Input first number: "))
            secondNumber = int(input("Input second number: "))
            # First number cannot be higher than second number
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

def get_guess(low,high):
    '''
        Function to get user's secret number, looping until the function get the correct number

        Parameters:
            low (int): Number to be the floor of the number range
            high (int): Number to be the ceiling of the number range
        
        Input:
            string: the string to be the user's response based on the guess number. Accept: h, l, or c
        
        Returns:
            guess (float): The correct number guessed by the function
    '''
    # First guess, get middle number between low and high
    guess = (low+high)/2
    # Loop until we get the correct guess
    while(True):
        try:
            print(f"\nIs your secret number {guess:.0f}?")
            print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
            indicator = str(input()).lower()

            if(indicator != 'h' and indicator != 'l' and indicator != 'c'):
                raise ValueError
                continue
            # If guess is too high, set high to guess, then middle number again
            if(indicator == 'h'):
                high = guess
                guess = (low+high)/2
            # If guess is too high, set low to guess, then middle number again
            elif(indicator == 'l'):
                low = guess
                guess = (low+high)/2
            # If guess correct, return guess number while breaking the loop
            else:
                return guess
        except ValueError:
            print("Input must be a h, l, or c")
            pass
        except KeyboardInterrupt:
            sys.exit()
    

if __name__ == "__main__":
    main()