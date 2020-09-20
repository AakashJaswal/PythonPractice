import json

str = 'False'.lower()
test = json.loads(str)
print(type(test))
print(test)