##lambda expression :
###or we can call it anonymous funtion :

##function which we write in one line

# def add(a,b):
#     return a+b

# ##same funtion we can make with lambda
# add2 = lambda a,b : a+b
# print(add2(2,3))

# ##we dont store lambda funtion into any variable this is for understanding purpose only
# ##we direclyy use it in built in functions like map,reduce,filter

# mutiply = lambda a,b: a*b

# ####to prove lambda is anonymous function
# print(mutiply(2,3))
# print(add)  ##<function add at 0x7fec1f54e340> //this just gives where that function is stored at
# print(add2)  ## <function <lambda> at 0x7fec1f100cc0> //it just gives function as lambda
# print(mutiply) ##<function <lambda> at 0x7fec1f101da0>


##------------------practice:
# def is_even(a):
##now same function with lambda function
# is_even2 = lambda a : a%2==0  ##this way we can create in single line with lambda
# print(is_even2(2))
# print(is_even2(3))


##print last char of given string
# last_char = lambda  a:a[-1]
# print(last_char("kanan"))

# ##print reverse string
# reverse_str = lambda a:a[::-1]
# print(reverse_str("Kanan"))

##----------------------using if else condition with lambda
func = lambda a: (
    True if len(a) > 5 else False
)  ##this is just for understading how we can write if else with lambda
func2 = (
    lambda a: len(a) > 5
)  ###we can write above directly like this buut above is just for understaing how to write if else
