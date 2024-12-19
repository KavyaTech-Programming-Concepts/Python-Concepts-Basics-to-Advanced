#they are like the primitive function but it is the short form of the function,it uses the keyword "lambda"
## syntax 
#        lambda arguments : expressions
#. the characters of lambda functions are :
#.  anonymous : they are unknown unless they are assigned explicitedly
#.  short and easy to use

####example 1
add = lambda x,y : x + y 
print(add(2,3))

print((lambda x : x+2)(2))

# #we can also usse lambda function in built-in functions as well
nums = [1, 2, 3, 4]
squared = map(lambda x: x**2, nums)
print(list(squared)) 

####alternative way wihtout using lambda function
nums = [1, 2, 3, 4]
squared=[]
for x in nums:
    x= squared.append(x**2)

print(squared)


## we can also use it inside the  regular functions 
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(4)) 
print(triple(4))