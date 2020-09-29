class ClassTest:
    def instance_method(self):
        print(f'Called instance method of {self}')

    @classmethod
    def class_method(cls):#cls is class itself
        print(f'Called class method of {cls}')

    @staticmethod
    def static_method():#Don't need to pass anything
        print(f'Called static method')

test=ClassTest()
test.instance_method()
#ClassTest.instance_method(test)

#For class method you don't need an instance because it's a class method
ClassTest.class_method()#If we don't pass anything then python will pass ClassTest
#test.class_method()----It works

ClassTest.static_method()#Don't need object for calling this method
#test.static_method()-----It works


class Book:
    TYPES=('hardcover','paperback')

    def __init__(self,name,type,weight):
        self.name=name
        self.type=type
        self.weight=weight

    def __repr__(self):
        return f'{self.name} have type {self.type} and {self.weight}'

    @classmethod
    def hardcover(cls,name,page_weight):
        return Book(name,Book.TYPES[0],page_weight+100)
    
    @classmethod
    def paperback(cls,name,page_weight):
        return Book(name,Book.TYPES[0],page_weight)

hard=Book.hardcover('Harry',500)
print(hard)
light=Book.paperback('You can win',300)
print(light)