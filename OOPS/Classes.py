"""
A classes is like a blueprint ot templat for crating object.
Think of a class like the blue print of a house. It defines what the house should have (rooms, windows,etc)
but does  not build the house, An object is the actual  house built  using that blueprit
"""

class Car:
    brand = "BMW" #Attribute

    def make_color(self): # method
        print("blue")

Car()
print(Car().brand)
