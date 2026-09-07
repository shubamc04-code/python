""" Function in Python group code into a block that can be executed by calling
    the function name. This helps avoid repetition and makes programs modular and readable.
    
    there are many in-build functions in python like print() , inpute() len() etc
    
    but you can create your own function and they are called as user defined functions. To make your 
    own function you have  to use def keyword and then name the function . After this to use def keyword
    and then name the function.After this you have to call the function using Name() and parameters"""


#def hello():
  #  print("this is a hello function")

#hello()


# Positional Arguments
def sum(a,b): # parameter get
    print(f"the sum of your number is : {a+b}" )

sum(12,34)#arguments pass



#types of Arguments 

def hello(name , age):
    print(f" hello {name} your age is {age}")
hello("shubham", 22)


# keyword Argument
def hello(name , age):
    print(f" hello {name} your age is {age}")
hello(age=22, name="shubham" )



#default Argumnet
def sum(a,b=45):
    print(a+b)
sum(a=23)


#check it if string are pallindrom or nor

def pallindrom(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev=rev+st[i]

    if rev == st:
        print("pallindrom")
    else :
        print("not pallindrom")

st = input("enter your String:-")
pallindrom(st)
