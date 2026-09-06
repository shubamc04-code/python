"""The while loop repeat a block of code as long as a condition is ture.
 It is useful when the number of iteration is unknown before execution"""

#a = 1 

#while a <= 30:
   # print(a)
    #a = a+1

#a =256

#while a>0:
    #print(a%10)
    #a=a//10


"""Revers a number"""
num =int(input("enter your number:-"))
rev = 0

while num > 0:
   rev=rev*10+num%10
   num=num//10

print(rev)
