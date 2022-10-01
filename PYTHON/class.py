##class:is a collection of member variables and memeber functions(methods)
##object:instance of a class
##constructor:default method

#Example 1:
"""class Student:
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.name,self.rollno,self.per)

std1=Student("PADMA","123",65)
std2=Student("Pavan","456",12)
std1.display()
std2.display()
#output:PADMA 123 65
       #Pavan 456 12"""

#Example 2:
"""class Student:
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.name,self.rollno,self.per)

std1=Student("PADMA","123",65)
std1.display()

#output: PADMA 123 65"""

#Example-->For class variable it  call with <class_name.>
"""class Student:
    college="ADITYA"
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.name,self.rollno,self.per,Student.college)

std1=Student("PADMA","123",65)
std1.display()
#output: PADMA 123 65 ADITYA"""


#Example-->For class variable it  call with <class_name.> even if we call with self. it gives same result
#because any variable with object reference going to check first is there any instance variable with that name and then check
#is there any class variable with that name. If it not either one then it gives an error
"""class Student:
    college="ADITYA"
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.name,self.rollno,self.per,self.college)#if we write only college-->error

std1=Student("PADMA","123",65)
std1.display()
#output: PADMA 123 65 ADITYA"""

#Example
"""class Student:
    college="ADITYA"
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
        self.college="AEC"
    def display(self):
        print(self.name,self.rollno,self.per,self.college)#if we write only Student.college-->Aditya

std1=Student("PADMA","123",65)
std1.display()
#output: PADMA 123 65 AEC"""


#Example
"""class Student:
    college="ADITYA"
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
        self.coll="AEC"
    def display(self):
        print(self.name,self.rollno,self.per,Student.coll)

std1=Student("PADMA","123",65)
std1.display()
#output: ERROR"""

#Example
"""class Student:
    college="ADITYA"
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
        self.coll="AEC"
    def display(self):
        print(self.name,self.rollno,self.per,Student.coll)

std1=Student("PADMA","123",65)
std1.display()
#output: ERROR"""

#We can access class variable with object if that name is not used for instance variable
"""class Student:
    college="ADITYA"
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
        self.coll="AEC"#college and coll are different
    def display(self):
        print(self.name,self.rollno,self.per,Student.coll)

std1=Student("PADMA","123",65)
print(std1.college)
#output: ADITYA"""

#first it check that if that name is instance variable and then check for class variable
"""class Student:
    college="ADITYA"#class variable or static variables
    def __init__(self,n,rollno,per):#constructor is a instance method
        self.name=n
        self.rollno=rollno
        self.per=per
        self.college="AEC"
    def display(self):#instance method
        print(self.name,self.rollno,self.per,Student.coll)
std1=Student("PADMA","123",65)
print(std1.college)
#output:AEC"""

##Methods
#1.Instance-->accessing with objects-->we can access both class variables and instance variables
#2.class-->@classmethod
#3.static

#class methods
"""class Student:
    college="ADITYA"#class variable or static variables
    def __init__(self,n,rollno,per):#constructor is a instance method
        self.name=n
        self.rollno=rollno
        self.per=per
        self.college="AEC"
    def display(self):#instance method
        print(self.name,self.rollno,self.per,Student.coll)
    @classmethod
    def class_method(cls):#passing class name to cls
        print("class method")
std1=Student("PADMA","123",65)
Student.class_method()
std1.class_method()#-->even call with object..its class only is passed to cls
#output:class method
#       class method"""

#we can access only class variables but not instance variables from class methods
"""class Student:
    college="ADITYA"#
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
        self.college="AEC"
    def display(self):#instance method
        print(self.name,self.rollno,self.per,Student.coll)
    @classmethod
    def class_method(cls):
        print(cls.per)#Student.per-->nothing here so error
        print(cls.college)#Student.college-->ADITYA
std1=Student("PADMA","123",65)
Student.class_method()
std1.class_method()"""

#static methods can call with either class name or object name
class Student:
    college="ADITYA"#
    def __init__(self,n,rollno,per):
        self.name=n
        self.rollno=rollno
        self.per=per
        self.college="AEC"
    def display(self):#instance method
        print(self.name,self.rollno,self.per,Student.coll)
    @staticmethod
    def num(n,a):
        print(n,a)
std1=Student("PADMA","123",65)
Student.num(100,20)#output:100,20
std1.num(100,20)#output:





