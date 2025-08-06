##functions :


##enumerate function : this func we use with for loop
##we use it with for loop to track position of our item in iterable

##how to do without enumerate func :
# names = ["abc",'kanan','mihal']
# pos = 0
# for name in names:
#     print(f"{pos}----->{name}")
#     pos +=1

# ##with enumerate func :
# for pos,name in enumerate(names) :
#     print(f"{pos}----->{name}")

# ##----->exercise :
# def check_pos(name,l) :
#     for pos,item in enumerate(name):
#         if item == l:
#                 return (f"{item} is at {pos} position in names")
#     return -1

# print(check_pos(names,"mihal"))
# print(check_pos(names,"nirv"))
##----------------------------------------


##----------------------------------------map function :
##--
# numbers = [1,2,3,4,5,6]
# # def square(a) : ##in this u have to pass one element at a time
# #     return a**2
# ##with map
# # print(map(square,numbers)) ##u dont have to write () ; output : <map object at 0x760dafbf0130>
# # print(list(map(square,numbers))) ##to print it we have to store it in tuple or list right
# ##shortest version with lambda version
# print(list(map(lambda a:a**2,numbers)))
# ##3we could have done this with list comprehension also
# print([a**2 for a in numbers])
# ##all three gives same output : [1, 4, 9, 16, 25, 36] //same also we can do with for loop also
##we can only iterate only one time threw map fun
###-----------------------------------------------------------------------------------


##----------------------------------------filter function :
# numbers1 = [3,4,2,5,6,7,1,8,9,10]
# evens = filter(lambda a:a%2==0,numbers1)
# print(evens)        ###----output : <filter object at 0x79c11fa34130>
# # print(list(evens)) ##[4, 2, 6, 8, 10] we store it in list or tuple
# ##if we dont want to store it in list we can run loop over it
# # for i in evens :
# #     print(i) ##we can iterate only one time threw filter fun
# # for i in evens :
# #     print(i) ##this wont get print second time because we have already iterate it above
# ##if we store it like this : evens = list(filter(lambda a:a%2==0,numbers1)) we can iterate this as much as we want cause this became a list

# ##with list comprehension
# print([i for i in numbers1 if i%2==0])

###-----------------------------------------------------------------------------------
