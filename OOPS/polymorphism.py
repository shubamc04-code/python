"""
Polymorphism
============
Theory concept:
Polymorphism means "many forms". In OOP, it allows objects of different classes
to be treated in the same way if they share a common method or interface.

The same method name can behave differently depending on the object calling it.
This helps us write flexible and reusable code.

Real-world example:
Think of a "make_sound()" action for animals:
- Dog says: "Bark"
- Cat says: "Meow"
- Cow says: "Moo"
All are animals, but each produces a different sound.

In Python, polymorphism is usually achieved through method overriding.
"""


class Dog:
    def sound(self):
        return "Bark"


class Cat:
    def sound(self):
        return "Meow"


class Cow:
    def sound(self):
        return "Moo"


# Same method name, different behavior based on object type
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(type(animal).__name__, "->", animal.sound())

 