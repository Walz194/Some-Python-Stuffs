num = 5

while num > 0:
    print('There are {0} green bottle{1} hanging on the wall\nThere are {0} green bottle{1} hanging on the wall'.format(
        num, 's' if num > 1 else ''))
    print('If 1 green bottle should accidentally fall', sep=', ')
    ans = int(input('How many green bottles will be hanging on the wall?: '))
    while ans != num-1:
        print('Try again!')
        ans = int(input('How many green bottles will be hanging on the wall?: '))
    num = ans
print('There are no more green bottles hanging on the wall')
