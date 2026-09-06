"""The while loop repeat a block of code as long as a condition is ture.
 It is useful when the number of iteration is unknown before execution"""

a = 1 

while a <= 30:
    print(a)
    a = a+1

a =256
while a>0:
    print(a%10)
    a=a//10


"""Revers a number"""
num =int(input("enter your number:-"))
rev = 0

while num > 0:
   rev=rev*10+num%10
   num=num//10

print(rev)


"""check pollindromic number"""

num = int(input("enter your number:-"))
original_num = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

if original_num == rev:
    print(f"{original_num} is a palindrome")
else:
    print(f"{original_num} is not a palindrome")


"""Genrate a randome number game"""

import random

num = random.randint(1,20)
tries = 0

while True:
  guess = int(input("please guess your number between 1 And 20 :-"))
  if num == guess:
    tries +=1
    print(f"congratutional you guess your right number is {num} in {tries} tries" )
    break
  
  elif num<guess:
    print("go a little lower")
    tries+=1

  elif num>guess:
      print("go a little higher")
      tries+=1