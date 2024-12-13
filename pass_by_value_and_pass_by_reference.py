# Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”. 
# Depending on the type of object you pass in the function, the function behaves differently. Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

##for pass by value (immutable)
def modify_immutable(x):
    print("Before modification:", x)
    x = x + 10  
    print("After modification:", x)

num = 5
modify_immutable(num)
print("Original num:", num)    ##it shows that the value of original num is 5  which means it is immuatablee



###for mutabale (passs by refernece)
def modify_mutable(lst):
    print("Before modification:", lst)
    lst.append(4)  # Modifies the original object
    print("After modification:", lst)

numbers = [1, 2, 3]
modify_mutable(numbers)
print("Original list:", numbers)   #[1,2,3,4] because it is mutable 


# Immutable types (e.g., int, str, tuple): Assignments or modifications inside a function will not affect the original object.
# Mutable types (e.g., list, dict, set): Modifications inside the function will reflect outside because the same object is referenced.

        #######  https://imgur.com/a/CZfzgD8