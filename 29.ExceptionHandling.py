#exception Handling
# 1)sepecifi Exception handling
# 2) Gerneric Exception Handling
# 3) Default Exception Handling

# # 1)sepecific Exception handling

# try:
#     a=int(input('enter your number: '))
#     b=int(input('enter your number: '))
#     print(a/b)
# except ZeroDivisionError: #those name give to except because of this error are thrown as time of the 
#     print('The Value for b can not be zero')

# except ValueError:
#     print('The both value should be interger')

# ctrl+c to throw the keyboard interrupt
# major drakback of generic exception handling thats it cannot handle keyword interrrupt 
#2 generic Exception Handling
# try:
#     a=int(input('enter the numbers1: '))
#     b=int(input('enter your number2:'))
#     print(a/b)
#     for i in range(1,1000):
#         print(i)

# except Exception as var:
#     print('The error is handled')
#     print(var)

#Default Exception Handling
# ctrl+c to throw the keyboard interrupt
# try:
#     for i in range(1,1000):
#         print(i)
    
# except:
#     print('The Error is handled')


# try:
#     a=int(input("enter your number:"))
#     b=int(input("enter your number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print('The b value should no tbe 0')
# except ValueError:
#     print("The value should be int")
# except:
#     print("the error is handled")


# try:
#     for  i in range(1,10000):
#         print(i)
        
# except:
#     print('the error is handled')
# else:
#     print('the loop is completed')
# finally:
#     print('Hurreay') 
    
    
# n=int(input('enter the number: '))
# if n<0:
#     raise TypeError ('The shopping cart value can not be in negative')
# else:
#     print('the number has been added')


#userdefind 

# class ValueCanNotBeZero(Exception):
#     pass

# n=int(input("enter the number:"))
# if n<0:
#     raise  ValueCanNotBeZero('The shopping cart value can not be in negative')

# else:
#     print('the number has been added',n)


# a='hello'
# b=[1,2,3,4]
# assert type(a)==type(b),'the type of a and b is different'
# print(a+b)

# a=[1,2,3,4]
# b=[1,2,3,4]
# assert type(a)==type(b),'the type of a and b is different'
# print(a+b)



