#The underscore
#Often ignored, multiple uses
#_Single
#__Double
#__Before
#After__
#__Both__

#Skipping
for _ in range(5):
    print('Hello')

#Test class
from person import *

#Before (Single)
#Internal use only, called a weak private
p = Person()
p.setName('Bryan')
print(f'Weak private {p._name}')
p._name = 'NOOOOOOO'
print(f'Weak private {p._name}')

#Before (Double)
#Internal use only, avoid conflict in subclass 
#and tells python to rewrite the name (Mangling)
p = Person()
p.work()
#p.__think()
#c = Child()
#c.testDouble()

#After (Any)
#Helps to avoid naming conflicts with key words
class_ = Person()
print(class_)

#Before and after
#Considered special to Python, like the init and main function
p = Person()
p.__call__()