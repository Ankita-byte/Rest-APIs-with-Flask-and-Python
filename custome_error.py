class Toomanypagesreaderror(Exception):
    pass

class Book:
    def __init__(self,name,page_count):
        self.name=name 
        self.page_count=page_count
        self.pages_read=0

    def __repr__(self):
        return (f'Book {self.name},{self.pages} read among {self.page_count}' )

    def read(self,pages):
        if self.pages_read+pages>self.page_count:
            raise Toomanypagesreaderror('You are trying to read pages more than book')


        self.pages_read+=pages
        print(f'You have read {self.pages_read} out of {self.page_count}')

obj=Book("Python",900)
obj.read(12)
obj.read(35)
obj.read(900)