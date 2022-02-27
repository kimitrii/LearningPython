import json
data = '''{
    "name" : "Fred Mercure",
    "phone" : {
        "type" : "intl",
        "number" : "+1 545 878 65487"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('name:', info["name"])
print('Hide:', info["email"]["hide"])

#we can do a loop from the items of a Json file
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
for algumacoisa in info:
    print('Nome',algumacoisa['name'])
