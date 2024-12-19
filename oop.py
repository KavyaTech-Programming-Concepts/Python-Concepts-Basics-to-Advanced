#####ref:from geeksforgeeks.org
#Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and 
# scalable applications. By understanding the core OOP principles (classes, objects, inheritance, encapsulation, polymorphism, and abstraction), programmers can
# leverage the full potential of Python OOP capabilities to design elegant and efficient solutions to complex problems.
#OOPs Concepts in Python
            # Class in Python
            # Objects in Python
            # Polymorphism in Python
            # Encapsulation in Python
            # Inheritance in Python
            # Data Abstraction in Python

            ##python class
# class is a collection of objects and they are like the blueprint for creating objects
# classes are created by the keyword "class"
# attributes are the variables that belong to the class
# attributes are always public and can be accessed by using . operator
##creating a class
class Student:
    faculty="computational mathematics" ##"faculty is called the attribute of the class student"

## we use '__init__' method for the initialisation 
    def __init__ (self,name,roll):
        self.name= name   ##instance attribute
        self.roll = roll   ##instance attribute


        ####objectt
#an object is also an instance of the class and it holds its own data
##State: It is represented by the attributes and reflects the properties of an object.
# Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.


##object creating->> to create an object in python , it invloves to create a new instance of that class
std1=Student("raj",20)
print(std1.name)
std2=Student("shyam",19)
print(std2.roll)


##self
class Department:
    hod="rabindra kayastha"
    def __init__ (self, name,age):
        self.name=name
        self.age=age

    def teach(self,subject):
        print(f"{self.name} teaches {subject}")

t1=Department("kb sir", 39)
t1.teach("analysis")
print(Department.hod)