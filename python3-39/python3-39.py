#Map
#Looping without a loop
#Maps function calls to a collection of items
#map(func, iterables)

#Basic usage - Count len
people = ['Matt', 'Bryan', 'Tammy','Markus']

#old way
counts = []
for x in people:
    counts.append(len(x))
print(f'Old way: {counts}')

#modern way
print(f'Mapped: {list(map(len,people))}')

#More complex - Combine elements
#Notice different lens, we are also passing multiple args

firstnames = ('Apple','Choclate','Fudge','Pizza')
lastnames = ('Pie', 'Cake','Brownies')

def merg(a,b):
    return a + ' ' + b

x = map(merg,firstnames,lastnames)
print(x)
print(list(x))

#Multiple functions - Combine functions
#Call multiple functions in one map call

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def doall(func,num):
    return func(num[0],num[1])

f = (add,subtract,multiply,divide)
v = [[5,3]]
n = list(v) * len(f)
print(f'f:{f}, n:{n}')

m = map(doall,f,n)
print(list(m))
