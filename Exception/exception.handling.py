"""
Errors
     Errors occur due to mistake in the code that prevent it from
     runing.These can be syntax error or logical error


"""

#Syntax error
"""
print("Hello mitra mandali) # missing double cotes closer

indentation error 

def func():
print('hello) # no indentation
"""


# Exception 

""" Exception are unexpected events or  error that occurs dusring the execution of a program ,
    which disrupts the normal flow of the program
"""

a = int(input("enter number :"))
try:
 print(10/a)

except Exception as err:
 print(f"sorry there is an error {err}")

else:
 print("good")

finally:
 print("I will run no matter what")
   
print("ok i have a done the division")