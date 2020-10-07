a=5
b=2

try:
    print('resourse open')
    print(a/b)
    print('Hi Ankita')

except ZeroDivisionError as e:
    print('Hey,You can not divide number by zero',e)

else:
    print('Hurray,No error')

finally:
    print('Resource close')

print('Bye')