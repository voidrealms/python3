#Decorators

#Everything in python is an object
#That means functions can be used as objects
#So we can do some really cool things
#A decorator takes in a function, adds some functionality and returns it. 

#Basic decorator
#In this example we will change the execution order

def test_decorator(func):
    print('before')
    func()
    print('after')
    
@test_decorator
def do_stuff():
    print('Doing stuff')

#Real decorator
#In this example we will change the functionality
#@makeBold is equal to
#f = makeBold(printName)
#f()
def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner #Return the inner function

@makeBold
def printName():
    print('Bryan Cairns')

printName()

#Decorator with params
#Notice this has a defined number of params
def numcheck(func):
    def checkInt(o):
        if isinstance(o,int):
            if o == 0:
                print('Can not divide by zero')
                return False
            return True
        print(f'{o} is not a number')
        return False
    
    def inner(x,y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x,y)
    return inner

@numcheck
def divide(a,b):
    print(a / b)

divide(100,3)
divide(100,0)
divide(100,'cat')

#Decorator with unknown number of params
#We want a decorator that can pass params and handle anything
#We also want to chain them together
# *args, **kwargs to the rescue

def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        func(*args,**kwargs)
        print('~'*20)
    return inner

def list_items(func):
    def inner(*args, **kwargs):
        func(*args,**kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'arg={x}')
        for k,v in kwargs.items():
            print(f'key={k}, value={v}')
    return inner

@outline
@list_items
def display(msg):
    print(msg)

display('hello world')

@outline
@list_items
def birthday(name='',age=0):
    print(f'Happy birthday {name} you are {age} years old')

birthday(name='Bryan',age=46)