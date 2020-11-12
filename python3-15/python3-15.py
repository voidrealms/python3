#Intro to functions

#A function is a block of code which only runs when it is called. 
#You can pass data, known as parameters (or arguments), into a function. 
#A function can return data as a result.
#We will split this up into a few videos

#Note the difference between parameters and arguments: 
#Function parameters are the names listed in the function's definition. 
#Function arguments are the real values passed to the function. 
#Parameters are initialized to the values of the arguments supplied.

#Reads from the top down 
#def name( parameters ):
#   code
#   code

#Define a function
def test():
    print('This is a function')

#Define a function with parameters and return a value
def sqft(w,h):
    v = w * h
    return v

#Call a function
test()

#Call a function mutiple times
for x in range(4):
    test()

#Call a function with parameters
x = sqft(12,8)
print(f'The square footage is {x}')
