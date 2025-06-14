##tupl data structure
##tuple can store any data type
##tuples are immutable, once tuple is created can't be updated

example = ('hei','kanan','by')
##no appened ,no insert,no pop ,no remove
##when we know that our data is not going to change in that case we use tuple like
days = ('monday','tuesday','saturday')
##tuples performance is faster than list that's why we use tuple when our data is not going to change

##mehods
##count
# print(days.count('monday'))
# print(days[1]) ##index
# print(len(days)) ##for printing length

# print(example[::1])

##example[0]=1  we cant update tuple values like this 

##looping in tuple
mixed = (1,'two',0.3,'kanan')

# for i in mixed:
#     print(i)

##while loop
# i=0
# while i < len(mixed):
#     print(mixed[i])
#     i+=1
    
##tuple with one element
# nums = (1) ##this isnt tuple
# words = ('word1') ## this is also not tuple 
# print(type(nums))
# print(type(words))
# ##for one elment tuple
# n = (2,) ##u have to put , 
# word1 = ('nirv',) ##u have to put ,
# print(type(n))
# print(type(word1))

##tuples without parenthesis ()
# n1 = 'hei','kanan','how'
# print(type(n1))

##tuple unpacking
# guitarists = ('Maneli jamal','Andrew joy','eddie van der meer')
# ##take variable as much element in tuple
# g1,g2,g3 = (guitarists)
# print(g1)

##list inside tuples
# favorites = ('sunny',['natasha','maalkova','briana beach']) ##in this tuples there's a list inside it ... with that list we can do anything we can do with list
# favorites[1].pop() ##('sunny', ['natasha', 'ana de arms'])
# favorites[1].append("we made it angela") ##('sunny', ['natasha', 'maalkova', 'we made it angela'])
# print(favorites)


##min max in tuples
# t = (22,33,11,45,8,21)
# print(min(t))
# print(max(t))
##sum 
# print(sum(t))

##function returing two values
# def fun(int1,int2):
#     add = int1 + int2
#     multiply = int1*int2
#     return add,multiply ##it will return tuple (add,mutiply)

# print(fun(2,3))

##something more about tuples,list,str

nums = tuple(range(1,11)) ##this will create a tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(nums)

##tuple to list 
tup1 = list(nums) ##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
str2 = str(tup1) ## this will convert list into string
print(tup1)
print(str2,type(str2)) ##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'str'>

str1 = str(nums)
print(str1 , type(str1))    ##(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) <class 'str'>


##summary 
##functions in tuples
##min(),max(),len(),sum()
##in tuple we can store any data type
##in tuple we cant do append,extend,pop,insert, no remove 
##only count and index
##we use tuple when we know we're not gonna change values  ##for example days = ('monday','tuesday')
##tuples are faster than list
##we dont make list in tuples cause that affects the performace of that tuple
