class Animal:
    name="lion" #public attribute
    _age=12 #protected attribute
    __height = 120 #private attribute

    def speak(self): #public object method
        print("the lion is roars")
    def _walk(self): #private object method
        print("the lion is walking")
    def __sleep(self): #private method
        print("the lion is sleeping")

obj1=Animal()
#print(obj1.__height)
obj1.__sleep()
#private attribute and method cannot be accessed by your object and inherited classes
