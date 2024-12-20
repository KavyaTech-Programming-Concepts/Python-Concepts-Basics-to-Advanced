        ##python inheritance
## allow us to define a class that inherits all the methods and properties from another class.
### euta classs ko sabai methods ra properites arko class ma inherit hunii

##parent class and child classs


##creating a parent class is as easy as creating a simple class , a simple class can be called as parent class or base class itself

### while creating a child class, we use () and inside it (), we mentiion the name of parent class we want the methods to inherit from
##for example;
    # class Parent:   ##it is called parent class
    #     pass

    # class Child(Parent):        ##it is called child class
    #     pass
###example
class Person:
    def __init__(self,fname):
        self.fname=fname
    def print_name(self):
        print(self.fname)

class Student(Person):
    pass

x= Person("raj")
x.print_name()


## it can also override, child class can also override parent class if explicitedly defined 
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
class Person:
    def __init__(self,fname):
        self.fname=fname

    def print_name(self):
        print(f'name from person class is {self.fname}')

class Student(Person):
    def __init__(self,fname):
        self.fname=fname
    
    def print_name(self):
        print(f'name from student class is {self.fname}')
y=Person("KB sir")
y.print_name()
x= Student("raj")
x.print_name()


####    we use super().init() function to make the child calss inehrit all the methods and properties of its parent
## using super() function haleps to maintain multiple subclasses 
## it inherits updates from the parents automatically


        ##example from ChatGpt
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary must be non-negative")
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Directly assigns attributes, bypassing validation
        self.name = name
        self.salary = salary
        self.department = department

# This will cause issues because validation is skipped
manager = Manager("Raj Shrestha", -5000, "Mathematics")  # No error here!
