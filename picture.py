picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for subl in picture:
    i = 0
    pic = []
    while i < len(subl):
        if(subl[i] == 0):
            pic.append(' ')
        else:
            pic.append('*')
        i+=1
    print(''.join(pic))
