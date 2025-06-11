##funciton 

# def add_two(a,b):
#     return a+b
# print(add_two(3,4))

##odd even function
# def odd_even(num):
#     if num%2==0:
#         return "number is even"    
#     return "number is odd"

# print(odd_even(int(input("Enter your number "))))

##print last character of string 
# def last_char(name):
#     return name[-1]
# print(last_char(input("Enter your name : ")))

##make a funtion which says which num is greater and lower
# def greater_lower(n1,n2):
#     if n1 > n2 :
#         return n1
#     elif n1 == n2 :
#       return "Both are same number" 
#     return n2
# n1 = int(input("Enter a first number : "))
# n2 = int(input("Enter a second number : "))
# print(f"the greate number is : {greater_lower(n1,n2)}")

##defin greates number from three numbers
# def three_greater(n1,n2,n3):
#     if n1 >= n2 and n1>=n3 :
#         return n1
#     elif n2 >= n3 and n2>=n1:
#         return n2
#     return n3

# a = int(input("Enter 1st number"))
# b = int(input("Enter 2nd number"))
# c = int(input("Enter 3rd number"))

# print(f"{three_greater(a,b,c)} is greatest number")

##exercise make function that checks given string is pelindrom or not
# def check_pelindrom(n) :
#     if n == n[::-1]:
#         return "Pelindrom"
#     return "Not a pelindrom"
# name = input("Enter your string ")
# print(check_pelindrom(name))

##fibonacci series (some of last two numbers mean fibonacci)
##0 1 1 2 3 5 8 13 21 34
# def fibonacci_seq(n):
#     a = 0
#     b = 1 
#     if n == 1 :
#         print(a)
#     elif n == 2 :
#         print(a , b)
#     else : 
#         print(a , b  , end = " " )
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c 
#             print(b, end=" ")

# fibonacci_seq(10)

##default parameter
##in function u can only make a last parameter default 
## which means u cant do this def function(name="nirav",surname,age)
##you can make all parameters default def function(name="lucifer",surname="parmar",age=22)
# def funciton(name,surname,age=22):
#     print(name, surname, age)
# funciton("nirav","parmar")

##variable scope
# def fun():
#     x = 7 ##this function x is only used in this fun cant use in another fun
#     return 7
# def fun2():
#     print(x) ## this cant be happen ##eror  will come

##u can do this
# y = 7
# def fun():
#     global y ##to change global variables value but we won't be doing this 
#     y = 10
