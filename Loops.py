n = 5
while n > 0 :
    print(n)
    n = n - 1

#breaking a infinety loop

b = 5
while b > 0 :
    print(n)
    break
print('done')

#cantinue make returns to the top of the function

b = 5
while b > 0 : #return of 'continue'
    print(n)
    #'continue' this made returns to top
    print('brake')
    break
print('done')

a = 0
while True:
    if a == 3:
        break
    print(a)
    a = a + 1
