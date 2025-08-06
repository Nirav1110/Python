##min and max functio advance

##basic usage learned before
# num = [1,2,32,4,5]
# print(max(num),min(num))

# names = ["Nirav",'mihl','kandarap','ab']
##### print(max(names))  ##it gives 'mihl' but we want max based on it's length
##based on legth of string decide which one is max or min
# print(max(names,key=lambda item:len(item)))
# print(min(names,key=lambda item:len(item)))

#####------------------------------------------->
# students2 = [
#     {'name':'nirv','score':90,'age':22},
#     {'name':'kanan','score':99,'age':23},
#     {'name':'mihal','score':89,'age':4},
# ]

# print(max(students2,key=lambda item:item.get('score'))) ####{'name': 'kanan', 'score': 99, 'age': 23}
# print(max(students2,key=lambda item:item.get('score'))['name']) ####kanan : print name of student who have max score
# print(min(students2,key=lambda item:item.get('score'))['name']) ####mihal : print name of student who have min score

#####------------------------------------------->
# students1 = {
#     'harshit': {'score':89,'age':24},
#     'mihal': {'score':67,'age':14},
#     'kanan': {'score':63,'age':24},
# }

# print(max(students1,key=lambda item:students1[item]['score'])) ##harshit
# print(min(students1,key=lambda item:students1[item]['score'])) ##kanan


### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++sort method advanced :
####-----list sort
# fruits = ['graps','mango','apple','finger']
# fruits.sort()
# print(fruits) ##gives sorted list : ['apple', 'finger', 'graps', 'mango']

# ####-----tuple sort
# fruits2 = ('graps','mango','apple','finger')
# print(sorted(fruits2)) ###this returns list : ['apple', 'finger', 'graps', 'mango']
# print(fruits2) ###('graps','mango','apple','finger') because tuples are immutable

# ####-----sets sort
# fruits3 = {'graps','mango','apple','finger'}
# print(sorted(fruits3)) ##same gives list


####--------------sort complex list or dictionary
# guitarist = [
#     {'model':'yamaha f30','price':2000},
#     {'model':'honda a30','price':1000},
#     {'model':'pleasure','price':5000},
#     {'model':'kia','price':8400},
# ]
# ##---sort based on price
# print(sorted(guitarist,key= lambda d : d['price']))
# print(sorted(guitarist,key= lambda d : d['price'], reverse = True)) ##it will be print in decreasing order of price because of reverse = True

###################3####################################################################################
##------------------more about functions
###----what are doc strings
##how to write it
##how to see doctstring
##what is help function

# def add(a,b):
#     '''This the function of add two numbers'''
#     return a+b

# print(add(1,2))
# print(add.__doc__) ###how to see doctstring
##it helps us to know what our function does
###len , sum , max , min , sorted
# print(len.__doc__)
# print(sum.__doc__)
# print(max.__doc__)
# print(min.__doc__)
# print(sorted.__doc__)

######---- help() : in bracket function name it will tell what that function does
#### print(help(sum))
