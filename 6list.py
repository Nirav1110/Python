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
# fruits = ['mango','grasps']
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
