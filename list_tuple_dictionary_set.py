            #list in python
#ordered, mutable 
#syntax---> my_list=[l1,l2,...]
#it supports duplicate valyes

numbers=[12,1,2,8,5,3,4]
mixed=['raj',True, 1,"shrestha"]
mixed[0]='ram'    # it replaces " raj " to 'ram'
print(mixed[0])
print(numbers)

####there are many methods we can use in list such as
# append()    #it appends the data at the end of the list
mixed.append(5)
print(mixed)

# remove()    #it removes the index of the list 
mixed.remove(1)
print(mixed)

# pop()       #it pops out the element
mixed.pop(2)
print(mixed)

#sorted()       #it sorts the given list
sorted1=sorted(numbers)
print(sorted1)

#### similarly=reverse(),index(),count()





                    ##tuples
#tuples is ordered but not mutable ie  imutable and support duplicate vaues as well
#it takes minimal memory than list
#used when data should not change
#tuple=(t1,t2,...)

# Examples:
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3,2)

# Accessing
print(fruits[0])  # 'apple'

# Tuples are immutable:
# fruits[1] = "blueberry"  # Error: Tuples cannot be modified



#methods are:
print(numbers.count(2))  #use to count the total number of element in the given tuples
print(numbers.index(2))  #returns the index of the given tuples



                        ######dictionary
###unordered collection of key-value
####immutable and unique keys
##but values can be duplicated and of any type
#syntax---> dict_name={key1=value1,key2=value2}

# Examples:
person = {"name": "Alice", "age": 25, "city": "New York"}
empty_dict = {}

# Accessing and modifying
print(person["name"])  # 'Alice'
person["age"] = 26  # Modify the value
person["country"] = "USA"  # Add a new key-value pair


                    #set
#unordered collection of elements
#syntax---> set={s1,s2,...}
#mutuable
#does not allow duplicate
#useful for membership testing and eliminating duplicates.



# Examples:
fruits = {"apple", "banana", "cherry"}
empty_set = set()  # Use `set()` for an empty set

# Adding and removing
fruits.add("orange")
fruits.remove("banana")
print(fruits)  # Order may vary

### https://imgur.com/a/h7fcHQv