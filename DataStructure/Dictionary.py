"""Dictionary Syntex and  working
Now we  know we have to use key and value pairs to store values in dictionary
and the key in dictionary acts like index values that we use in list

keys must be unique,not same 
its follows insertion order

student = {"name": "shubham", "age":22}
print(student['name']) //output :  shubham

again telling we can perform CRUD operation on values but not all on key 
cause the keys cannot be changed after creation.
"""

"""student = {"name": "shubham", "age":22}
print(student['name'])

d = { 10:100, 20:200, 30:300, 40:400}
print(d[10],d[20])

d[10] = 1000 # UPDATING
print(d)

d.update({50:500}) # d[50] = 500
print(d)

del d[30]
print(d)

#Dictionary traversing

d = { 10:100, 20:200, 30:300, 40:400}
for i in d:
    print(d[i])

#METHODS

a = [1,2,3,4,5]
b = a #deep copy
b[0] = 100
print(a)

a = {1:10,2:20,3:30,4:40,5:50}
b = a.copy() #shallow copy
b[0] = 100
print(b)
a.get(1)
print(a)
print(a.items())
a.pop(2)
print(a)
a.update({2: 300})
print(a)"""

#Merg the Dictionary

d1 = { 10:100, 20:200, 30:300,40:400}
d2 = { 50:500, 60:600, 70:700,80:800}
for i in d2:
    d1[i] = d2[i]
print(d1)

# total sum
total = 0
for value in d1.values():
    total += value
print(total)

d1 = { 10:100, 20:200, 30:300,40:400}
d2 = {40:400, 50:500, 30:600, 70:700,80:800}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
      d1[i] = d2[i]
print(d1)
