class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):#Turn object into a string
       return f'{self.name} is {self.age} years old'

    def __repr__(self):#Usually used in python debugger
        return f'{self.name} is {self.age} years oldd'

bob=Person('Bob',35)
print(bob.__str__())#bob is an object


