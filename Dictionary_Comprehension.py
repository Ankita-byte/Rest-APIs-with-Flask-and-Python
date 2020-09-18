users=[
    (0,'Bob','password'),
    (1,'Rolf','bob123'),
    (2,'Jose','longp'),
    (3,'user','1234')
]

username_mapping={user[1]:user for user in users}
#print(username_mapping)

username_input=input('enter the username')
password_input=input('enter the password')

_,user,password=username_mapping[username_input]

if password_input==password:
    print('Details are correct')

else:
    print('Details are incorrect')