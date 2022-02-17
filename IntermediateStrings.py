#it's like Str from php
s = "the life is great"
print(s[0:5])
print(s[2:])
print(s[:2])

#we can use 'in' to return true or false
fruit = 'banana'
if 'n' in fruit:
    print('theres n in ', fruit)

#lower function give a lower version of string

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print('HI THERE' .lower())
print('hi there'.upper())

#find something in a string, return the count of things
pos = greet.find('l')
print(pos)

#replace values
print(greet.replace('He','oia'))

#check if strings starts with something, return true or false
if s.startswith('the'):
    print('yes, it start')
