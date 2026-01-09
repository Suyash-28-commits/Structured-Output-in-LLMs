from typing import TypedDict

#Example of typed dictionary
#class Person inherits typedDict Class
class Person(TypedDict):
    name : str
    age : int 

#Typed dictionary
new_person : Person = {'name':'Suyash','age':20}
print(new_person)

#At runtime there is no validation of data type, so if data type changes of any value corresponding to a key
#It will not raise any exception
person: Person = {'name':'Nitish','age':'50'}
print(person)