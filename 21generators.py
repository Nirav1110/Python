###generators :
##generators are iterators
######Iterable = A book 📖 (you can read it from the start)
######Iterator = A bookmark 🔖 (it remembers where you are in the book)
import time


##iterator , iterable
# l = [1,2,3,4] ##iterable : something you can loop over // it has data like list,string,tuple,set,dict etc...
####But it doesn't remember where it is during iteration.

###for i in l:
###   print(i)
# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for i in map(lambda a:a**2,l): ##it's already a iterator
#     print(i)

##genrator is also sequence
# 
# #####write 1st generator with generator function 
##1.)generator function 
##2.)generator comprehension


# def nums(n):
#     for i in range(1,n+1):
#         yield i ###yield is a keyword to write generators
# # print(nums(10)) ###<generator object nums at 0x758deaeb1b60>
# for numbers in nums(10): ####our demand is in this loop
#     print(numbers)
# ##memory -------->1 than 1 removes and 2 comes at a time only store one single : means in a memory at a time only one number
# ###next number will be generated when we demand it and our demand is in for loop 

# ###we tried again but it wont print anything because memory got clear 
# for numbers in nums(10): 
#     print(numbers)

###because we store it 
##############---------------------exercise : generate sequence of even numbers
# def even_generator(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i 

# for i in even_generator(20): ##we can write this loop again and it will generator again because we're generating direclty in loop but if we 
#     ####done this even = even_generator(20) than on even we can run loop only one time 
#     print(i)

##############--------------------------------------------------------------------------

##############------------------Generator comprehension :
# square = (i**2 for i in range(1,11))
# print(square) ###<generator object <genexpr> at 0x7a192256a0c0>
# for i in square :
#     print(i)

#### it's compeletely like list comprehension u just have to remove square brackets and put ()
##############--------------------------------------------------------------------------

##############------------------list vs generator :
# t1 = time.time()
# l  = [i**2 for i in range(10000000)] ##10 million
# print(time.time()-t1)

t1 = time.time()
g = (i**2 for i in range(10000000))    ##10 million
print(time.time()-t1)
