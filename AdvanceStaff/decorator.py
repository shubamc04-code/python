"""Decorator is just a function that modifies another function
without changing its actual code.

Imagine you have a cake (your function). A decorator is like putting icing on the cake.it
doe not change the cake itself, but make it better,pretter ,or adds some new flavor

for creating a decorator you first need to create a decorator funcation and then inside that we will
create a wrapper

"""

class Animal:
    @property
    def show(self):
        print("hello how are you")

obj = Animal()
obj.show 


def decorate(func):
    def wrapper():
        print("I will print myself before the function hello")
        func()
        print("I will print myself after the function hello")
    return wrapper

@decorate
def hello():
    print("hello I am shubham Chouhan")
hello()


def decorate(func):
    def wrapper(a,b):
        print("your some is here")
        func(a,b)
        print("I hoperyou enjoy it ")
    return wrapper

@decorate
def addition(a,b):
    print(f"sum = {a+b}")
addition(12,13)