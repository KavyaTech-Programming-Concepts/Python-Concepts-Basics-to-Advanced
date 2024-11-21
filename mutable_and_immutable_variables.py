                                ##mutuable variable
# mutuable variables are such variable which value can be changed in place without creating new objects in memory
# it modifies the already existing object 
# examples:
# list
# dictionaries
# set 

# list
fruits=[ "apple" , "banana" , "orange" ]
print(fruits)    
print(id(fruits))
print(type(fruits))         

fruits.append("mango")      #it adds mango in the list
print(fruits)               
print(type(fruits))
print(id(fruits))           #same memory addreess as before list appends




                              ###immutabale variable 
#an object is immutable only if its value cannt be changes after it is created                              
# Examples of Immutable Types:
# Numbers: int, float, complex
# Strings: str
# Tuples: tuple
# Frozen Sets: frozenset
# Booleans: bool

z=10 #we cannnot change the value of z
print(z)
print(id(z))
##but we can do following things
z=z+10
print(id(z))   # we can see that the id of this z and previous z is not same because this is immutable variables