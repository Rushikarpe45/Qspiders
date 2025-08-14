import pickle
l=[1,2,3,4,5]
a=pickle.dumps(l)
print(type(a))

print('-------------')

b=pickle.loads(a)
print(b)
print(type(b))