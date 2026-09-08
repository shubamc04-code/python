"""list basic
*  First we have to know what is the syntax of list and how ,to create
   a list we have to use square brackets([]) 
   Fruits = ["apple","banana", "cherry"]  
   mutable  - multibility refers to whether an object value can be 
             changed after creation. And list allows this 
    Duplicate - we know data Structure are used to store  multiple
             values so duplicates means same value occuring
    Ordered - List maintains ordered data structure maintains the sequence of element
            as they were inserted this means you can Access elements using their position """

fruits = ["apple","banana", "cherry"] 

a=[12,14,23,43,53,23,43,54,65,23,55]
print(a[0:6])

#1st way using index

a=[12,14,23,43,53,23,43,54,65,23,55]
for i in range(len(a)):
    print(a[i])

#2nd wqay directly on values

for i in a :
    print(i)


#METHOD

print(dir(list))  #print all the list method
help(list)

l = [1,2,3,2,4,5]

l.append(6)#insert the last in list
l.append(7)
print(l)

l.insert(1,1) # insert inside the list
print(l)

l.remove(2)#remove first occurrence of 2
print(l)

popped_items=l.pop(4)#Remove and store the element at index 4

index=l.index(5)# find the index of 5

l.count(2)# count occurences of 2

l.sort()# Sort the list in asending order

l.reverse() # Reverse the list order

new_list = l.copy() # create a copy of the list

l.clear()#Remove all element from the list

# print postive and nagetive number of list 

l=[12,34,-54,-34,23,-45,34,35-46,-96]
print("positive number are:-")
for i in l:
    if i>=0:
        print(i)
print("nagetive numbers are;-")
for i in l:
    if i<0:
        print(i)


#print mean of the list

l=[12,34,23,34,35,2,34,5]

sum=0
for i in l:
    sum+=i
print(f"mean of list : {sum/len(l)}")

#Print the gretest element and its index too

l=[23,34,2,3,4,23,54,652,2,65,343,5433,54,232,12]
larg=0
index=0
for i in range(len(l)):
    if larg<l[i]:
      larg=l[i]
      index = i
print(f"your gretest no is {larg} & its index no. {index}")


# print the list is sorted or not

l1=[23,34,23,54,35,64,23]
l2=[12,13,14,14,15,16]

for i in range(len(l1)-1 and len(l2)-1):
    if l1[i]<l1[i+1] and l2[i]<l2[i+1]:
        continue
    elif l1[i]>l1[i+1]:
        print("your list 1 is not sorted")
        break
    else:
        print("your list 2 is not sorted")
        break
else:
    print("your both listed are sorted")