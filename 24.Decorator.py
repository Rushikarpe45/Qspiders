# def outer(func):
#     def inner(*args,**kwargs): #to safer time
#         print("www.instagram.com")
#         print("login")
#         func(*args,**kwargs)
#         print("logout")
        
#     return inner
# @outer 
# def f1():
#     print("i am posting photo")
    
# f1()

# @outer
# def f2(a,b):
#     print("addition of two number",a+b) 
# f2(2,5)


#to check whattime do you have execution

# import time

# def outer(func):
#     def inner(*args,**kwargs):
#         start=time.time
#         func(*args,**kwargs)
#         end=time.time
#         print(start-end)
        
#     return inner
# @outer
# def f2(a,b):
#     print(a+b)
# f2(2,5)

# @outer
# def f3(S):
#     if S==[::-1]:
#         print("palindrome")
        
#     else:
#         print("Not palindrome")
        
# f3("madam")


#wap to create decorator which shouuld return positie valuue
#use abs()
# to get positive value

# def absnc):
#     def inner(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(start-end)
        
#     return inner
# @outer
# def f2(a,b):
#     print(a+b)
# f2(2,5)

# def outer(func):

#     def inner(a,b):
#         a=abs(a)
#         b=abs(b)
#         func(a,b)
        
#     return inner
# @outer
# def f2(a,b):
#     print(a+b)
    
# f2(-10,-50)


# def outer(func):
#     def inner(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return abs (result)
#     return inner

# @outer
# def f2(a,b):
#     return a+b
    
# print(f2(-10,-50))



# def outer(func):
#     def inner(*args,**kwargs):
#         print("login")
#         func(*args,**kwargs)
#         print("logout")
#     return inner

# @outer
# def func():
#     print("post")
# func()



# import time
# def outer(func):
#     def inner(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(end-start)   
#     return inner
# @outer
# def f2(a,b):
#     time.sleep(2)
#     print(a+b)
# f2(2,5)

#WAP to create a decorator which should going to positive value
# def outer(func):
#     def inner(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return abs (result)
#     return inner

# @outer
# def f2(a,b):
#     return a+b
    
# num1=int(input("enter your number 1:"))
# num2=int(input("enter your number 2:"))
# print(f2(num1,num2))


# d={}
# def func(*args,**kwargs):
#     fn=func.__name__
#     if fn not in d:
#         d[fn]=1
#     else:
#         d[fn]+=1
# func()
# print(d)

# d={}
# def outer(func):
#     def inner(*args,**kwargs):
#         func(*args,**kwargs)#function name covert into string
#         fn=func.__name__#int value pass as the string
#         if fn not in d:
#             d[fn]=1
#         else:
#             d[fn]+=1
#         print(d)
#     return inner
# @outer
# def add(a,b):
#     print(a+b)  
# add(1,3)
# add(1,4)
# add(1,5)
# # print(d)