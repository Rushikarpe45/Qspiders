# from abc import ABC,abstractmethod


# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass
# #concrete class
# class Car(Vehicle):
#     def start(self):
#         print("This method will start your car")
    
# class Bike(Vehicle):
#     def start(self):
#         print("this method will start your bike")

# c1=Car()
# c1.start()

# b1=Bike()
# b1.start()

# from abc import ABC,abstractmethod

# class Calculator(ABC):
#     @abstractmethod
    
#     def add(self,a,b):
#         pass
#     def sub(self,a,b):
#         pass
#     def mul(self,a,b):
#         pass
#     def div(self,a,b):
#         pass
# class Cal(Calculator):
    
#     def add(self,a,b):
#         print(a+b)

#     def sub(self,a,b):
#         print(a-b)
#     def mul(self,a,b):
#         print(self,a*b)
        
#     def div(self,a,b):
#         print(self,a/b)

# c1=Cal()
# c1.add(10,20)


# animal
# speak'
# tiger 
# dog
# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
    
# class Tiger(Animal):
#     def speak(self):
#         print("roar")

# class Dog(Animal):
    
#     def speak(self):
#         print("barked")


# c1=Tiger()
# c1.speak()
# c2=Dog()
# c2.speak()
        
#created and shape with and abtract method area   make to subclass reactangel and circle both must implement area and return they area

#write  crated  object print therir area


# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self,a,b):
#         pass
# class rectangle(Shape):
#     def area(self,a,b):
#         print("Rectangle Area =", a * b)
        

# class circle(Shape):
#     def area (self,a,b):
#         print("Rectangle Area =", 3.14*b*b)

# c1=rectangle()
# c1.area(10,20)
# c2=circle()
# c2.area(3.14,6)


# from abc import ABC,abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def account(self):
#         pass
#     def balance(self):
#         pass
    
# class Saving_Account(Bank):
#     def account(self):
#         print("this is saving accout balance")
    
# class Current_Account(Bank):
#     def balance(self):
#         print(" this is current balance account")
#     def account(self):
#         return super().account()
        
# # Cus1=Saving_Account()
# # Cus1.account()
        
# Cust2=Current_Account()
# Cust2.balance()
# Cust2.account()


#vowel 
# from abc import ABC,abstractmethod
# class Karpe(ABC):
#     @abstractmethod
#     def Girls(self):
#         pass
#     def Boys(self):
#         pass
#     def children
    
# class Bhausaheb_Karpe(Karpe):
#     def Girls(self):
#         print("Three Girls")
    
#     def Boys(self):
#         print("No Boyes in KarpeNo1")
        
# class Valmik_Karpe(Karpe):
#     def Girls(self):
#         print("only one  girls")
        
#     def Boys(self):
#         print(" two boy ")
        
# class Sadashibv_Karpe(Karpe):
#     def Girls(self):
#         print("three Girls are here")
        
#     def Boys(self):
#         print("two boyeies")
        
# class Vitthal_karpe(Karpe):
#     def Girls(self):
#         print("two girls are here")
#     def Boys(self):
#         print("only one boys")

# class Dnayeshwar_karpe(Karpe):
#     def Girls(self):
#         print("only one girls")
#     def Boys(self):
#         print("only one boys")
    
# Member1=Vitthal_karpe()
# Member1.Boys()

# Member2=Valmik_Karpe()
# Member2.Boys()




# from abc import ABC,abstractmethod

# class Dog(ABC):
#     def __init__(self,name):
#         self.name=name

#     @abstractmethod
#     def sound(self):
#         pass

#     def display_name(self):
#         print(f"Dog's Name:{self.name}")

# class Labrador(Dog):
#     def sound(self):
#         print("labrador Woof!")

# class Beagle(Dog):
#     def sound(self):
#         print("Beagle Bank!")

# d=Labrador()
# d.sound()