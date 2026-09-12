"""you saw last example where we wanted material of house using object 
 if we talk about a function we can ask the user using
 parameters, but in class we can't have parameters for that we use constructor.
 A constructor is a method that runs automatically when we call a class and this constructor
 function will targrt thr objects location
 
 """

class Factory:
   name = 'amazone' #class Attribute
   def __init__(self,material,zips, pokets):
      self.material= material #instance Attribute
      self.zips = zips
      self.pokets= pokets

   def show(self):
      print(F"your object details are {self.material},{self.zips},{self.pokets}")
      

reebok = Factory("leather",2,2)

campus  = Factory("lyon",3,3)

print(reebok.pokets)
print(campus.pokets)

reebok.show()