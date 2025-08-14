import json
l=[1,2,3,4,5]
a=json.dumps(l)
print(a)
print(type(a))

print('----------')
b=json.loads(a)
print(b)
print(type(b))