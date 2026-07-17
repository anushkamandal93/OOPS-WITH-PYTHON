#POLYMORPHISM:
#--> many forms of same interface
  
class animal:
    def speak(self):
        print("animals are shouting")
class human:
    def speak(self):
        print("humans are inteeligent so they are speaking")

obj1=animal()
obj2=human()

obj1.speak()
obj2.speak()

#both the speak method appears to be same but both have different task and this is known as 
#POLYMORPHISM

#METHOD OVERRIDING
#a child class object has the power to call methods and attributes of a parent 
#but he cannot call the details method of his parent class cause that deatils method is overriding
#and this concept is known as OVERRIDING.
class reebok:
    def __init__(self,material,size):
        self.material = material
        self.size = size
    
    def details(self):
        print("your bag details")
        print(self.material)
        print(self.size)

class campus(reebok): 
    def __init__(self,material,size,colour):
        super().__init__(material,size)
        self.colour = colour

obj1 = campus("leather", 10 ,"black" )   
obj1.details()

#METHOD OVERLOADING(no use case in python)
#-->allow a class to have multiple methods with exact same name as long as 
# their parameter lists are different
class animal:
    def hello (self,a):
        print("hw r u")
    def hello (self,a,b):
        print("hw r you")