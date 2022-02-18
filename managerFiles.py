#first of all we need to open the file
handle = open('for.py')
#this means for each line in the file
count = 0
for cheese in handle:
    count = count + 1
    print(cheese)
print('Existem ', count, ' linhas nesse código')
#\n means that python go to the newline
stuff = 'hello\nWorld'
stuff
'Hello\nWorld!'
print(stuff)
