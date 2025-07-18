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
# class Laptop2 :
#     def __init__(self,name,price,model):
#         ####instance variables
#         self.name = name
#         self.price = price
#         self.model = model
#         self.combine = name  + ' ' + model
#     def discount(self,num):
#         return self.price*num - self.price*(num/100)

# l6 = Laptop2('lenovo',50000,'yoga')
# print(l6.discount(10))

##-----------------------class variables: 
# class Circle :
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def cacl_circumference(self):
#         return 2*Circle.pi*self.radius

# c = Circle(4)
# c1 = Circle(5)

# print(c.cacl_circumference())


# class Laptop3 :
#     discounts = 10 
#     def __init__(self,name,price,model):
#         ####instance variables
#         self.name = name
#         self.price = price
#         self.model = model
#         self.combine = name  + ' ' + model
#     def discount(self):
#         ####here if we write Laptop3.discounts than if we change discounts ##l6.discounts = 50## value it wont apply it will use only intial value that's 10
#         return self.price*self.discounts - self.price*(self.discounts/100)

# l6 = Laptop3('lenovo',10000,'yoga')
# l6.discounts = 50
# print(l6.__dict__)
# print(l6.discount())

###############-----exercise : 
# class Person2 :
#     count_instance = 0 
#     def __init__(self,first_name):
#         Person2.count_instance += 1
#         self.first_name = first_name

# p3 = Person2('name')
# p4 = Person2('123')
# p5 = Person2('wi')
# print(Person2.count_instance)


####----------------diffrence between class methods and instance methods
class Person3 :
    count_instance = 0 ##class variables/ class attribute
    def __init__(self,first_name,last_name,age): ##init method is a constructor
        Person3.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age= age

    @classmethod
    def from_string(cls,string):
        first,last,age =  string.split(',')
        return cls(first,last,age)
         
    @classmethod ###decorator from python
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"
         
    def full_name(self): ##instance method
        return f"{self.first_name} {self.last_name}"

    def is_adult(self): ##instance method 
        return self.age > 18

p3 = Person3('nirv','parmar',22)
p4 = Person3('mihal','parmar',2)
# print(Person3.count_instances())
p10 = Person3.from_string('rajshree,bhavsaar,23')
print(p10.full_name())
