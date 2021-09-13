num = int(input("Enter a number between 1 and 12: "))
if num > 12 or num < 1:
    print("Can't you read ni ?!!!")
else:
    i = 0
    while(i <= 12):
        print(num, "x", i, "=", num*i)
        i += 1
