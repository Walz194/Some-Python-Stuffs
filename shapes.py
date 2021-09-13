proceed = True

while proceed == True:
    print("1) Square \n2) Triangle")
    choice = int(input("Enter a number: "))
    if choice == 1:
        print("Ooohoo (Land of Wano sound)...you have chosen a square\n")
        length = float(input("Enter the length of one of the sides of the square, I want to find the area: "))
        print("The area of the square is: ",length**2)
    elif choice == 2:
        print("Duh..you chose a triangle\n")
        height = float(input("How high is the triangle? : "))
        base = float(input("How wide is the base? : "))
        print("The area of your triangle is: ", (1/2) * base * height)
    else:
        print("You've gotta learn to follow simple instructions B**CH")
    response = input('Would you like to try again? [Y/N]')
    proceed = False if response == 'N' else True
