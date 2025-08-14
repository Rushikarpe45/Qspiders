import csv
# with open('file1.csv','w') as fh:
#     a=csv.writer(fh)
#     a.writerow(['name','sal','id'])
#     a.writerows([['Rushikesh',2300,45],['Krishna',6800,54],['Pratik',3400,2]])
    
# with open('file1.csv','r') as rfh:
#     b=csv.reader(rfh)
#     for i in b:
#         if i!=[]:
#             print(i)
    
#proper structure is madatory to display output is show other wise it show objct address
# with open('file1.csv','r') as rfh:
#     b=csv.reader(rfh)
    # next(b)
    # a=rfh.seek(0)
    # for i in b:
        # if i!=['name','sal','id'] and i!=[]:
        # if i=a and i!=[]: using range function
            # print(i)
    # for i in b:
    #     if i[0]!=i:
    #         print(i)
                
    # for i in b:
    #     if i!=[] and i==0:
    #         if int(i[1])>=2500:
    #             print(i)

# with open('file2.csv','w') as fh:
#     a=csv.writer(fh)
#     a.writerow(['name','sal','id'])
#     a.writerows([
#         ['Rushikesh',2300,45],
#         ['RKrishna',6800,54],
#         ['Aratik',3400,2]])

    
# with open('file2.csv','r') as rfh:
#     b=csv.reader(rfh)
#     next(b)
#     print(list(b))
    
#     for i in b:
#         if i!=[] and  i==0:
#             if str(i[0])=='A':
#                 print(list(i))