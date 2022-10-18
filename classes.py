# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#class
class User:
    #constuctor 
    def __init__(self,name,email,age):
        self.name =  name 
        self.email= email
        self.age = age

def greeting(self):
    return f'name is {self.name} and i am {self.age}'
#create an object
brad = User('brad ttraver','aarushi@gmail.com',20)

print(brad.name)

print(brad.greeting())
