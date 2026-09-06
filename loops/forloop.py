#two LOOP for & while

"""for i in range(1,21,1): # range defind S S S ,, Start ,stop , step 
    print(i)# printing the value of i 1 to 20 num

    # for in reverse order

for i in range(20,0,-1): 
    print(i)# printing the value of i 20 to 1 num"""


"""LEST PRINT A TABLE"""

"""num = int(input("enter your number which table you want to print :-"))

for i in range(1,11,1):
    print(num,"*",i,"=",num*i)



    a ="shubham chouhan"
    print(len(a)) # printing the length of string

    for i in range(len(a)):
        print(a[i]) # printing the string in vertical order"""


"""for i in range(1,21):
    if i== 15:
        break # break the loop when i is 15
    else:
        print(i)

for i in range(1,21):
    if i == 15:
        continue # skip the iteration when i is 15
    print(i)"""


#num = int(input("enter your number:-"))

#for i in range(num):
    #print("hello world")



#n = int(input("please tell your number:-"))
#for i in range(1,n+1):
#    print(i)

"""Sum of n terms"""

"""n = int(input("enter your number which you want sum:-"))
sum = 0
for i in range(1,n+1,1):
    sum +=i 
print(sum)




n = int(input("enter your number which you want fact:-"))
fact = 1
for i in range(1,n+1,1):
    fact *=i 
print(fact)"""


"""s = int(input("enter your starting range for even odd number:-"))
e = int(input("enter your ending range for even odd number:-"))
for i in range(s,e+1,1):
    if i % 2 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")"""



"""num = int(input("enter ypur number for factorizationh:-"))
for i in range(1,num+1,1):
    if num % i ==  0:
        print(f"{i} is factor of {num}")"""


"""num = int(input("enter ypur number for a perfact number:-"))
sum=0
for i in range(1,num,1):
    if num % i ==  0:
      sum +=i
if num == sum :
        print(f"{num} is perfact number")
else :
        print(f"{num} is not a perfact number")"""


num = int(input("enter ypur number for a prime number:-"))

if num < 2:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number")

     

    
  






    

    



