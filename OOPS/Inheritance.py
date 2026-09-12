""" In general terms  inheritance means property or any possession that comes to an heir
it work between classes
"""

# Syntax

"""Syntax is very simple just like you take parameters in functions here
 you will take parameters but those parameters will be classes
"""

class Parent :
    def speak(self):
        print("I can speak")

class Child(Parent):
    pass

class Factorymumbai:# parent class / super class
    a = "I am an attribute mentioned inside Factrory"
    def hello(self):
        print("hello I am a methd mentioned inside Factory")

class Factorypune(Factorymumbai):  # child class / sub class
    pass


obj2 = Factorypune()
obj2.hello()


# Constructor in Inheritance

class Animal:
    def __init__(self,name):
        self.name= name


class Human(Animal):
    #constructor  function
    def __init__(self, name, age):
        super().__init__(name)
        self.age=age

    def show(self):
           print(f" hello your name is {self.name}, and age is {self.age}")

person1 = Human("Shubham",22)
person1.show()



#Multipal Inheritance

# Example: one child class inherits from two parent classes
class Father:
    def drive(self):
        print("Father can drive")

class Mother:
    def cook(self):
        print("Mother can cook")

class Child(Father, Mother):
    pass

child = Child()
child.drive()
child.cook()


# Multilevel Inheritance
# One class inherits from another class, and a third class inherits from it.
class Grandparent:
    def family_name(self):
        print("Our family name is Sharma")

class ParentLevel(Grandparent):
    def work(self):
        print("Parent goes to work")

class ChildLevel(ParentLevel):
    def study(self):
        print("Child goes to school")

member = ChildLevel()
member.family_name()
member.work()
member.study()


# Hierarchical inheritance
# One parent class is inherited by multiple child classes.
# Real-world example: different types of employees share common details,
# while each type has its own behavior.
class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def write_code(self):
        print("Developer writes code")

class Designer(Employee):
    def create_design(self):
        print("Designer creates designs")

developer = Developer()
designer = Designer()

developer.work()
developer.write_code()
designer.work()
designer.create_design()




