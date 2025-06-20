## *operator
## *args

# def total(a,b):
#     return a + b
####print(total(1,2,4,6)) ##here we want sum of 1+2 + 4+6 so we passed four arguments 
# ##but function only expects two arguments so it will give an error

## *(star) operator solves that problem
# def all_total(*args): ##it will take all arguments and will give the tuple//// * operator prints all arguments in tuple
#     print(args) ##(1, 2, 3, 4, 5, 67) ##this works does by * (in place of args we can write anything but we write args always acc to convection)
# all_total(1,2,3,4,5,67,)

##now sum of all arguments passed
# def total_all(*args):
#     total = 0
#     for i in args:
#         total+=i
#     return total
# print(total_all(1,2,3))


##------------------------>*args with normla parameters
# def mutiply(num,*args): ##u cant write normal parameter after the *args like this def mutilply(*args,num): cause the *args takes everything in tuple and there will nothing for num
#     print(num)
#     print(args)
#     mutiply = 1
#     for i in args:
#         mutiply*=i
#     return mutiply
# print(mutiply(4,1,2,3)) ##here 4 is num in function and after that everything will be in *arge (tuples)

##--------------------->how to use * as a argument
# def mutiply(*args):
#     mutiply = 1
#     for i in args:
#         mutiply*=i
#     return mutiply

# ##if u want to pass the list into this *args
# nums = [1,2,3]
# print(mutiply(nums)) ##this will be give only [1,2,3]
# print(mutiply(*nums)) ## * unpacks this nums list so now it will give 6 answer
##---* will also unpacks : list , tuple , set,string,range 


##------------>exercise : give one number and list or tuple return list which have that numbers power
##num, iterable(tuple,list) containing number as a args
# def to_power(num,*args):
#     if args : 
#         return [i ** num for i in args]
#     else :
#         return "Hei you didn't pass args"
# print(to_power(3,*list(range(1,11)))) ##it will print list of 1 to 10 numbers cube ... we can pass any number in num 



##----------------------------------->kwargs (full form : key word arguments)
## **kwargs (double star operator)

##----------------------------->kwargs as a parameter
# def func(**kwargs): ##** will gather all arguments as a dictionary 
#     ###########return {f"{i}:{j}" for i,j in kwargs.items()} ##this will become set not dictionarie
#     return {i:j for i,j in kwargs.items()} ##now this is the dictionarie

# print(func(first_name="nirav", last_name="Parmar"))

# ##unpack dictiona rie
# d = {'first name': 'kanan' , 'last_name':'bhavsar'}
# print(func(**d))



##-------------------------------------------------------------------->parameter order
##======(normal parameter,*args,default parameters,**kwargs)
# def fun2(normal,*args,default_age=24,**kwargs):
#     print(normal)
#     print(args)
#     print(default_age)
#     print(kwargs)
# fun2('nirav',1,2,3,name='kana',surname='bhavsar')



##----------->exercise : 
def capital_rev(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    return [name.title() for name in l]
names = ['nirav','kanna','roshni']
print(capital_rev(names, reverse_str =  False))
print(capital_rev(names, reverse_str =  True))