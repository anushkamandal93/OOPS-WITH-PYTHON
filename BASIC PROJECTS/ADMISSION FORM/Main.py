#1. CREATING PARENT CLASS
class students:
    def __init__(self,name,age,email,phone):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone

    def display_details(self):
        print(self.name)
        print(self.age)
        print(self.email)
        print(self.phone)

class class10admission(students):
    def __init__(self,name,age,email,phone):
        super().__init__(name,age,email,phone)
    print("admission sucessful")

class class12admission(students):
    def __init__(self,name,age,email,phone):
        super().__init__(name,age,email,phone)
        if self.age>= 16:
            print("admission successful")
        else:
            print("admission failed")

print("press 1 for class 10th admission")
print("press 2 for class 12th admission")

choice=int(input("enter your choice"))
name=input("tell your name")
age=int(input("enter your age"))
phone=int(input("enter your phone"))
email=input("enter your mail") 

if choice==1:
    student1 = class10admission(name,age,email,phone)
    student1.display_details()

if choice==2:
    student1 = class12admission(name,age,email,phone)
    student1.display_details()