##list comprehension
##--------------------------------------------------------------------------------------------------
##with the list help of list comprehension we can create list in one line
##create a list of squares from 1 to 10
##normal method
# squares = []
# for i in range(1,11 ):
#     squares.append(i**2)
# print(squares)
##comprehension method in one line
# squares2 = [i**2 for i in range(1,11)] ##this is called comprehension
# print(squares2)
##--------------------------------------------------------------------------------------------------

# ##print negative numbers
# negative = [-i for i in range(1,11)]
# print(negative)
##--------------------------------------------------------------------------------------------------
##print 1st letter
# names = ['Nirav','Mohit','Kanan','Rohit']
# ##normal way
# #
# ##exercise : make a function that reverse every element of that list
# def reverse_string(l):
#     return [i[::-1] for i in l]

# print(reverse_string(names))
# ##--------------------------------------------------------------------------------------------------

##list comprehension with if statement :
# numbers = list(range(1,11))
# print(numbers)

##print even nums from this list
##-------------------->noraml long method
# nums = []
# for i in numbers :
#     if i%2==0 :
#         nums.append(i)
# print(nums)

##-------------------->comperehension method to print even numbers with if statement
# even_nums = [i for i in range(1,11) if i%2==0] ##direct using range and print even number
# odd_nums = [i for i in range(1,11) if i%2!=0] ##direct using range and print odd number
# print(even_nums)
# print(odd_nums)
# ##-------------------------------------------------------------------------------------------------------------------
##--------------------->exercise : make a function which only prints int or float type
# def int_float(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]
# print(int_float([1,2,{"name":"nirav"},[1,2,3],1.0,2.0,True,False]))
# ##-------------------------------------------------------------------------------------------------------------------
##---------->if else statement in comprehension
##if numer is odd print it's negative and if it's even mutiple it with 2
##----------++++++>normal method
# new_list = []
# for i in range(1,11):
#     if i%2==0 :
#         new_list.append(i*2)
#     else :
#         new_list.append(-i)
# print(new_list)

##----------++++++>comprehension method : with if else statement
# print([ i*2 if i%2==0  else -i for i in range(1,11)])
# ##-------------------------------------------------------------------------------------------------------------------
##------------------->list comprehension in nested list
example = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]  ##create list like this with list comprehension
print([[i for i in range(1, 4)] for j in range(3)])
