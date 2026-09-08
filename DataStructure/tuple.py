"""
Before starting we need to understand some of the terminoly
Immutable: TUples are not mutable you can not change the values of tuples

Duplictae: you can have duplicate values in tuple there are no restriction

Ordered : set are ordered and you can  access them through index values

Heterogenous : Set Also have heterogeneous nature and can have different types of data structure in tuple
"""

a=( 1,2,3,4,5,5,5,4,5,print(), "hello")

for i in range(len(a)):
    print(a[i])


#Tuples have only two methds

index = a.index(5)
print(index) # Find the index of first occurrence of 5
count_5 = a.count(5)
print(count_5) # Counts occurrence of 5


#TUple Unpacking

a,b,c,d,e=(1,2,3,4,5)
print(a)
