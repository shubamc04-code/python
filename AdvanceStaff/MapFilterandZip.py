"""Map And Filter
  Make is used for appying a function to multiple items.
  Take a list(or any sequence)
  applies the same function to every item in that list
  Gives you back a new list (in Python 3 it gives a map object which you can convert to a list)
"""

a = [1,2,3,4,5,]

result = map(lambda x : x*2,a)

print(list(result))

# Convert strings to uppercase
names = ["alice", "bob", "charlie"]
print(list(map(str.upper, names)))

# Convert strings to integers
numbers = ["10", "20", "30"]
print(list(map(int, numbers)))

# Apply a function to two lists at the same time
first = [1, 2, 3]
second = [4, 5, 6]
print(list(map(lambda x, y: x + y, first, second)))

# Use a regular function with map
def square(number):
  return number ** 2

print(list(map(square, a)))



"""Use map() when ypu want to transform every item in a list 
it doesn"t remove or skip items ( that't what filter () does),
You can use it with lambda or normal functions."""



#FILTER 
"""
Filter as the name suggest is used to silter out the stuff
Take a list (or other Sequence)
Checks each item using a function ( a set)
Keep only the items that pass the test
"""

number = [1,2,3,4,5]
even = filter(lambda x: x%2 ==0 , number)
print(list(even)) 

# Real-world example: keep only products that are in stock and affordable.
products = [
  {"name": "Laptop", "price": 900, "in_stock": True},
  {"name": "Phone", "price": 700, "in_stock": False},
  {"name": "Headphones", "price": 80, "in_stock": True},
  {"name": "Monitor", "price": 250, "in_stock": True},
]

affordable_products = filter(
  lambda product: product["in_stock"] and product["price"] <= 300,
  products,
)

print(list(affordable_products)) 