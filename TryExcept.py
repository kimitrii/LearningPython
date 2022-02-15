astr = 'hello blob'
#try is a command that try to do something, if it returns a error, it trigger the 'except' command
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)


# If interger
astr = input("type a number")
try:
    istr = int(astr)
except:
    istr = "it isn't a number"

print ('Second', istr)
