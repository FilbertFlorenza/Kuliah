while(True):
    number = int(input("Input number: "))
    if(number >=1 and number <= 50):
        break
    else:
        print("Input valid number")

text = ""
if(number % 3 == 0):
    text += "Papa"
if(number %5 == 0):
    text += "Mama"

if(text != ""):
    print(text)
else:
    print(number)