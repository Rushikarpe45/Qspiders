import csv

# with open("employee.csv",'w') as emp:
#     a=csv.writer(emp)
#     a.writerow(['name','sal','id','Dname','Did'])
#     a.writerows([['Rushikesh',2300,45,'HR',101],
#                 ['Krishna',6800,54,'Marteting',102],
#                 ['Pratik',3400,2,'Sales',103],
#                 ['Mahesh',5000,3,'HR',104],
#                 ['Pankaj',6000,4,'HR',105],
#                 ['Ketan',7000,5,'Marketing',106],
#                 ['Rahul',6000,6,'Manager',107],
#                 ['Lalit',5000,7,'HR',108],
#                 ['Manoj',4000,8,'HR',109],
#                 ['Om',50,'Sales',9,110]])
    
# with open('employee.csv','r') as fhs:
#     a=csv.reader(fhs)
#     next(a) #skip the header file
#     for i in a:
#         if i!=[]:
#             print(i)
    
# 🔹 Basic Questions:
# Print only employee names.
# with open('employee.csv','r') as fhs:
#     a=csv.reader(fhs)
#     next(a) #skip the header file
#     for i in a:
#         if i!=[]:
#             print((i[0]))
            

# Count how many employees are in the "HR" department.
# with open('employee.csv','r') as fhs:
#     a=csv.reader(fhs)
#     next(a) #skip the header file
#     for i in a:
#         if i!=[]:
#             if i[3]=='HR':
#                 print((i))
# Print all employee details whose salary > 5000.

# with open('employee.csv','r') as fhs:
#     a=csv.reader(fhs)
#     next(a) #skip the header file
#     for i in a:
#         if i!=[]:
#             if int(i[1])>=5000:
#                 print(i)

# Find the total salary of all employees.

# with open('employee.csv','r') as fhs:
#     a=csv.reader(fhs)
#     next(a) #skip the header file
#     total=0
#     for i in a:
#         if i!=[]:
#             if int(i[1])==int(i[1]):
#                 total+=int(i[1])
#                 # print(total)
#     print("Total salary is:", total)


# Print employee names and their departments.


# with open('employee.csv','r') as fhs:
#     a=csv.reader(fhs)
#     next(a) #skip the header file
    
#     for i in a:
#         if i!=[]:
#             # if str(i[0]) and int(i[3]):
#                 # if i!=int(i[1]) and str(i[2]) and str(i[4]):
#                     print(i[0] ,'-',i[3])

