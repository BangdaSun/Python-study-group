### OOP
"""
class syntax:
    
    class newClass(object):
        # initialization, like constructor
        # self like 'this' in java
        # in javascript, we use 'this' when define method in this form: obj.method = ...
        def __init__(self, *args)
            self.args = args
    
"""

class Person(object):
    def __init__(self, name, age, is_male):
        self.name = name
        self.age  = age
        self.is_male = is_male
    
    def printInfo(self):
        print('Name: ', self.name, 'Age: ', self.age, 'Male: ', self.is_male)
        
bangda = Person('bangda', 23, True)
print(bangda.name)

bangda.printInfo()

"""
inheritance syntax:
    
    class DerivedClass(FatherClass):    

"""

class Student(Person):
    def __init__(self, name, age, is_male, gpa):
        self.name = name
        self.age = age
        self.is_male = is_male
        self.gpa = gpa
    
    def getGPA(self):
        return self.gpa

class GraduateStudent(Student):
    def __init__(self):
        pass
    
bangda = Student('bangda', 23, True, 3.9)
bangda.printInfo()

jiahui = GraduateStudent()
jiahui.age = 22
jiahui.age
