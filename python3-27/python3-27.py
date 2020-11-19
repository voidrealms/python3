#Imports

#Lets make our code usable to other scripts
#This allows us to structure our code and simplify things
#We are really just scratching the surface of the import system

#Create the file
#Go ahead and look at mycode.py

#Import as
import mycode as person

#Scope issues
global name #can shove it into the global scope but we should not
#print(name) #not in the same scope
print(person.name) #Each file can and should use its own scope

#Test the code
person.name = 'Bryan'
person.greet()
person.toFile('test.txt')

person.name = 'Tammy'
person.greet()

person.fromFile('test.txt')
person.greet()




