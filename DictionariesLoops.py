counts = dict()
print('enter a line of text!...')
line = input('')
words = line.split()

print('Words:',words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) +1
print('Counts: ', counts)

#geting the keys and values from a dictionarie
jjj = {'chuck':1, 'fred':42, 'jan':100}
print(list(jjj))

#get the keys only
print(jjj.keys())

#get values only
print(jjj.values())

#get the items
print(jjj.items())

#we can loop the keys and values of a list
for aaa,bbb in jjj.items():
    print(aaa,bbb)
