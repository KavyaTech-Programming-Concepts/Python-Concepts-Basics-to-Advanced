        ##method overriding in python
#also known as runtime polymorphism , method in child class or subclass overrides method in superclasss(parent class)

class Animal :
    def sound(self):
        print("some animal sounds")

class Dog (Animal):
    def sound(self):
        print("woof woof!")

class Cat(Animal):
    def sound(self):
        print("meow")

a=Animal()
a.sound()           ##output--> some animal sounds


animals=[Dog(), Cat()]
for animal in animals:
    animal.sound()          ##output--> wwof woof and meow

## we can observe that both the dog and cat classes override sound() method of the class Animal
### it is the core concept that achieves polymorphism, in oveerding a subclass provides its own specific implementation of a method that is already defined in its superclass
###this allows subclasses to alter or extend the behaviour of parent clas methods