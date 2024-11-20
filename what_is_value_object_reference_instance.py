                    ###### value
# value refers to the actual data that has been stored in the given variable
# for ex: x=10, then 10 is the value of variable "x"

                    ###object
x=10  # it creates an int type object that is x and tht has been adssigned to variable x
print(type(x))  ##returns class 'int' because it is of int type
print(x.bit_length())
y=10

print(id(x))  #
print(id(y))   #both variables points toward same memory location bcause python reuses the same object for the integer


                    ##references and instances
# it is a connection between variable name and object it points to in memory
# when we assign value to variable, it points to an object in memory
#they are the fundamental for undersstanding how variables interact with objects in memory
x=[1,2,3]
y=x
y.append(4) 
print(x)   
print(y)
##->we get that the list of both x and y at the end of the putput is same because the refenrence of both x and y is same

                    #instances
#when you create an object , it is called instance of its types
# #ex:
#     a number is an instance of the type "int"
#     A string is an instance of the type "str".
#     A list is an instance of the type "list".
x=10  # "x" is an instance of the 'int"
x = 10  # `x` is an instance of the `int` type
y = [1, 2, 3]  # `y` is an instance of the `list` type
