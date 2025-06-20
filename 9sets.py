##sets :
##unordered collection of unique items

# s = {1,2,3,4,1} ##1 every element should be unique 1 will be counted only 1 time //1 item shouldn't be more than once
# print(s) ##it will print 1 only 1 time : {1, 2, 3, 4}

##unordered collection means u can't do indexing in it
# print(s[1]) ##this will give error

##removing duplicate from list
# l = [1,23,3,2,2,3,1,1,1,5,5,6,6,7,7,7,7,7]
# s2 = list(set(l)) ##1st list will be converted into set and that set converted into list again which will have no duplicate elements
# print(s2) ##[1, 2, 3, 5, 6, 7, 23]


##set methods

##add method
s3 = {1,2,3}
s3.add(4)  ##4 will be added to the sets
# print(s3)

##remove method :if we try to remove somethid that doesnt exists in set it will give error
s3.remove(3) ##3 will be removed
# print(s3) 

##discard method : it also removes the elements but if element doesnt exist in set it will not give and error
s3.discard(9) 
# print(s3) ##print s as it's 


##clear method : it will clear the set
# s3.clear()
# print(s3) ##output : set()

##copy method : it will create copy of that set
s4 = {1,2,3,4,5,6}
s1 = s4.copy()
# print(s1)

##what u can store in the set :
##u can store integer,float,string 
##u can't store list or dictionarie into set
##it treats 1 and 1.0 as a same so it will print only 1

# ##in keyword in sets
# s5 = {'a','b','c',}

# if 'a' in s5 :
#     print("present")
# else : 
#     print("Not Present")

# ##for loop in sets 
# for item in s5:
#     print(item)

##math in set : union and intersection just like mathematics
s6 = {1,2,3,4}
s7 = {3,4,5,6}

##union : | pipe
print(s6 | s7) ##{1, 2, 3, 4, 5, 6}

##intersection 
print(s6 & s7) ##{3, 4}
