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

#read files as a series of characters
stringsFile = open('Strings.py')
inp = stringsFile.read()
print('theres ',len(inp), ' characters')

#searching for something in files
camera = open('first.py')
for expecificWorld in camera:
    #rstrip() clen the empyt lines in return
    expecificWorld = expecificWorld.strip()
    if expecificWorld.startswith('n'):
        print(expecificWorld)

#if file don't exist
fname = open('adfasdfafs.py')
try:
    fname = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()#quit() makes the code ends without traceback
