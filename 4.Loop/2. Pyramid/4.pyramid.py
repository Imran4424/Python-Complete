'''
Problem:
        1
        1 0 1
        1 0 1 0
        1 0 1 0 1

'''

for i in range(1, 6):
    for j in range(i):
        if(i % 2 == 0):
            print("0", end=' ')
        else:
            print("1", end=' ')

    print()
