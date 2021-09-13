# wale = open('./webapp/wale.txt')
# print(wale.readlines())
# print(wale.readlines())
# print(wale.readlines())
# wale.close()  # after opening a file, we have to close it

# With a 'with' statement, it not necessary to close() the file
# by default, the mode is 'r' which stands for read, if it is not specified, it is 'r' by default
with open('./webapp/wale.txt', mode='r') as new_wale:
    print(new_wale.read())

# To write, you specify it with 'w', read and write is specified with 'r+'

with open('./webapp/wale.txt', mode='r+') as new_wale:
    # When the write method is called, the cursor is set to zero, so if we write another text, the first set of characters will be overridden

    # new_wale.write('I am going on here')
    new_wale.write('Ippo')

# To prevent that, we can use the append tag 'a'
with open('./webapp/wale.txt', mode='a') as another_wale:
    another_wale.write('IS it working?')
