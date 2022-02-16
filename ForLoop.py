for i in [5,8,9,3,5,7]:
    print(i)
print('done')


#exemple 2

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

#count the number of values

zork = 0
for stuffs in [5,7,5,8,9,7,2,4,8,6,7]:
    zork = zork + 1
print('são ', zork, ' coisas')

#hunting for values
for value in [5,8,9,10,20,84,3]:
    if value > 15:
        print('Large number is ', value)
print('end of code')


#hunting the smallest
smallNumber = None
for valueNumber in [8,5,8,52,4,8,1,2,6]:
    if smallNumber is None :
        smallNumber = valueNumber
    elif valueNumber < smallNumber :
        smallNumber = valueNumber
print('Smallest is ', smallNumber)
