purse = dict()
purse['money'] = 12
purse['candy'] = 7
purse['issues'] = 2

print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 1
print(purse['candy'])

#other exemple of dictionaries
ttt = {'fruit':2, 'meat':8, 'cloves':4}
print(ttt)

#count the frequency of items
counts = dict()
names = ['csve','cwen','csve','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#'Get' method is equal 'if or else' from dictionaries.
#the code bellow works as the same as top
countP = dict()
nameP = ['csve','cwen','csve','zqian','cwen']
for namesP in nameP:
    countP[namesP] = countP.get(namesP,0) + 1
print(countP)
