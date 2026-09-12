"""
Dubder methods are special methods in python that start and end with double
underscore , like __init__, __str__, __add__, etc
They automatically get called ehwn you perform certain actions on an object
they help you:
  Custmize behavour of your class
  Make your class objects behave like built-in data types (like string, list ,etc)
"""

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def __str__(self):
    return f"{self.name}: {self.marks} marks"


student = Student("Asha", 95)
print(student)  # __str__ is called automatically