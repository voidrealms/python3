#Lists []

#Create a list - remember the square brackets
x = ['Bryan','Cairns',46] #Can mix data types
print(f'List: {x}') #Print the list
print(f'Len: {len(x)}') #Print the len

#Index and positioning - zero based
print(f'Zero: {x[0]}') #First item is ZERO
print(f'Slice: {x[1:2]}') #Slice the list

#Adding Items - append, insert
x.append('Pizza') #Adds at the end
x.append('Beer') #Adds at the end
x.insert(1,'Cats') #Adds at a specific position
print(f'List: {x}')

#Removing items - remove, pop, delete
x.remove('Cats') #Remove an item
print(f'List: {x}')

i = x.index('Pizza') #Will raise an error if not found
print(f'Food: {x.pop(i)}') #Remove and return the item
print(f'List: {x}')

i = x.index('Beer') #Will raise an error if not found
del x[i] #Delete a specfic item without returning it
print(f'List: {x}')

#Extending - Adds elements from another list
y = ['Cats', 'Dogs', 'Birds']
x.extend(y)
print(f'Extend: {x}')

#Sort - sort, reverse
x.remove(46)
x.sort() #Will throw an error if there mixed types
print(f'Sort: {x}')
x.reverse()
print(f'Reverse: {x}')

#Copy
y = x.copy() #Copies the elements into a new list
y.reverse()
y.append('Apples')
print(f'Original: {x}')
print(f'New: {y}')

#Delete the whole thing
del y
#print(y)

#Clear
x.clear()
print(f'Cleared: {x}')
print(f'Len: {len(x)}')

#Lists can contain other lists [[],[],[]]
x = []
y = [1,2,3]
z = ['Bryan','Cairns']
x.append(y)
x.insert(0,z)

print(f'List: {x}')
print(f'Len: {len(x)}')
print(f'0: {x[0][0]}')
print(f'1: {x[1][2]}')

#Changing items - positional
x = [1,2,3,4,5]
x[2] = 'TEST'
print(x)