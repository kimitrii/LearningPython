fruit = "banana"
print(fruit[1])

#other kind of lists
for i in [5,4,3,2,1]:
    print(i)

#len say who many itens are in string
cubecall = [1,2,3,5,8,7]
print('Theres ',len(cubecall), 'items on string')

#calculating lists

a = [1,2,3]
b = [4,5,6]
print(a + b)
print(b[2:])

#adding stuffs on lists
stuff = list()
stuff.append('book')
stuff.append('88')
print(stuff)
stuff.append('cloves')
print(stuff)

#"in" operator check if something is on lists, returns True or False
88 in stuff
20 not in stuff

#ordering the items from a list order by abc
stuff.sort()
print(stuff)
print(stuff[1])

#functions to manipulate the lists
print(len(stuff))
print(max(stuff))
print(min(stuff))
print(sum(stuff))
