
#Create a program that calculates the area of a square while taking into account these test cases:
#If the user inputs a negative number, print an error message
#If the user inputs a string, print an error message
#If the user inputs a positive number, print the area of the square

end = False

def area():
    global l
    l = float(l)
    area = l * l
    return area

while end == False:

    print("What is the length of the square?")
    l = input()

    try:
        x = float(l)
    except ValueError:
        print("You entered text. Please enter a positive number.")
    else:
        if float(l) < 0:
            print("You entered a negative number. Please enter a positive number.")
        else:
            print("The area of the square is:", area())
            end = True
