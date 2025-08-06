##zip function
# user_id = ['user1','user2','user3']
# names = ['kanan','nirv','mihal']
# last_names = ['bhavsar','parmar','parmar']

# print(zip(user_id,names)) ###<zip object at 0x78626f427c00>
# print(list(zip(user_id,names))) ###[('user1', 'kanan'), ('user2', 'nirv'), ('user3', 'mihal')]

# ###if one list is shorter than it will stop zip from that
# user_id2 = ['u1','u2']
# print(list(zip(user_id2,user_id)))  ##[('u1', 'user1'), ('u2', 'user2')]
# print(list(zip(user_id,user_id2)))  ##[('user1', 'u1'), ('user2', 'u2')]
# print(dict(zip(user_id,user_id2)))  ##{'user1': 'u1', 'user2': 'u2'} we can directly convert it to the dictionary too
# print(list(zip(user_id,user_id2,last_names)))  ###we can take as many list want
# ####print(dict(zip(user_id,user_id2,last_names)))  ###gives error because we can only convert that kind of tuples which have two values

###---------------------------
###we can unpack list and make them seprate with zip
# li = [(1,2),(2,3),(3,4)]
# l1,l2 = list(zip(*li)) ##this will give tuple like this (1,2,3) (2,3,4)
# ###now convert it to the list
# print(list(l1),list(l2)) ####[1, 2, 3] [2, 3, 4]


####what else we can do with zip func
# l3 = [1,2,3,4]
# l4 = [5,6,7,8]
# new_list = [] ###here if we want to store from 1,5 which number is greater , like wise from 2,6 ....

# ####we can do this with list comprehension or any other method
# print([max(i) for i in zip(l3,l4)]) ##[5, 6, 7, 8]

# ##now do with loop
# for i in zip(l3,l4):
#     new_list.append(max(i))
# print(new_list) ##[5, 6, 7, 8]


###############-------------------------------practice
##exercise : define a func which take any no of lists containing number
###that function will return average
def average_finder(*args):
    average = []
    for i in zip(*args):
        average.append(sum(i) / len(i))
    return average


print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))  ###[4.0, 5.0, 6.0]

##now in one line with lambda
average_finder2 = lambda *args: [sum(i) / len(i) for i in zip(*args)]
print(average_finder2([1, 2, 3], [4, 5, 6], [7, 8, 9]))  ###[4.0, 5.0, 6.0]
