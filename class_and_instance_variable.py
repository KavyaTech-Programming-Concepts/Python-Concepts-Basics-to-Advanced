###in python understand about variables can be crucial for oop conceps
##variables in classes are either defined in class varibales or instance varibales

            ##class variables
# they are defined at the class level and outside any methods.
# therefore it shares the same value accross the program unless defined explicitly
##for example in "oop" concept on previous file
# class Department:
#      hod="rabindra kayastha"            # 'hod ' is called the class variables



            ##instance varibales
#unlike in class variable, instance variables are unqiue in every instances of class
#these are defined within __init__. method
#each object maintains its own copy of instance variables, independent of the other objects
class Department:
    hod="rabindra kayastha"            # 'hod ' is called the class variables

    def __init__(self, name):
        self.name = name

t1=Department('raj sir')
print(t1.name)
