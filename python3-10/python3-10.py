#Dictionary {k:v , k:v}
#Indexed by keys, which can be any immutable type

#Create a dictionary
d = {'pet':'dog','age':5,'name':'spot'}
print(d)
d = dict(pet='dog',age=5,name='spot')
print(d)

#Get keys and values
print(f'Items: {d.items()}')
print(f'Keys: {d.keys()}')
print(f'Values: {d.values()}')

#Getting a value from the key
print(f'Name: {d["name"]}')
#print(f'Test: {d["bla"]}') #Will throw an error if the key is not found

#Add an item
d['trick'] = 'sit'
print(d)
d['trick'] = 'roll over'
print(d)

#Removing an item
del d['trick']
print(d)

#Testing for existence (covered in a future video)
if 'name' in d:
    print(d['name'])

#Looping (covered in a future video)
for key in d.keys():
    print(f'{key} = {d[key]}')


