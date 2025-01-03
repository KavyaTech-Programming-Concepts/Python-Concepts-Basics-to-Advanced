                        ##Inheritance
# Inheritance is a mechanism where a new class (child or subclass) is derived from an existing class (parent or superclass). 
# The child class inherits attributes and behaviors (methods) from the parent class, and it can also override or extend them.

            ##When to Use Inheritance
# Is-a Relationship: Use inheritance when one class is a specialized version of another. For example:
# A Dog is a type of Animal.
# A Car is a type of Vehicle.
# Shared Behavior: When multiple subclasses share common behavior defined in the parent class.


                ##examplee
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog()
print(dog.sound())  


                        ###Composition
# Composition involves creating a relationship where one class contains an instance of another class and delegates work to it. It’s often described as a "has-a" relationship.
# When to Use Composition
# Has-a Relationship: Use composition when a class is made up of other objects.
# A Car has an Engine.
# A House has Rooms.
# Flexible Design: When you want to combine behaviors or functionality dynamically.
# Advantages
# Reduces tight coupling between classes.
# More flexible than inheritance (you can change composed objects at runtime).
# Avoids problems associated with deep inheritance hierarchies.
# Disadvantages
# Can lead to slightly more boilerplate code.
# May require more explicit delegation of methods.

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        return self.engine.start()


engine = Engine()
car = Car(engine)
print(car.start())  # Output: Engine started
