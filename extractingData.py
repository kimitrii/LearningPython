import re
x = 'My 2 favorites movies are 19 and 48'
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[r]+', x)
print(y)

#We can find a especific value until some point like ":"
import re
a = 'From: Using the: character'
b = re.findall('^F.+:', a)
print(b)

#we can especify an especific value with no-blank characters. the '@' is what we're looking for
email = 'From steph.marqued@uct.ac.za Sat Jan 5 09:14:16 2008'
final = re.findall('\S+@\S+', email)
print(final)

#other way to do the same thing
final = re.findall('^From (\S+@\S+)', email)
print(final)

#getting just the email from this frase bellow. Especify the '@' surrownd by blank space '\S'
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
