#####-----closure

##basics
# def square(a):
#     return a**2
# s = square ###u can write it like this also and use s() like this
# print(s(7))

##-------------how pass function as argument
###map function also takes function as a argument
####print(list(map(square,[1,2,3,4,5]))) like this square is function
####----making our own function that takes another function as a argument
# def my_map(func, l):
#     new_list = []
#     for item in l :
#         new_list.append(func(item))
#     return new_list
# print(my_map(square,[1,2,3,4]))
# print(my_map(lambda a: a**3,[1,2,3,4])) ###passed lambda function as a function

####----------------how to return function from function
# def outer_func():
#     def inner_func():
#         print('inside inner func')
#     return inner_func
# var = outer_func() ###still inner function isn't called it's only outer_func ----currently var is inner_func than we have to call it
# var() ###executed inner function

# def outer_func2(msg):
#     def inner_func2():
#         print(f"message is {msg }")
#     return inner_func2
#     # return inner_func2()  ####we can directly return this function too
# var1 = outer_func2('hei this is the kanan')
# var1()


#### function returning function we call it closure also or first class function


#########------ practie
def to_power(x):
    def calc_power(n):
        return n**x

    return calc_power


cube = to_power(3)
print(cube(5))
quadrent = to_power(4)
print(quadrent(2))
