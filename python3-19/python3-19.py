#Functions and arguments

#Function in an argument
def test(name, age, pet):
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'pet = {pet}')

def getData():
    return dict(name='Bryan', age=46, pet='Cat')

d = getData()
test(d['name'],d['age'],d['pet'])

test(**getData())

#Function as an argument
def funky(kittens):
    d = kittens()
    print(f'd = {d}')
    print(f'Name: {d["name"]}')
    print(f'Age: {d["age"]}')
    print(f'Pet: {d["pet"]}')

funky(getData) #notice we are not calling the function, just passing it





