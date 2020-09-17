from functools import reduce
#Normal Function
def add(x,y):
    return x+y

print(add(5,4))

#Lambda Function
addition=lambda x,y : x+y
print(addition(3,7))

li=[2,3,5,6,7,8]

#map(func,seq) takes 2 arguments 1)a function 2)a sequence
square_all=list(map(lambda x: x**2,li))
print(square_all)


#filter(func,seq) ****Need to import functools for using reduce
fib = [0,1,1,2,3,5,8,13,21,34,55]
result=list(filter(lambda x : x%2,fib))
print(result)

#reduce(func,seq)
final=reduce(lambda x,y: x if x>y else y,li)
print(final)
