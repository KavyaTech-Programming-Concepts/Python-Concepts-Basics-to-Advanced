##a function in python is a block of codes that can be reused and used to perform specific type of tasks.
# there are many types of functions:
# 1.built-in functions
#     they are the pre-defined functions that are already built or defined
# 2. user-defined functions:
#     they are the functions that we create to perform specific tasks
def name(x):        ###def is the keyword we used to define a functions, name is the name of the fucntion and x is the parameter we passed to the fucntions

    print(f"name is {x}")

name("raj")         #function calling, "raj" is argument


###totsl number of arguments must be equal to total number of parameters

def name(fname,lname):
    print(fname +" " +lname)

name("raj", "shrestha")


def classes(stds):
    total=100
    avg_stds=total/stds
    return avg_stds
print(classes(10))


            #Arbitrary Arguments, *args
# sometimes we dont know how many arguments we are going to pass
# so we use * before the argument name, it takes the tuples of arguments 

def friends(*frns):
    print("my best friend name is :",frns[3])

friends("ram", "shyam", "hari","himanshu")