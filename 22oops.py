##oop is just a way/style to write code
###oop : object oriented programming
##class, object(instance),method
##class: it's a blue print in which we decide that how will be our upcoming object
##in python everything is object


# class Person : ###acc to convection u should keep class 1st letter capital it's not rule u can write in small letter to
#     def __init__(self, first_name,last_name,age): ###by default we pass 1st argument in init is self(self represents our object)(in place of self u can write any name but acc to convection write self)
#         ##instance variables 
#         print('init method / constructor get called')
#         self.first_name = first_name
#         self.last_name= last_name
#         self.age = age

# p1 = Person('kanan','bhavsar',22)
# # p2 = Person('mihal','parmar',3)

# print(p1.first_name)

##############---------------------------------exercise : make a class of laptop
# class Laptop :
#     def __init__(self,name,price,model):
#         self.name = name
#         self.price = price
#         self.model = model
#         self.combine = name  + ' ' + model

# l1 = Laptop('lenovo',50000,'yoga')
# print(l1.name)
# print(l1.combine)

##################-------------------------------------instance method
# class Person1 :
#     def __init__(self,first_name,last_name,age) : ##init is also a method we call it constructor also
#         self.first_name = first_name
#         self.last_name= last_name
#         self.age = age

#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'

# p3 = Person1('kanu','raaji',22)
# print(p3.full_name())
# print(Person1.full_name(p3)) ##this and above are same  

####---------we can write like this below also methods of list class
# l3 = [1,2,3]
# list.append(l3,10)
# print(l3)

########################-------------------------------exercise:
class Laptop2 :
    def __init__(self,name,price,model):
        self.name = name
        self.price = price
        self.model = model
        self.combine = name  + ' ' + model
    def discount(self,num):
        return self.price*num - self.price*(num/100)

l6 = Laptop2('lenovo',50000,'yoga')
print(l6.discount(10))