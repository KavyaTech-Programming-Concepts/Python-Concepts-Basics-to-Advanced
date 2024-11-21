                #datatypes
#it is the type or kind of the value that an object can hold
#there are built-in datatypes and advanced types
 #built-in data types are
#   -int
#   -float
#   -str
#   -char
#   -bool

# we use """type""" to return the datatype of the given object

x=10
y=type(x)   #it returns int type
print(y)    
print(x)
print(id(x))   #it returns the memory address of x
print(id(y))    #it returns the memory address of datattype of x i.e y

x="raj"
print(type(x))  #it overwrites int data type into string

