# class A:
#     a=10
#     _b=20
#     def show(self):
#         print("this is protectecd")
# ob=A()
# print(ob.a+ob._b)
# ob.show()


# class Bank:
#     bname="abc"
#     bno = 3452345234
#     _bmail="abc@gmail
#     _bid="ABC01"
#     def _display(self):
#         print("this is bank")
# obj=Bank()
# print(obj.bname,obj.bno,obj._bmail,obj._bid)
# obj._display()


#________________________________________Private_____________________________________________________________________________

# class Scl:
#     scl_name="svr"
#     scl_no=8647836873
#     scl_loc="nagpur"
#     __scl_revenue=900000
#     scl_addmissions=1902
#     def __init__(self,st_name,st_id,st_loc):
#         self.st_name= st_name
#         self.st_id=st_id
#         self.st_loc=st_loc
#     def __display(self):
#         print(self.st_name, self.st_id, self.st_loc)
# obj=Scl("pratik",1991,"pimpri")
# obj._Scl__display()
# print(Scl._Scl__scl_revenue)
        
# class Bank:
#     bname="abc"
#     __brevenue=324627435526
#     def __init__(self,cname,cloc,csal):
#         self.cname=cname
#         self.cloc=cloc
#         self.__csal=csal
#     def _display(self):
#         print(self.cname,self.cloc,self.__csal)
# class Bank_bnk(Bank):
#     pass
# c1=Bank_bnk("cust1","pimpri",15000)
# c1._display()
# print(Bank_bnk._Bank__brevenue)  


# class Bank:
#     __bname="abc"
#     __bloc="nashik"
#     __bphn=12345678
#     __bemail="abc@gmail.com"
    
#     def __init__(self,eid,ename,ephn):
#         self.eid=eid
#         self.ename=ename
#         self.ephn=ephn
#     def display(self):
#         print(self.eid,self.ename,self.ephn)

# ob1=Bank(100,"rushi",79752)
# ob1.display()

# print(ob1._Bank__bloc) #syntax method
# print(ob1._Bank__bemail)


#getter and setter methods

# class School:
#     __Sname="ABC"
#     def __init__(self,marks):
#         self.__marks=marks
        
#     def get_marks(self):
#         return self.__marks
    
#     @classmethod
#     def get_sname(cls):
#         return cls.__Sname
    
#     def set_marks(self,new_marks):
#         self.__marks=new_marks
    
#     @classmethod
    
#     def set_sname(cls,new_sname):
#         cls.__Sname=new_sname
        
# ob1=School(89)

# print(ob1.get_marks())

# ob1.set_marks(560)
# print(ob1.get_marks())

# ob1.set_sname("ABCD")
# print(ob1.get_sname())#synatx


# class PetHouse:
#     def __init__(self,a1,a2):
#         self.__a1=a1
#         self.__a2=a2

# class Owner(PetHouse):
#     def __init__(self, a1,a2,name):
#         # super().__init__(a1,a2)
#         self.__name=name
        
    
#     def get_name(self):
#         return self.__name
    
#     def set_name(self,new_name):
#         self.__name=new_name
        
#     # def get_type(self):
#     #     return 
        
# ob1=Owner(1,2,"rushi")
# ob2=PetHouse(1,2)
# # print(ob1.get_name())

# print(ob2._PetHouse__a1)
    


# property method
# class Company:
#     cname="ABC"
#     def __init__(self,sal):
#         self.__sal=sal
    
#     @property
#     def sal(self):
#         return self.__sal
    
#     @sal.setter
#     def new_sal(self,newsal):
#         self.__sal=newsal
        
# ob1=Company(2000)

# print(ob1.sal)



# class PetHouse:
#     def __init__(self,a1,a2):
#         self.__a1=a1
#         self.__a2=a2

#     @property
#     def a1(self):
#         return self.__a1
#     @property
#     def a2(self):
#         return self.__a2
#     @a1.setter
#     def a1(self,newvalue):
#         self.__a1=newvalue
# class Owner(PetHouse):
#     def __init__(self, __a1,__a2,name):
#         super().__init__(__a1,__a2)
#         self.__name=name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self,newname):
#         self.__name=newname

# ob=Owner(1,2,"rushi")
# ob.name="ketan"
# ob.a1=2
# ob.a2
# print(ob.name,ob.a1,ob.a2)


# class Dog:
#     def __init__(self,name,breed,age):
#         self.name=name
#         self._breed=breed
#         self.__age=age
    
#     def get_info(self):
#         return(f"name:{self.name},breed:{self._breed},age:{self.__age}")
    
#     #getter and setter for private attribute
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if age>0:
#             self.__age=age
#         else:
#             print("invalid age!")
            
    
# dog=Dog("Buddy","Labrador",3)

# print(dog.name)
            
# print(dog.get_info())

# dog.set_age(5)
# print(dog.get_info())
# print(dog._breed)