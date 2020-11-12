#Functions in depth

#No Arguments
def test():
    print('Normal function')

print('\r\n------ No Arguments')
test()

#Positional and Keyword Arguments
def message(name,msg,age):
    print(f'Hello {name}, {msg}, you are {age} years old')

print('\r\n------ Positional and Keyword Arguments')
message('Bryan', 'good morning', 22) #positional
message('Bryan', 22, 'good morning') #positional (wrong order)
message(msg='Good morning', age=46, name='Bryan') #Keywords
message('Bryan', age=46, msg='Good morning') #Both


#Internal functions
def counter():
    def display(count = 0): #Function in a function
        print(f'Internal: {count}')
    for x in range(5): display(x)

print('\r\n------ Internal functions')
counter()

# *args - positional variable length arguments
def multiple(*args):
    z = 1
    for num in args:
        print(f'Num = {num}')
        z *= num
    print(f'Multiply: {z}')
print('\r\n------ *args')
multiple(2,3,1,4,5,6,8,2,4,5,6)

# **kwargs is used to pass a keyworded, variable length arguments
def profile(**person):
    print(person)
    def display(k):
        if k in person.keys(): print(f'{k} = {person[k]}')
    display('name')
    display('age')
    display('pet')
    display('pezzzzt')

print('\r\n------ **kwargs')
profile(name='Bryan', age=46)
profile(name='Bryan', age=46,pet='Cat')
profile(name='Bryan', age=46,pet='Cat',food='pizza')

#Lambda functions (anonymous functions)
print('\r\n------ Lambda')
#normal
def makesqft(width=0,height=0):
    return width * height
print(makesqft(width=10,height=8))
print(makesqft(15,8))

#lambda
#z = lambda x: x * y
sqft = lambda width=0,height=0: width * height
print(sqft(width=10,height=8))
print(sqft(15,8))
