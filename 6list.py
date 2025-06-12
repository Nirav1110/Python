##list is a data structures
##ordered collection of items
##you can store anything in lists float,int,string
##we create list using [] square brackets

# number = [1,2,3,4]
# print(number)
# print(number[2]) ##for accessing individual elements
# 
# words = ["Hei","how","you","doing","today?",]
# print(words) 
# print(words[:3]) ##slicing same as a string slicing
# 
# mixed = ["hei",12,7.8,None,0] ##None and 0 are diffrent 
# print(mixed)
# 
# mixed[1]="lucifer" ##for changing value of individual index 1 is index here it will change 12 to "lucifer"
# print(mixed)
# 
# mixed[1:]="nirv" ##it will change mixed as like this ['hei', 'n', 'i', 'r', 'v'] if we give it bigger "niravparmar" output : ['hei', 'n', 'i', 'r', 'v', 'p', 'a', 'r', 'm', 'a', 'r']
# print(mixed)
# 
# mixed[1:]=["luci",11,"clori",99.99,"oggy"] ##output : ['hei', 'luci', 11, 'clori', 99.99, 'oggy']
# print(mixed)
#

##how to add items to our list  
fruits = ['mango','grasps']
# fruits.append('watermellon') ##append method adds items at the last of the list
# print(fruits)

# ##other methods to add data
# ##insert method to add item at anywhere  
# fruits.insert(1,'apple') ##it will be added at index 1
# print(fruits)

# ##how to concate two lists
# fruits1 = ["pineapple",'banana']
# # fruits2 = fruits+=fruits1 
# # print(fruits2)

# ##extend method
# fruits.extend(fruits1) ##all fruits1 will be added into the fruits list
# print(fruits)
# print(fruits1)

# fruits.append(fruits1) ##['mango', 'apple', 'grasps', 'watermellon', 'pineapple', 'banana', ['pineapple', 'banana']] ##adds list into list
# print(fruits)

##to delete data from list
vegetables = ["bhindi",'baigan','gobi','cabbage','gobi', "dhaniya",'phuding','kiwi']
# vegetables.pop() ##removes last element from list if not passed index
# vegetables.pop(1) ##it will remove element of index 1
# print(vegetables)

##delete operato or statement but it doesnt matter
##del 
# del vegetables[0] ##removes index 0 element 
# print(vegetables)

##remove method
# vegetables.remove('dhaniya') ##dhaniya will be removed
# vegetables.remove('gobi') ##removes only 1 gobi
# print(vegetables)

# ##check if any element exists in our list 
# if 'grasps' in vegetables :
#     print('present')
# else :
#     print('not present')


##more methods in list
# print(vegetables.count('gobi'))

##sort method
vegetables.sort() ##sorts in alphabetical order like a,b,c,d
# print(vegetables) ##this sort method sorts our original list

number = [13,12,223,0.4,25]
# number.sort()
# print(number)

##sorted function 
# print(sorted(number)) ##only print in sorted but doesnt change our original list

##clear() ##empty's our list
# number.clear()
# print(number) ##output : []

##copy()
# number2 = number.copy()
# print(number2)


##is vs equal
##compare lists we use == , is keyword
# veg1 = ["bhindi",'baigan','gobi']
# veg2 = ["bhindi",'baigan','gobi']
# print(vegetables==fruits) ## == checks only values are same 
# print(veg1==veg2)

# print(veg1 is veg2) ##is checks if both are at same place in our  memory 

##split() : converts string into list
#  
##join() : converts list into string
# f = ['n','i','r','v'] ##cant join this [1,'pirav','lover'] //[0,11,1,2] integer
# print(','.join(f)) ##n,i,r,v
 
##loops in list 
# fruits =  ['hei', 'luci', 11, 'clori', 99.99, 'oggy']
# for i in fruits : 
#     print(i)

# ##while loop
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

##list inside list
matrix = [[1,2,3],[4,5,6],[7,8,9]] ##2d list

##for loop print full matrix
# for i in matrix :
#     for f in i :
#         print(f)

# print(matrix[2][2])
# string = "hellow"
# print(type(matrix) ,type(string)) ##prints type of matrix and string

##generate list with range function
# num = list(range(1,11)) ##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(num)

##more about pop method
# poped_num = num.pop() ##it will store 10 into this ##we can reuse it again
# print(num) ##[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(poped_num) ##10 

##index method
# print(num.index(2)) ##here 2 is not index it's element of num list and index method will print it's index position

##pass list into function 
# def negative_list(l):
#     negative = []
#     for i in l :
#         negative.append(-i)
#     return negative

# print(negative_list(num)) ##[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]





num = list(range(1,11)) ##here list is pythons built in type 
##Exercise 1
# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i*i) ##or u can do i**2  exponetial **
#     return square

# print(square_list(num))

##exercise 2 : reverse the list but not with slicing and without using reverse method 
# def reverse_list(l):
#     ulta = []
#     for i in range(len(l)):
#         f = l.pop()
#         ulta.append(f)
#     return ulta
# okay = [1,2,3,4,5,6,7,8,9,10]
# print(reverse_list(okay))

# ##with reverse method 
# def r_method(l):
#     l.reverse()
#     return l
# print(r_method(num))

# ##with slicing
# def r_slice(l):
#     l[::-1]
#     return l
# print(r_slice(num))


##exercise 3 : every string should be reversed like : ['abc','dfg','Hei'] reverser--> ['cba','gfd','ieH']
# def reverse_every(string):
#     rev = []
#     for i in string:
#         rev.append(i[::-1])
#     return rev  
# string = ['abc','dfg','Hei']
# print(reverse_every(string))

##ex4:  take a list divide them into odd and even numbers 
# def odd_even(l):
#     odd = [] 
#     even = []
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else :
#             odd.append(i)    
#     output = [odd,even]
#     return output

# inpit = [1,2,3,4,5,6,7,8,9,10]
# print(odd_even(inpit))

##ex5: take two list as input and return a new list in which only commone number from both list
# num1 = [1,2,5,8]
# num2 = [1,2,7,6]
# def common_fun(n1,n2):
#     output = []
#     for i in n1:
#         if i in n2:
#             output.append(i )
#     return output
# print(common_fun(num1,num2))  


##min and max function 
# n3 = [2,333,3,4,33,1,23]
# print(max(n3)) ##prints maximum number
# print(min(n3)) ##prints minimum number

# def max_min(l) :
#     return max(l)-min(l)
# print(max_min(n3))


##exercise 6: make a function our input have how many list inside it
okay = [1,2,3,[1,2],['word'," "]] 

def list_count(l):
    count = 0
    for i in okay:
        if type (i) == list :
            count +=1
    return count
print(list_count(okay))