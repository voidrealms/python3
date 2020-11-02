
#Basic String Operations
str = "Hello World, this is a string!"

print(len(str)) #Get the length
print(str * 3) #Repeat
print(str.replace('Hello', 'Hola')) #Replace
print(str.split(',')) #Split
print(str.startswith('H')) #Starts with
print(str.endswith('!')) #Ends with
print(str.upper())
print(str.lower())
print(str.capitalize())

#Slicing - or getting a sub string
print(str[0:5]) #Get the first 5 - zero based
print(str[6:]) #Get the 6th to the end
print(str[-7:]) #Get the last 7
print(str[6:11]) #Get the 6 to 11

#Indexs - the position of
l = ','
c = str.find(l) #-1 if not found
print(f'Find returned {c}')

i = str.index(l) #Will throw an error!
print(f'Find returned {i}')

#"Hello World, this is a string!"
x = str[:i]
print(x)


