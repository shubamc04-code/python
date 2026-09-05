"""FORMATING sTRING"""

#name ="shubham"

#age="22"

#print(f"my name is {name} and my age is {age}")

#name = input("enter your name")

#print(name)

""" Arithmatic opratore"""
#a=12

#b=34
#print(a+b)

#print(a-b)

#print(a*b)

#print(a//b)

#print(a/b)

#print(a**b)

"""IF ELSE STATEMENT"""
money =int(input("please provide me the moeny :-"))

if money == 10:
    print("you can buy a coffee")

elif money ==20:
    print("you can buy a coffee and a samosa")
else:
    print("you can buy a coffee and a samosa and a cake")


a=10
b=30

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

gender=str(input("enter your gender :-"))
if gender=="male":
    print("Good  morning sir")
elif gender=="female":
    print("Good  morning ma'am")
else:
    print("Good  morning everyone")

"""EVEN AND ODD NUMBER"""

a=int(input("enter your number :-"))
if a%2==0:
    print("this is even number")
else:
    print("this is odd number")



    

"""temperature"""


t = int(input("enter your temperature :-"))

if t < 0:
        print("freezing weather")

elif t>0 and t<10:
        print("very cold weather")

elif t>10 and t<20:
        print("cold weather")
elif t>20 and t<30:
        print("mild weather")
else:
        print("hot weather")



