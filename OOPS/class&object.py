#CLASS --> 'blueprint/template of the object'

""" class sharmaVishnu:
    def sample(): #can be clld method or fun but its created under class its clld method
        print('this is sample function')
    def sample2(): #These methods do not take self because you are calling them directly using the class name
        print("this is sample 2 function")
sharmaVishnu.sample()
sharmaVishnu.sample2()  """

""" class sharmaVishnu:
    a= "lolo" #class ke andr variable clld attribute
    def sample():
        print("this is sample function")
sharmaVishnu.sample()
print(sharmaVishnu.a) """

#OBJECT --> 'real world entity'

""" class Animal:
    #attribute
    name="Animal"

    #method
    def greet (self):#jb bhi class ke adr fun ko object ki help se call karoge toh ek parameter set ho jaayega
      print('this is animal class')
#object ka naam save as hota hai as name of the variable
tau = Animal() # here tau is object cuz class is store in this #Animal class se ek naya object banao aur uska naam tau rakho"
tau.greet() #class can have multiple object
print(tau.name) """

#Q1. create a class which will perform 2 tasks:
#a. greet the user - this is ----- class
#b. adding up two number

""" class welcome: 
   def greet (self):
      print("this is welcome class")
   def add(self):
      a=10
      b=20
      print(a+b)
obj = welcome()
obj.greet()
obj.add() """
