"""Understanding *args and **kwargs.

Theory:
	*args collects any extra positional arguments into a tuple.  The name
	``args`` is a convention; the asterisk is what performs the packing.

	**kwargs collects any extra keyword arguments into a dictionary.  The
	name ``kwargs`` is also a convention; the double asterisk performs the
	packing.

	They are useful when a function should accept a flexible number of
	arguments.  They can also unpack a tuple/list with * and a dictionary
	with ** when calling a function.
"""


def introduce(name, *subjects, **details):
	"""Accept required, extra positional, and extra keyword arguments."""
	print(f"Name: {name}")
	print(f"Subjects (tuple from *subjects): {subjects}")
	print(f"Details (dict from **details): {details}")


# "Math" and "Python" are collected in subjects; the keywords are collected
# in details.
introduce("Asha", "Math", "Python", age=20, city="Delhi")


def add(*numbers):
	"""Receive any number of positional numbers and return their sum."""
	return sum(numbers)


print("Total:", add(10, 20, 30))


# Unpacking arguments while calling a function:
subjects = ("English", "Science")
details = {"age": 21, "city": "Mumbai"}
introduce("Ravi", *subjects, **details)




def addition(*args):
	total = 0
	for i in args:
		total += i
	return total

a= addition(12,34,45,65,76,34,23,545,65)
print(a)

def information(**kwargs):
	print("your information is\n\n")
	for i in kwargs:
		print(f"{i} : {kwargs[i]}")

information(name="shubham", age= 22, designation ="Mern fullStack developer")
		