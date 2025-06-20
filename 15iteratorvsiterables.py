##------------iterator vs iterables :
numbers3 = [1,2,3,4]   ##tuples,list,string-----iterables
squares3 = map(lambda i:i**2,numbers3)  ##-----iterator
# print(squares3)

# ###for i in numbers3:
#    ### print(i)]

##-----------------now iterables
##step call iter function
##iter(numbers3) ---> iterator
##next(iter(numbers3)) :---> it will give 1st time 1st element , 2nd time 2nd element ,3rd time 3rd element
# number_itr = iter(numbers3) ##we made it iterator 
# print(iter(numbers3))  ####----<list_iterator object at 0x79d5625c04f0>: iter is also a object
# print(next(number_itr))  ##1
# print(next(number_itr))  ##2
# print(next(number_itr))  ##3
# print(next(number_itr))  ##4
# print(next(number_itr))  ##this will give error of StopIteration

##-----------------now iterator
##we can dirctly run loop on squares3 (iterator) ##it gives directly iterator
print(next(squares3))   ##1
print(next(squares3))   ##4
print(next(squares3))   ##9
print(next(squares3))   ##16
# print(next(squares3)) ##this will give error
