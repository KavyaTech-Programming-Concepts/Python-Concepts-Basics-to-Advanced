#sequence of characters enclosed in "",'' or '''asjdhkjasdfhaklf '''' and eg : "raj"
str="raj"
print(str)
multi_line_string='''this is
a multi line string '''

            #string indexing and slicing
str="kathmandu"
print(str[0])       #---> k
print(str[-1])      #----> u
print(str[:3])      #takes upto three characters from start that is 'kat'
print(str[3:])      #takes 3 characters from back ide, 'ndu'
print(str[::1])     #reverse string

#concatenation and repetition
name="raj"+ " shrestha"  
print(name)  #----> "raj shrestha"
boy = "raj" *3          #-----> "raj raj raj"
print(boy)

#string formatting
name = "raj"
age ="500"
print(f"name is {name} and age is {age}")
print("my name is {} and my age is {} years ago".format(name,age))
