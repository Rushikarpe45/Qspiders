# Functional Programing

# Write a program to check the given number is even or not
# n=int(input('Enter the number:'))
# even=lambda n:n%2==0
# print(even(n))

# Write a program to check the given number is odd or not

# n=int(input('Enter the number:'))
# even=lambda n:n%2!=0
# print(even(n))

#write a program to check whether given string is starting with vowel or not

# n=input("enter your name:")
# check=lambda n:n[0] in ['aeiouAEIOU']
# print(check(n))

#check whether given element in list or not

# r=[10,20,30,40,50,60,70]
# n=int(input("Enter your number:"))
# check=lambda n:n in r
# print(check(n))

#add number

# n=int(input("enter your number:"))
# r=int(input("enter your number:"))
# add=lambda n,r:n+r
# print(add(n,r))


#map 

# n=int(input("enter the number:"))
# even =lambda n:'even' if n%2==0 else 'odd'
# print(even(n))


#write a program to return n+10 if it is multiple of 5 else return n-10

# n=int(input("enter your number:"))
# multiple=lambda n:'n+10' if n%5==0 else 'n-10'
# print(multiple(n))

#write a progema to check whether a given string is palindrome or not if it is palindrome print the string else return the reverse string 

# n=input("enter your String:")
# palindrome=lambda n: if n[::-1]==n else n[::-1]
# print(palindrome(n))

#write a program  add minimum 2 number and maximum  5 number

# a=int(input("enter your number 1:"))
# b=int(input("enter your number2:"))
# total=lambda a,b,c=0,d=0,e=0:a+b+c+d+e
# print(total(a,b,c,d))




#write a program to return the concatenated list if both have same len else return the first list

# li1=[10,20,30,40]
# li2=[20,30,40,50]
# concat=lambda li1,li2:li1+li2 if len(li1)==len(li2) else li1
# print(concat(li1,li2))


#filter function

# sqr=lambda n:n**2
# sqr_gen=map(sqr,range(1,11))u
# print(list(sqr_gen))

##### we can same code executed as single line approach
# print(list(map(lambda n:n**2,range(1,11))))

#write the get the following output
# l=['abcd','nayan','python','car']
# # out=[4,5,6,3]
# print(list(map(lambda l:len(l),l)))
# l=['abcd','nayan','python','car']
# r=lambda l:len(l)
# len_gen=map(r,l)
# print(list(len_gen))

#write a program to find the factorial of all the interger present in the 

# t=(4,5,6,3)
# def fact(n):
#     if n==0 or  n==1:
#         return 1
#     return n*fact(n-1)
# print(tuple(map(fact,t)))


#write a program to find
# pow=lambda n:n**n
# pow_scq=map(pow,range(1,11))
# print(list(pow_scq))

# n=int(input("enter your number:"))
# print(list(map(lambda n:n**n,range(1,n+1))))


# even=lambda n:n%2==0
# print(even(10))
# even=lambda i:'even' if i%2==0 else 'odd'
# print(even(10))


#wap to check the given string last element is  consonent or not
# s=input("enter your number:")
# vow=lambda s:s[-1] not in 'aeiouAEIOU'
# print(vow(s))


# wap to print square of the number if it is odd number else it is cube of the numbers

# s=int(input("enter your number:"))
# squ=lambda s:s**2 if s%2!=0 else s**3
# print(squ(s))


#wap to check the addition of minimum 2 number and maximum 6 number
# a=int(input("enter your number 1:"))
# b=int(input("enter your number2:"))
# total=lambda a,b,c=0,d=0,e=0,f=0:a+b+c+d+e+f
# print(total(a,b,c,d))



# print(tuple(map(lambda n:n**2,range(1,11))))


#wap to print the factorial of each number form they tuple

# t=(1,5,6,4,3)
# def fact(n):
#     if  n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(tuple(map(fact,t)))

#wap to get the following output
# s='hey how are you'
# out=['hy','hw','ae','yu']

# s='hey how are you'
# print(list(map(lambda s:len(s[0]+len(s[-1])),s)))

# print(list(map(lambda s:s[0]+s[-1],s.split())))

# def string(s):
#     return s[0]+s[-1]
# print(list(map(string,s.split())))


#wap to print number and its cube from 1to 5 in the form dictionary

# out={1:1,2:8,3:27,4:64,5:125}
# n=[1,2,3,4,5]
# a=lambda n:(n,n**3) #key value pair
# b=map(a,n)
# print(dict(b))


# s='program on map function'
#out={'program':'margorp','on':'on','map':'pam','function':'function'}
# print(dict(map(lambda s:(s,s[::-1] if len(s)%2!=0 else s),s.split())))


# s='program on map function'
# fname=lambda s:(s,s[::-1] if len(s)%2!=0 else s)
# var(map(fname,s.split()))
# print(dict(var))

#filter question
# fname=lambda n:n%2!=0
# var=filter(fname,range(50,101))
# print(list(var))
                
                
                
#wap to extract all they  str data item from they tuple only it is starting with lower case and ending with upper case

# string=('Digit','ihR','Rushi')
# a=lambda n:type(n)==str and 'a'<=n[0]<='z' and 'A'<=n[-1]<='Z'
# b=filter(a,string)
# print(list(b))
#wap to extract all collection value present inside the list which has even length


#wap to find the square all they even number from they given list
# l = [1, 2, 4, 5, 8, 5]
# print(list(map(lambda l:l**2 , l%2==0)))

# even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, l)))

#wap to extrcat all the prime numbers 2 to 10



# n=int(input("enter your number:"))
# rev=0
# while n!=0:
#     k=k%10
#     rev=rev*10+k
#     n=n//10
# print(rev)

# n=input("enter your number:")
# out=""
# i=0

# while i<len(n):
#     if not('A'<=s[i]<='Z' or 'a'<=s[i]'z','0'<=s[i]<='9'):
        
#  Write a program to get the following output.
# s='good day'
# #  Output={'good':4, 'day':3}

# out={}
# for i in s.split():
#     out[i]=len[i]
# print(out)
