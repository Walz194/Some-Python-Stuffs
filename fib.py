import random


def fibbonaci(interval):  # 0 1
    fib = []
    count = 0
    acc = 0
    while count <= interval:
        if count == 0:
            fib.append(acc)
            count += 1
        elif count == 1:
            acc = 1
            fib.append(acc)
            count += 1
        else:
            acc = fib[count-1] + fib[count-2]
            fib.append(acc)
            count += 1
    return fib


def fibbonaci2(interval):
    a = 0
    b = 1
    for i in range(interval+1):
        yield a
        temp = a
        a = b
        b = temp + b


# wale = fibbonaci2(20)
# print(next(wale))
# print(next(wale))
# print(next(wale))
# print(next(wale))

def num_pair_generator(num):
    for i in range(num):
        yield (i, i**2)


# wale = num_pair_generator(20)
# print(next(wale))
# print(next(wale))
# print(next(wale))
# print(next(wale))


def choose_walz_gal():
    count = 0
    choices = []
    contestants = ['Rashida', 'Kamila', 'Hafsat', 'Sameerah', 'Amina']
    while count < 1000:
        choices.append(random.choice(contestants))
        count += 1
    for i in contestants:
        print(f'{i} was suggested by the computer {choices.count(i)} time(s)')


choose_walz_gal()
