#INHERITANCE
"""
1. Single Inheritance 
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchial Inheritance
5. Hybrid Inheritance
"""
#1. Single Inheritance --> 1 Parent class and 1 Child Class
#EX:1
""" class Parent:
    def __init__(self):
        print('This is Parent class constructor')

    def greet(self):
        print('This is Parent class')

class Child(Parent):
    def __init__(self):
        print("This is child class constructor")

    def show(self):
        print('This is Child class')


obj = Child()
obj.greet()
obj.show() """ 

#EX:2
""" class Factory:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def show(self):
        print(f'Bag has {self.name} and {self.color} color')
    
class Bata(Factory):
    def __init__(self,name,color,zip,pockets):
        super().__init__(name,color)
        self.zip = zip
        self.pockets = pockets
    
    def display(self):
        print(f'Bag has {self.name} , {self.color} color , {self.zip} zip and {self.pockets} pockets')
Rahul = Bata('Rahul','Purple',4,10)
Rahul.display() """



#2. Multiple Inheritane -> 1 Parent,multiple Child
""" class Father: #Parent1

    def __init__(self):
        print('This is Father class constructor')

    def greet_father(self):
        print('This is Father class')

class Mother: #Parent2
    def __init__(self):
        print('This is Mother class constructor')

    def greet_mother(self):
        print('This is Mother class')


class Child(Mother,Father): #Child If we have to run constructor of Father class first
    
    def __init__(self):
        Father.__init__(self) #Sabse pehle Father class ka constructor will be run
        Mother.__init__(self) #After Father class Mother class constructor will be run

obj = Child()
obj.greet_father()
obj.greet_mother() """


#3. MULTILEVEL INHERITANCE
#--> one child class become parent of another class 
""" class A: #g.parent
    def greet(self):
       print("this is classs A")
class B(A): #parent
    def show(self):
        print('this is class B')
class C(B): #child class
    def details(self):
        print('this is class C')

obj = C()
obj.show()
obj.greet()
obj.details()

#EX:2
class CEO:#g.parent
    def __init__(self):
        print('this is CEO class contructor')
class manager(CEO):#child class,parent
    def __init__(self):
        super().__init__()
        print('this is manager class constructor')
class employee(manager):#child
    def __init__(self):
        super().__init__()
        print('this is employee class constructor')

rahul=employee()
 """
#4. **HIERARCHIAL INHERITANCE --> 2 parent 1 child
#EX:1
""" class Parent:
    def greet(self):
        print("This is Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj = Child2()
obj.greet()

obj2 = Child1()
obj2.greet() """

#EX:2
""" class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def details(self):
        print(f"Hello {self.name} you have {self.balance}")
    
class Saving(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        print(f'This is Saving class constructor {self.name} , {self.balance}')

class Current(Account):
    def __init__(self,name,balance,type):
        super().__init__(name,balance)
        self.type = type
        print(f'This is Current class Constructor {self.name} , {self.balance}, {self.type}')
obj = Current("Mukesh",0,"Current") """

