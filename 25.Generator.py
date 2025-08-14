#Generator using yield and return keyword
# def num_seq():
#     for i in range(1,11):
#         yield i
# print(list(num_seq()))


# def num_seq():
#     for i in range(1,51):
#         yield i*2
# print(list(num_seq()))


# wap to extract all they string form list collection if it is palindrome
# l=["mam","madam","rushi",45,85,55,55]
# def squ():
#     for  i in l:
#         if type(i)==str and i==i[::-1]:
#             yield i
# print(list(squ()))

# def fu():
#     for i in range(1,11):
#         yield i
        
# print(list(fu()))


#WAP To extract all the string  from they list collection only if it is even length

# l=["mam","madam","rushi","Rush"]
# def squ():
#     for  i in l:
#         if len(i)%2==0 :
#             yield i
# print(list(squ()))

# out={'A':65,'B':66,'C':67,'D':65 -------------- 'Z':90}


# out = {chr(i): i for i in range(65, 91)}

# def alpha_seq():
#     for i in range(65,91):
#             yield( chr(i),i)
# print(dict(alpha_seq()))

# def cube():
#     for i in range(1,11):
#         yield (i,i**3)
# print(dict(cube()))

#write a program all to extract alll prime number between 3 m to n

# m=int(input("enter your number:"))
# n=int(input("enter your number:"))
# def prime(m,n):
#     for i in range(m,n+1):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             yield i
#         # else:
#         #     print("not prime")   
# print(tuple(prime(m,n)))

# def prime_sq(m,n):
#     for i in range(m,n+1):
#         if prime(i)==True:
#             yield i
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return false 
#         return True
# print(list(prime_sq(50,101)))

#fibonacci series using generator

# def fibonacci(a=0,b=1):
#     for i in range(0,10):
#         yield a
#         a,b=b,a+b
# print(tuple(fibonacci()))

#to get following output 
# s='GeneRAT@r2'
# # out={'G':'g','e':'E','n':'N','@':'@','2':'2'}
# def out():
#     for i in s:
#         if  'A'<=i<='Z':
#             yield (i,chr(ord(i)+32))
            
#         elif 'a'<=i<'z':
#             yield(i,chr(ord(i)-32))
        
#         else:
#             yield(i,i)
# print(dict(out()))
