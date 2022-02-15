astr = 'hello blob'
#try is a command that try to do something, if it returns a error, it trigger the 'except' command
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)


# If interger
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print ('Second', istr)
