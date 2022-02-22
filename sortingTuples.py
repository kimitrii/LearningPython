#'Sorted' is a function to organize the returns values
d = {'a':10, 'b':1, 'c':22}
for k, v in sorted(d.items()):
    print(k,v)

#we can reverse sorted items with the simple code bellow

c = {'a':10, 'b':1, 'c':22}
print(sorted([(k,v) for v,k in c.items()]))
