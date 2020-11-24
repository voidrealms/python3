#Pickle
#dill

#Serializing objects
#Saving and loading objects and their states
#Python data types, and top level classes
#https://docs.python.org/3/library/pickle.html

import pickle

def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args,**kwargs)
        print('-'*20)
    return inner

#Simple class
class Cat:
    def __init__(self, name,age,info):
        self._name = name
        self._age = age
        self._info = info
    
    @outline
    def display(self,msg=''):
        print(msg)
        print(f'{self._name} is a {self._age} years old cat')
        for k,v in self._info.items():
            print(f'{k} = {v}')

othello = Cat('Othello', 15,dict(color='Black',weight=15,loves='eating'))
othello.display('Testing')

#Serialize
sc = pickle.dumps(othello)
print(sc)

with open('cat.txt', 'wb') as f:
    pickle.dump(othello,f)

#Deserialize
mycat = pickle.loads(sc)
print('from string')
mycat.display('from string')

with open('cat.txt', 'rb') as f:
    diskcat = pickle.load(f)
diskcat.display('from disk')

print(mycat)
print(diskcat)