#Inheritance-->deriving subclass from superclass
#**TYPES:
#---------
##1.Single
##2.multilevel
##3.multiple
##4.hierarichal
##5.hybrid
####################
#SINGLE INHERITANCE:
#----------------------

##example 1:
"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def dispaly(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per):
        print("subclass")
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per)
std1=Student(123,97)
#output:subclass
#>>> std1.rollno##we need to call display method with object name
#123
#>>> std1.per
#97"""


##example 2:
"""
class Personal:#super class
    def __init__(self,name,adhar,pan):
        print("super class")
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def dispaly(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    pass
std1=Student("raj","123456","dhfbj")
#output:superclass
##>>> std1.name
##'raj'
##>>> std1.pan
##'dhfbj'"""

##example 3
"""
class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def dispaly(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per)
std1=Student(123,97,"raj","12345","hdfjd")
#output:
##>>> std1.rollno
##123
##>>> std1.name
##AttributeError: 'Student' object has no attribute 'name'"""

##example 4
"""
class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def dispaly(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        super().__init__(name,adhar,pan)#-->using super() we can access super class arguments using subclass
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per)
std1=Student(123,97,"raj","12345","hdfjd")
#output:
##>>> std1.rollno
##123
##>>> std1.name
##'raj'"""

##example 5
#if we invoke display method with object name -->
#it will first search for whether the dispaly method is in subclass
#if not then it check if it is in super class
"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        super().__init__(name,adhar,pan)
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per)
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
##output:
#123 97
"""
################################
"""
class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        super().__init__(name,adhar,pan)
        self.rollno=rollno
        self.per=per
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
##output:
#raj 12345 hdfjd"""
###################################

##example 6:
"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        self.rollno=rollno
        self.per=per
        super().__init__(name,adhar,pan)
    @classmethod
    def display(cls):
        print("class method")
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
##output
#class method"""

#example 7: super().display()#-->display method in super class is invoked 
"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        self.rollno=rollno
        self.per=per
        super().__init__(name,adhar,pan)
    def display(self):
        super().display()#-->display method in super class is invoked
        print(self.rollno,self.per)
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
##output:
##raj 12345 hdfjd
##123 97"""

#example 8
"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        super().__init__(name,adhar,pan)
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per,self.name,self.adhar,self.pan)#-->works here
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
#output:
#123 97 raj 12345 hdfjd"""

#example
"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    college="AEC"#-->works
    def __init__(self,rollno,per,name,adhar,pan):
        
        super().__init__(name,adhar,pan)
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per,self.name,self.adhar,self.pan,self.college)
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
#output:
#123 97 raj 12345 hdfjd AEC"""

"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    college="AEC"
    def __init__(self,rollno,per,name,adhar,pan):
        super().__init__(name,adhar,pan)
        self.rollno=rollno
        self.per=per
        self.college="aditya"#---->works
    def display(self):
        print(self.rollno,self.per,self.name,self.adhar,self.pan,self.college)
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
#output:
#123 97 raj 12345 hdfjd aditya"""


"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
        self.college="aditya"
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    college="AEC"
    def __init__(self,rollno,per,name,adhar,pan):
        super().__init__(name,adhar,pan)#using super class college is updated
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per,self.name,self.adhar,self.pan,self.college)
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
#output:
#123 97 raj 12345 hdfjd aditya"""

"""class Personal:#super class
    college="aditya"#if aec not given in subclass the o/p: is aditya
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
class Student(Personal):
    college="AEC"#-->prints aec 
    def __init__(self,rollno,per,name,adhar,pan):
        super().__init__(name,adhar,pan)#using super class college is updated
        self.rollno=rollno
        self.per=per
    def display(self):
        print(self.rollno,self.per,self.name,self.adhar,self.pan,self.college)
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()
#output:
#123 97 raj 12345 hdfjd AEC
"""

##HIERARICHAL INHERITANCE-->more than 1 subclass is derived from super class
#--------------------------
"""
class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
        
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        self.rollno=rollno
        self.per=per
        super().__init__(name,adhar,pan)
    def display(self):
        print(self.rollno,self.per,self.name,self.adhar,self.pan)
        super().display()
        
class Employee(Personal):
    def __init__(self,empid,salary,dept,name,adhar,pan):
        self.empid=empid
        self.sal=salary
        self.dept=dept
    def display(self):
        print(self.empid,self.sal,self.dept)
        
        
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()

emp1=Employee(1,50000,"ECE","shiv",7384738,"dhedgh")
emp1.display()
#output:
##123 97 raj 12345 hdfjd
##raj 12345 hdfjd
##1 50000 ECE"""

#example 2

"""class Personal:#super class
    def __init__(self,name,adhar,pan):
        self.name=name
        self.adhar=adhar
        self.pan=pan
    def display(self):
        print(self.name,self.adhar,self.pan)
        
class Student(Personal):
    def __init__(self,rollno,per,name,adhar,pan):
        self.rollno=rollno
        self.per=per
        super().__init__(name,adhar,pan)
    def display(self):
        print(self.rollno,self.per,self.name,self.adhar,self.pan)
        super().display()
        
class Employee(Personal):
    def __init__(self,empid,salary,dept,name,adhar,pan):
        self.empid=empid
        self.sal=salary
        self.dept=dept
        super().__init__(name,adhar,pan)##to access super class variables
    def display(self):
        print(self.empid,self.sal,self.dept,self.name,self.adhar,self.pan)
        
        
std1=Student(123,97,"raj","12345","hdfjd")
std1.display()

emp1=Employee(1,50000,"ECE","shiv",7384738,"dhedgh")
emp1.display()
#output:
##123 97 raj 12345 hdfjd
##raj 12345 hdfjd
##1 50000 ECE shiv 7384738 dhedgh"""


########
#Multilevel inheritance-->more than 1 level
#-----------------------
"""class Telephone:
    def __init__(self):
        print("calls")
class Mobile(Telephone):
    def __init__(self):
        print("Messages,basic games")
class SmartMobile(Mobile):
    def __init__(self):
        print("adv games,internet,movies")
sm1=SmartMobile()
#output:adv games,internet,movies"""

#######
"""class Telephone:
    def __init__(self):
        print("calls")
class Mobile(Telephone):
    def __init__(self):
        super().__init__()
        print("Messages,basic games")
class SmartMobile(Mobile):
    def __init__(self):
        super().__init__()
        print("adv games,internet,movies")
sm1=SmartMobile()
#output:
##calls
##Messages,basic games
##adv games,internet,movies"""


#if constructer is not there in subclass then it's going to check in parent classes
"""class Telephone:
    def __init__(self):
        print("calls")
class Mobile(Telephone):
    def __init__(self):
        super().__init__()
        print("Messages,basic games")
class SmartMobile(Mobile):
        pass
sm1=SmartMobile()
#output:
##calls
##Messages,basic games"""

##
#MULTIPLE INHERITANCE: ONE SUBCLASS IS INHERITING THE PROPERTIES OF MORE SUPERCLASSES
#----------------------
"""class Result:
    def __init__(self,name,players,score,marks1,marks2):
        self.sem1=marks1
        self.sem2=marks2
        super().__init__(name,players,score)#-->used to access the super class which is having name,players,score as arguments
    def display(self):
        print(self.sem1,self.sem2)
        super().display()#-->used to enter into display method of Sports superclass
class Sports:
    def __init__(self,name,players,score):
        self.name=name
        self.players=players
        self.score=score
    def display(self):
        print(self.name,self.players,self.score)
class Personal(Result,Sports):
    pass
p1=Personal("cricket",11,2500,92,98)
p1.display()
#output:
##92 98
##cricket 11 2500
"""
