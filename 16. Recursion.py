#extract  lowercase and uppercase letter from given string
# def extract_low(n,out='',i=0):
#     if i>=len(n):
#         return out
#     if 'a'<=n[i]<='z':
#         out+=n[i]
#     return extract_low(n,out,i=i+1)
# print(extract_low('GooD Morning'))

# def extract_low(n,out='',i=0):
#     if i>=len(n):
#         return out
#     if 'a'<=n[i]<='z':
#         out+=n[i]
#     return extract_low(n,out,i=i+1)
# print(extract_low('GooD Morning'))


#write to calculate length of the string

# def len_count(n,sum=0,i=0):
#     if i>=len(n):
#         return sum
#     if i<=len(n):
#         sum+=1
#     return len_count(n,sum,i=i+1)
# print(len_count('GooD MOrning'))

#program to find the sum of all the interger present in a given list


# def sum_int(n,sum=0,i=0):
#     if i>=len(n):
#         return sum
#     if type(n[i])==int:
#         sum+=n[i]
#     return sum_int(n,sum,i=i+1)
# print(sum_int([10,'rushi','ketan',20]))

#WAP l=[10,20,'ant','local',5.5]
# output=[10,20,'tnant','lacollocal',5.5)

# def output_len(n,l=[],i=0):
#     if i==len(n):
#         return l
#     if type(n[i])==int or type(n[i])==float:
#         l.append(n[i])
#     if type(n[i])==str:
#         reversed_str=n[i][::-1]
#         l.append(reversed_str+n[i])
#     return output_len(n,l,i=i+1)
# print(output_len([10,20,'ant','local',5.5]))


# input['hai',45,2+4j,'bye']
# output['iahhai','eybbye']

# def sam(s,out=[],i=0):
#     if i>=len(s):
#         return out
#     if type(s[i])==str:
#         out.append(s[i][::-1]+s[i])
#     return sam(s,out,i+1)
# print(sam(eval(input("enter your list:"))))


#TO EXTRACT INT WHICH ARE MULTIPLE OF 5 AND 3 using recursion
# def rushi(s,out=[],i=0):
#     if i>=len(s):
#         return out
#     if type(s[i])==int:
#         if s[i]%5==0 or s[i]%3==0:
#             out.append(s[i])
#     return rushi(s,out,i+1)
# print(rushi(eval(input("enter your list:"))))


# TO REMOVE DUPLICATE FROM THE LIST WITHOUT TYPECASTING
# a=eval(input("enter the list: "))
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# def Dupli(s,out=[],i=0):
#     if i>=len(s):
#         return out
#     if s[i] not in out:
#         out.append(s[i])
#     return Dupli(s,out,i+1)
# print(Dupli(eval(input("enter your list:"))))

#factorical of the number using recursion

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         result=n*fact(n-1)
#         return result
# print(fact(3))

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         result=n*fact(n-1)
#         return result
# print(fact(3))
# print(fact(4))

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(4))

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(4))


# def fibo(n,a=0,b=1):
#     # if n==0 or n==1:
#     if n<=1:
#         return n
#     return fibo(n-1)+fibo(n-2)
# for i in range(6):
#     print(fibo(i),end=" ")

#to check the give number is prime or not using recursion 
# def prime(n,i=2):
#     if i==n:
#         return n,'prime number'
#     if n%i==0:
#         return n,'not a prime number'
#     return prime(n,i+1)
    
# print(prime(int(input("enter your number:"))))



#extract voewl using 

# def fun(s,out='',i=0):
#     if i==len(s):
#         return out
#     if s[i] in 'AEIOUaeiou':
#         out+=s[i]
#     return fun(s,out,i+1)
# print(fun("this is recursion"))