##dictionaries intro
##-we use it because limitation of lists,lists are not enough to represent real data.
##dictionari : unordered collection of data in key : value pair.

 
##how to create dictionaries
# dic = { 'name' : 'nirv' , 'age' : 22}
# print(dic)
# print(type(dic))


# ##second way of creating didctionarie
# user1 = dict(name = 'kanan', age = 22)
# print(user1)

# ##imp : how to access your data in dictionarie
# ##Note : there's no indexing in dictionaries 
# print(user1['name']) ##this way we can access data ;output : kanan
# print(user1['age'])


##what we can store in dictionarie
##we can store anything -numbers,strings,list,dictionarie,
# user_info = {
#     'name' : 'Mihal', 
#     'age'  : 4,
#     'fav_movies' : ['365 days','iron man','thor']    
# }
# print(user_info['fav_movies'])

# users = {
#     'user1' : {
#         'name' : 'nirv',
#         'age' : 22
#     },
#     'user2' : {
#         'name' : 'kanan',
#         'age' : 22
#     },   
# }
# print(users)

##how to add data in empty dictionarie
# user_info2 = {'love':'nolove'}
# user_info2['name'] = 'rohit'
# user_info2['age'] = 24
# print(user_info2)

##in keyword and iteration in dictionarie
# if 'love' in user_info2 :
#     print('present')
# else : 
#     print('not present ')

# ##check if particular value exist 
# if 'rohit' in user_info2.values() :
#     print('value present')
# else : 
#     print('value not present ')


##loops in dictionarie
# for i in user_info2 : ##it will print all key of user_info2
#     print(i)

# for i in user_info2.values(): ##it will print values 
#     print(i)

##values method
# v1 = user_info2.values()
# print(v1, type(v1))
# ##keys method
# k1 = user_info2.keys()
# print(k1, type(k1))

##items method:
# user_items = user_info2.items()
# print(user_items, type(user_items)) ##dict_items([('love', 'nolove'), ('name', 'rohit'), ('age', 24)]) <class 'dict_items'>


# for i,j in user_info2.items() :
#     print(f"the key is {i} and it's value is {j}")

##add and delete data 
# user_info2['fav_songs'] = ['song1','song2']
# user_info2['singers'] = ['uravashi','shreya','aishwarya','love quin']
# print(user_info2)

##pop method : in pop u have to pass atleast one argument u cant keep it empty like list 
# popped_item = user_info2.pop('singers')  ##['uravashi', 'shreya', 'aishwarya', 'love quin']
# print(user_info2) ##singers removed : {'love': 'nolove', 'name': 'rohit', 'age': 24, 'fav_songs': ['song1', 'song2']}
# print(f"Popped items : {popped_item}")

##pop item method : for randomly delete any 
# popitem_method = user_info2.popitem()
# print(f"randomly popped any item : {popitem_method}")

##update method  
# more_info = {
#     'name': 'kanan', ##both user_info2 and more_info have key name but when we update it user_info2 name rohit will become kanan
#     'state': 'gujarat',
#     'hobbies': ['gaming','cooking','guitar']
# }

# user_info2.update(more_info)
# print(user_info2)


##fromkeys method : to give all key same value like 'unknown' or anything else like this: {'name':'unknown','age':'unknown'}
# d = dict.fromkeys(['name','age','height'],'unknown') ##here we have written list we can write it in tuples also ('name','age','height')
# c = dict.fromkeys("abc",'unknown') ##here it will become three keyys a , b , c
# f = dict.fromkeys(range(1,11),'unknown') ##1 to 11 key will have 'unknown' value
# print(d)
# print(c)
# print(f)


##get method:
# print(d.get('name'))
# print(d.get('male')) ##it wont give error it will return None

##clear : it will clear the dictionary
# f.clear()
# print(f) ##{} 

##copy method
# d1 = d.copy()
# print(d1)


##more about get method :
# u1 = {'name': 'kanan', 'age': 27,'age':21}
# print(u1.get('fav','Not found fav!')) ##now it will return: Not found fav!
# print(u1) ##age value will be overwritten it will be 21


##exercise : print a cube of given n numbers in dictionarie
# def cube(num):
#     k = {}
#     for i in range(1,num+1):
#         k[i] = i ** 3 
#     return k

# n3 = int(input("Enter a number : "))

# print(cube(n3))

##program word counter :
# def word_count(name):
#     k = {}
#     for i in name:
#        k[i] = name.count(i)
#     return k

# name = input("Enter your name : ")
# print(word_count(name))


##exercise : ask user his name,age,fav_movies , fav_songs 
user = {}

name = input("Enter your name : ") 
age = input("Enter your age : ") 
fav_movies = input("Enter your fav movies seprated by coma : ").split(",")
fav_songs = input("Enter your fav songs seprated by coma : ").split(",") 

user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs

for key,value in user.items():
    print(f"{key}:{value}")


