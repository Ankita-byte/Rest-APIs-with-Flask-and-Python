#Example1
def multiply(*args):
    print(args)
    print(type(args))
    total=1
    for value in args:
        total=total*value
    print(total)

multiply(1,2,3,5,4)

#Example2
def add(x,y):
    return x+y

l=[4,6]
print(add(*l))

#Example3
d={'x':1,'y':2}
print(add(**d))
