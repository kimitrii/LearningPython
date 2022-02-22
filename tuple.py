#tuple can't be modifed, when you try it, the code returns a traceback
#x = (2,1,5,6)
#x[3] = 5

#you can't add/edit/delete values from a tuple

(francisco, raimundo) = (4, 'fred')
print(raimundo)
print(francisco)

d = dict()
d['fdd'] = 45
d['lff'] = 24

for (k,v) in d.items():
    print(k, v)
