name = input('Enter your name: ')
name_list = list(name.lower())
print('Alright...Pig Latinization initiated!')
if name_list[0] not in ('a','e','i','o','u'):
    popped = name_list.pop(0)
    name_list.extend([popped,'ay'])
    print(''.join(name_list))
else:
    name_list.append('way')
    print(''.join(name_list))
    
