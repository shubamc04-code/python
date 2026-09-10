"""
file handling :-
  file handling means creating ,reading,updating ,  deleting operation that we can perform in files.
  now lets see how to perform these operation in python.
  We have to use open() function to open a file in python.
 
  there have some mode
  r  = read , w = write , a =append ,x = create a new file

"""

#p= open(r'D:\programing language\python\Exception&File\exception.handling.py')
#print(p.read())


#r=open("superman.txt",'w')  

#r.write("hello this is shubham and I am writing  in this file")

#r.close()


r=open("superman.txt",'a')  

r.write("and now I'm appending the text inside")

r.close()