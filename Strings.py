fruit = 'banana'
letter = fruit[0]
print(letter)
x = 2
w = fruit[x - 1]
print(w)

#how long the string is

print('theres ',len(fruit))

#loop strings

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#for loop
for letterFruit in fruit:
    print(letterFruit)

#count strings
word = 'banana'
count = 0
for letterbanana in word:
    if letterbanana == 'a':
        count = count + 1
print('theres ',count, 'letters', letterbanana)
