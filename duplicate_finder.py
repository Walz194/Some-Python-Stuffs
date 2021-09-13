import pdb
some_list = ['a','b','c','b','d','m','n','n']

# Duplicate Finder
def dup_finder(listy):
    temp_list = []
    dup_list = []
    pdb.set_trace()
    for i in range(0, len(listy)):
        if(listy[i] in temp_list):
            dup_list.append(listy[i])
        else:
            temp_list.append(listy[i])
                             
    return 'The duplcated elements are: '+ ','.join(dup_list)


dup_finder(some_list)
