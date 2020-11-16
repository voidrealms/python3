#Walrus operator and global
#Added in Python 3.8 looks like :=

#Assign a variable from an expression
#Must have the right version!

#Common issues ( )
#y := len('hello') #not valid syntax
(y := len('hello')) #valid but not recomended
print(y)

people = ['Bryan','Tammy','Rango']
if n := len(people) <= 3: print(n)
if (n := len(people)) <= 3: print(n)

#Simple example
lines = []

def canAdd(max = 5):
    global lines #Allows us to ensure we are using the global variable
    if allowed := (count := len(lines)) < max:
        print(f'You can enter {max - count} more')
    return allowed

while canAdd():
    lines.append(l := input('Enter a line:'))

print(f'You entered: {lines}')
