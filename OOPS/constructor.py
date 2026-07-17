#CONSTRUCTOR
'Constructor is a special function jo class ka object banate hi automatically run ho jata h'
'represent by __int__(dunder method)'
'sabse phele execute hone wale function h does not matter inke upar ya neeche koi function present h'

""" class sharmavishnu:
    def __init__(self):
        print("this is constructor function")
obj = sharmavishnu()"""

""" class sharmavishnu:
    def __init__(self):
        print("this is constructor function")
    def menu(self):
        print("paneer kulche") 
        
obj = sharmavishnu()
obj.menu()"""

""" class sharmavishnu:
    def __init__(self,name,age):
        self.name = name #instance attribute
        self.age = age
        print("this is constructor function")
        # print(self.name)
        # print(self.age) #can be written here also no effect on o/p

    def menu(self):
        print(self.name)
        print(self.age)
        print("paneer kulche")
        
obj = sharmavishnu("amit",21)
obj.menu() """

#QST make a class which will take 2 numbers as input create
#1. 2 instance attribute
#2  create a function which will print greatest among them

""" class Sample:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def greater (self):
        if self.a>self.b:
         print(self.a, "is greater")

        elif self.a<self.b:
            print(self.b,"is greater")
        else:
           print("equal")
obj =Sample(10,20)
obj.greater() """ 

""" lass Laxit:
    def _init_(self):
        print("This is the Laxit class")

    def greet(self,a,b):
        print(f"The sum of {a} and {b} is {a+b}")
    
    def _init_(self):
        print("This is another constructor function")
    
    def greet(self,name):
        self.name = name #Instance Attribute
        print(f'hello {self.name}')


obj = Laxit()
obj.greet(":Laxit") """

#CLASSMETHOD------------------------------------------------------------------------------------------------------
""" class animal:
    name="dog"
#instance (object) can never change your class attributes
    @classmethod
    def change(cls,new):
        cls.name=new
        print(cls.name)
cheeta=animal()
cheeta.change("cat")
print(animal.name) """

#STATICMETHOD-----------------------------------------------------------------------------------------------------
""" class sharmavishnu:
    @staticmethod
    def menu():
        print('paneer kulche')
        print('paneer tikka')
        print('paneer cheese sandwich')
        print('cold coffee')
new_market = sharmavishnu()
new_market.menu() """


