##if it quacks like duck and walks like duck, then it is a duck

##example
class Duck:
    def swim(self):
        print("i am a ducn and i can swim")
    def speaks(self):
        print("quack quack!")

class Dog :
    def swim(self):
        print(" i am a dog and i can swim ")
    def speaks(self):
        print("woof woof !")

## we can oobserve that both dog and duck class share 'swim', and 'speaks' methods
def display(a):
    a.swim()
    a.speaks()
    print('information displayed\n ')

d1=Duck()
display(d1)
d2=Dog()
display(d2)
