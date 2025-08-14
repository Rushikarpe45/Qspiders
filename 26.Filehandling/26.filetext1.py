# a=open("file1.txt","w+") #create the file using wirte operation 
# a.write("hi guys!!! we are learning file handling ")
# a.writelines(['\nGood Morning','\nGood Afternoon',"\nGood Evening","\nGood Night"])

# a.seek(0) #if my cursor is that position number start from the thats concept
# print(a.read())
# a.close()


# with open('file2.txt','w+') as fh:
#     fh.write('fantastic four')
#     fh.writelines(['\nGood Morning','\nGood Afternoon',
#                    '\nGood Evening','\nGood Night'])
#     fh.seek(0)#seek is using for indexing concept using
#     print(fh.readlines())    

# with open('file1.txt','r') as rh:
#     rh.seek(0)
#     print(rh.read())

# with open('Rushi.jpg','rb') as fh:
#     a=fh.read()
# with open('OIP1.jpg','wb') as photo:
#     photo.write(a)

#WAP to extract the number of word present in given text file
# with open('file1.txt', 'r') as file:
#     content = file.read()
#     words = content.split()
#     print("Number of words:", len(words))


# with open('file2.txt','w+') as fh:
#     fh.write('fantastic four')
#     fh.writelines(['\nGood Morning','\nGood Afternoon',
#                    '\nGood Evening','\nGood Night'])
#     fh.seek(10)#seek is using for indexing concept using
#     # print(fh.readlines()) 
#     a=fh.read()
#     l=a.split()
#     print(len(l))
    
    
# wap to extract the unique word from they string
# with open('file2.txt','w+') as fh:
#     fh.write('fantastic four')
#     fh.writelines(['\nGood Morning','\nGood Afternoon',
#                    '\nGood Evening','\nGood Night'])
#     fh.seek(10)#seek is using for indexing concept using
#     # print(fh.readlines()) 
#     a=fh.read()
#     l=a.split()
#     # print(set(l))
#     w=[]
#     for i in l:
#         if i not in w:
#             w.append(i)
#     print(w)
    


# wap to create a dictionary consists of  word with its count from they given text file
# with open('file2.txt','r') as fh:
#     fh.write('fantastic four')
#     fh.writelines(['\nGood Morning','\nGood Afternoon','\nGood Evening','\nGood Night'])
#     fh.seek(10)#seek is using for indexing concept using
#     # print(fh.readlines()) 
#     a=fh.read()
#     l=a.split()
#     d={}
#     for i in  l:
#         d[i]=l.count(i)
#     print(d)

#wap to consiste of oword which is repeatedd at list two time from they text file
        
# with open('file2.txt','w+') as fh:
#     fh.write('fantastic four')
#     fh.writelines(['\nGood Morning','\nGood Afternoon','\nGood Evening','\nGood Night'])
#     fh.seek(0)#seek is using for indexing concept using
#     # print(fh.readlines()) 
#     a=fh.read()
#     l=a.split()
#     b=[]
#     for i in l:
#         if l.count(i)>=2:
#             b.append(i)
#     print(b)
