"""
# Set are mutable but it can not have any duplicate values,
Set are unordered and you can not access them through index values
Set Store the data like string,number,tuples but not everything 

isme index nam jesi koi chij nhi hoti h 
but ye hash m value store krke traversing krta h 


how set store the value:-
1. Each value in a set os hashed usinf a hash function hash() is python
2. The hasg s used as an index to store the element in memory.
3. Since hashing does not maintain order ,sets are unordered.
4. only immutable (hashble) objects can be stored in a set
"""

#syntax
s = {1,3,4,5,5,6,7}
print(s)

#hash
b= hash("shubham")
print(b)

c=hash((1,2,3,4,5))
print(c)

#traversing in set

a = {1,8,4,5,3,6,9,12,10,11,13,"hello"}

for i in a:
    print(i)


#method of set

a.add(4) # adds an element to the set
a.remove(3) # Rremove 3 (raise error if not found)
a.discard(4) #Remove 4 (no error if not found)
popped_element=a.pop() #Remove a random element
print(popped_element)
a.clear()  # Removes all elements

# if you have a two set
a = {1,8,4,5,3,6,9,12,10,11,13,"hello"}
b={1,2,3,4,5,6,12,23,13,24,53,25,63,25}


union_set = a.union(b)#.... a|b
intersection_set = a.intersection(b)#.... a&b
difference_set= a.difference(b)#.... a-b
symentric_diff = a.symmetric_difference(b)#.... a^b
