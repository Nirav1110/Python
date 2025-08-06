#####-------------decorators
### enhance the functionality of other functions
### @ use for decorator
from functools import wraps
import time  ## time module

# def decorator_function(any_function): ####(we can give any name to this function) we give it this name just for understanding purpose
#     def wrapper_function():
#         print('This function is awesome')
#         any_function()
#     return wrapper_function


# def func1():
#     print('This is function 1')

# def func2():
#     print('This is function 2')

# var = decorator_function(func2) ####instead of var u can write anything we want like func1 , or anything else
# var()

# @decorator_function ###with @ we also use decorator functions : shortcut @:syntactic sugar
# def func3():
#     print('This is function 3')
# func3()

#### if we pass any argument in this func3(7) now it will give error function because decoratorfunction doesn't expects any argument so now to solve it we use *args and **kwargs
# def d2(any_function_with_arguments):
#     def wrapper_accepts_arg(*args, **kwargs):
#          print("this function accepts argument and kwargs")
#          return any_function_with_arguments(*args, **kwargs) ###we have to return this function so it can do a+b in add5
#     return wrapper_accepts_arg

# @d2
# def func4(a):
#     print(f"This function of d2 {a}")
# func4(1)

# @d2
# def add5(a,b):
#     return a + b
# print(add5(10,20))

# ####this still have problem if we print name of add5
# print(add5.__name__) ###wrapper_accepts_arg it should print add5

##so now to solve this problem we import one module


# def d3(function_wraps):
#     @wraps(function_wraps)
#     def wrapper_accepts_arg(*args, **kwargs):
#          print("This function use wraps which will give it's orginal function name")
#          return function_wraps(*args, **kwargs)
#     return wrapper_accepts_arg

# @d3
# def func6(a,b):
#     return a+b
# print(func6.__name__) ##func6 now it will print correctly


###practice :
##function name : print function data
# def print_function_data(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         print(f"You are calling this {function.__name__} function")
#         print(f"{function.__doc__}")
#         return function(*args,**kwargs)
#     return wrapper

# @print_function_data
# def addition(a,b):
#     '''This function takes two numbers as argument and return their sum'''
#     return a + b
# print(addition(4,5))


###########-----------exercise : calculate time
# def calculate_time(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"Executing........  {func.__name__} function")
#         t1 = time.time()
#         returnerd_value = func(*args,**kwargs)
#         t2 = time.time()
#         totol_time = t2 -t1
#         print(f"This {func.__name__} took {totol_time} seconds")
#         return returnerd_value
#     return wrapper

# @calculate_time
# def square_finder(n):
#     return [i**2 for i in range(1, n + 1)]

# print(square_finder(10))
####-----------------------------------------------------------------------------------------------------------------

#####-------------practice : 2
# def only_int_allowed(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         if all([type(i) == int for i in args]):
#             return func(*args,**kwargs)
#         else :
#             return "Invalid args"
#     return wrapper


# @only_int_allowed
# def add_all(*args):
#     return sum(args)
# print(add_all(1,3,4,5,6))
# print(add_all(1, 2.5, 3))
####-----------------------------------------------------------------------------------------------------------------
#####-------------decorators with arguments
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(i) == data_type for i in args]):
                return function(*args, **kwargs)
            return f"only this {data_type} is allowed"

        return wrapper

    return decorator


@only_data_type_allow(str)
def string_join(*args):
    string = ""
    for i in args:
        string += i
    return string


print(string_join("hhei", "helow", "how", 2))
