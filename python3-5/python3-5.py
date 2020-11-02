#What are Strings - big topic so we will split this into multiple videos
for x in 'hello':
    print(f'{x} = {ord(x)}')

#How to make a string
first = "Bryan" #Can be double qoute
last = 'Cairns' #Can be single qoute
print(first + ' ' + last)
print(f'Hello my name is {first} {last}')#Tend to use formatted to avoid issues

hers = "Heather's"
print(hers)

#Under the hood - Unicode (UTF8) - https://www.w3schools.com/charsets/ref_html_utf8.asp
#A string is a sequence of one or more characters
s1 = chr(72)
s2 = chr(105)
print(s1 + s2)
print(chr(8710)) #Way beyond ascii!

#Escape Characters - start with a slash \
print(f'Hello{chr(13) + chr(10)}World')
print(f'Hello\r\nWorld')
strTest = "Hello\tWorld"
print(strTest)

hers = 'Heather\'s'
print(hers)

qoute = "Then he said \"hello\" to me"
print(qoute)

#Must format strings to avoid errors
name = "Bryan"
age = 46
#print(name + ' ' + age) Error!!!
print(f'My name is {name} I am {age} years old')
print("My name is %s, I am %i years old!" % (name, age))
