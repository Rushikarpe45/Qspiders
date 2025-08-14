# def  add(*args):
#     print(args)
#     sum_int=0
#     for i in args:
#         sum_int+=i
#     print(sum_int)
# add(1,2,4,6,7)


# def details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:-{value}")
# details(name='rushi',email='karperushikesh42@gmail.com',phn_no='7972833455',location='Chhatrapati Sambhajinagar')


# def print_details(*args,**kwargs):
#     print('single Packaging,',args)
#     print('double Packaging,',kwargs)
# print_details(1,2,3,4,5,name='rushi',phn_no='7972833455')



#Write a function find max that takes any number of numbers using argument and return the maximum


# def max_no(*args):
#     maximum=args[0]
#     for i in args:
#         if i > maximum:
#             maximum=i
#     print(maximum)
# max_no(10,20,30,40)
        

# find_max(1,2,3)
#write a function descibes person that takes name and any number keyword detakes and print them nicell


# def name_(username,**kwargs):
#     p={'username':username}
#     # for key,value in kwargs.items():
#     #     p[key]=value
#     # print(p)
#     p.update(kwargs)
#     print(P)s
# name_('rushi',loc='Chhatrapati Sambhajinagar',hobby='vollyball')


#unpacking
# numbers=[1,2,3,]
# def add(a,b,c):
#     print(a+b+c)
# add(*numbers)

# d={'name':'rushi','loc':'chhatrapati Sambhajinagar'}
# def details(name,loc):
#     print(f"this smily boy name is {name} and he is living in{loc}')
#     print(d)
# details(**d)



# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(1,2,3,4,5)


# def add(args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(1,2,3,4)


# var=(1,2,3)
# def add(a,b,c):
#     print(a+b+c)
# add(*var)

#unpacking questions
# var=(1,2,3)
# def add(a,b,c):
#     print(a+b+c)
# add(*var)