#Filter function
#filter(fun, iterables)
#returns true if it matches the filter

#Sub range
import random
v = []
for x in range(10):
    v.append(random.randrange(100))
print(v)

def lower(value):
    if value < 50:
        return True
    else:
        return False

f = filter(lower,v)
print(f'Less than 50: {list(f)}')

#Filter types

class Animal:
    name = ''
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

animals = []
for x in range(10):
    name = 'Animal ' + str(x)
    if (x % 2) == 0:
        #Even number
        animals.append(Cat(name))
    else:
        #Odd Number
        animals.append(Dog(name))

print(animals)

for a in animals:
    print(f'Animal: {a.name}')

def cats(value):
    return isinstance(value,Cat)

def dogs(value):
    return isinstance(value,Dog)

for c in list(filter(cats,animals)):
    print(f'Cat: {c.name}')

for d in list(filter(dogs,animals)):
    print(f'Dog: {d.name}')