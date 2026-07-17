#ABSTRACTION
#--> the concept of hiding complex implementation details while exposing only 
# the essential features of an object.
""" from abc import ABC , abstractmethod
class shapes(ABC):
    @abstractmethod
    def aera():
        pass

    @abstractmethod
    def perimeter():
        pass

class square(shapes):
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        print(4*self.side)
    def area(self):
        print(self.side*self.side)

class circle(shapes):
    def __init__(self,radius):
        self.radius=radius
    def aera():
        pass
    def perimeter():
        pass

obj = square(10) """

#DUNDER METHOD
#-->they are not meant to be called directly; instead, they are invoked 
# automatically by the Python interpreter when specific operations occur, like 
# adding numbers or printing an object

"""class Robots:
    a=10
    def __init__(self,name):#dunder method
        self.name=name

    def __str__(self):
        return f"hello my name is {self.name}"
    
obj = Robots("alpha1")

print(obj.name)"""

""" class numbers:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value
    def __eq__(self,value):
        return self.value == value.value
    
a=numbers(20)
b=numbers(30)
print(a==b) """


