#Simple Program
student={'name':'Rolf','grades':(89,90,93,78,90)}

def average(sequence):
    return sum(sequence)/len(sequence)

print(average(student['grades']))

#Object Oriented Program
#Example 1
class Student():
    def __init__(self):#__init__() method  is called automatically
        self.name='Rolf'
        self.grades=(89,90,93,78,90)

    def average1(self):#You can use anything instead of self******this parameter means object
        return sum(self.grades)/len(self.grades)

student=Student()#Create the object in python
#print(student.name)
#print(student.grades)
#print(Student.average1(student))---Can use this but not recommended
print(student.average1())


#Example 2
class Student2():
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def average2(self):
        return sum(self.grades)/len(self.grades)

student2=Student2('Ankita',(90,89,95,96,99))
print(student2.average2())