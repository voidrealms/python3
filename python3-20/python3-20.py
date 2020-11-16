#Global

#Global keyword which allows code to modify a variable 
#outside of the current scope. 
x = 1
def test():
   # x = 6
    print(x)


test()
print(x)

#Global variable
counter = 0

#Scope issues
def count(max):
    #Without "global", python is confused
    global counter
    counter += 1
    if counter >= max: return False
    return True

#Global keyword in action
limit = 5
for x in range(limit):
    b = count(limit)
    print(counter)

print('Done')



