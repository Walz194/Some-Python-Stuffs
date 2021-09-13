name_num = input("Enter your name and the number of times to print it, seperate with space: ")
name = []
for i in range(len(name_num)):
    if name_num[i].isalpha() or name_num[i].isspace():
        name.append(name_num[i])

num = name_num.replace("".join(name),"")
for i in range(0, int(num)):
    print("".join(name))
