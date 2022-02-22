#To find just the host email from this sentense we use this '@([^ ]*)', where '^' this means 'not' whatever is in from, '^ ' this means extract data but not exctrat no-blank space
#'*' means one or more times
#'@( )' is the mark of when the exctract data begins. Inside parantecers is when we put what we want to.

import re
lin = 'From stread.floreanopeles@uft.udb.to  stread.floreanopeles@asdfasdf.to stread.floreanopeles@uft.udb.to Sat Jan 45:51:11 2005'
y = re.findall('@([^ ]*)', lin)
print(y)

#Bellow we find just the previous one email
y = re.findall('^From .*@([^ ]*)', lin)
print(y)


#'\' is the prefix the define what we're looking for, like '\$' here we are looking for everything after the $ signal.
x = 'we are received $500.00 for pie'
y = re.findall('\$[0-9.]+', x)
print(y)
