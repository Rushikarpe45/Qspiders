# var=[i for i in range(1,11)]

# print(var)

# print([i for i in range(1,11)])

# Wap to insert the value in a list if it is a multiple of  3 in between 5-95

# print([i for  i in range(5,95) if i%3==0])


#Wap to extract string from they given list

# print([i for i in [1,2,'string'] if type(i)==str])

# out='programs  are  the  just fun rishii om'
# # out=['ps','are','jt','fun']
# # split function is use normal string into list form
# print([i[0]+i[-1] if len(i)%2==0 else i for i in out.split()])

# print([ len(i) for i in out.split()])


#out[('A',1),('A',2),('A'3),
# ('B',1),('B',2),('B',3)]

# print([(i,j) for i in ('A','B') for j in (1,2,3)])
# print([(i,j)  for  i in 'AB' for j in range(1,4)])

# s='we are learning comprehension'
# print([i if i in 'AEIOUaeiou'else 0 for i in s])

# print([i*10 if i%2==0 else i*0 for i in range(1,20)])

# print([i*10 if i%2==0 else i+10 for i in range(1,20)])

# print([i**i for i in range(1,11) if i%2==0])

#s='hi athereu'
# print([i for i in s if i in 'aeiouAEIOU'])

# print([i**i for i in range(1,11) if i%2==0])



#wap to find the square root of the interger value in between 1to50

# print({i**0.5 for i in range(1,51) })
#wap to exterct all they complex from they given set

# print({i for i in [1,2,3,4,0+5j,5+4j] if type(i)==complex})
#wap to get the following output
# input='data science for data analyst'
#out={data:DATA odd asel tar reverse}

# print({i.upper() if len(i)%2==0 else i[::-1] for i in input.split()})
#wap to to make each student opt(selection ) a every subject  every subject  from they given string
# student name={'chinchan','doremon','shizuka'}
# student_subject=['python','web tech','sql']

# print({(i,j) for i in ('Chinchan','doremon','shizuka') for j in ('python','webtech','sql')})


# dictionary

# Zip function is only take that perticular value those lenght is lessc

# l=[1,2,3,4,6]
# m=[1,2,3,4,5]
# n=[1,2,3,4,5]

# for i,j,k in zip(l,m,n):
#     print(i,j,k)


# print({i:i**2 for i in range(1,10)})

# Q='how  are you '
# print({i:len(i) for i in  Q.split()})
# print({len(i) for i in  Q.split()})


# Q='how are you python'
# out="python"="nothyp"
# print({i:i[::-1] for i in Q.split() if len(i)%2==0})

# Q='how are you python'
# out='how':'howwoh','python':'6' 'are':'areera'
# print({i:i+i[::-1] if len(i)%2!=0 else len(i) for i in Q.split()})


#USE OF THE ZIP FUNCTIONS
# l1=[1,2,3,4,5]
# l2=[11,22,55,44,66]
# print({i:j for i,j in zip(l1,l2)})

# l1=['a',96,35.5,56,[3,2]]
# l2=[10,20,30,40,50,60,70,80,90,100]
# # out={'a':10,'96':20,'35.5':30,'56':40}
# print({i:j for i,j in zip(l1,l2) if type(i)!=(list or tuple)})


# print({i:i**3 for i in range(1,11)})
