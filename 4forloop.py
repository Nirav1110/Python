##for loops
##we use range function in for loop
# for i in range(10) :
#     print(f"hello: {i}")

##to give a range
# for i in range(2,10):
#     print(i)

##sum of n numbers
# total = 0
# n = int(input("Enter your numbe: "))
# for i in range(1, n+1):
#     total += i
# print(total)

##sum of digits in string
# number = (input("Enter a digits "))
# total = 0
# for i in range(len(number)) :
#     total += int(number[i])
# print(total)

##check the repeated number
# name = input("Enter your name ")
# total = ""
# for i in range( len(name)) :
#     if name[i] not in total :
#         print(f"{name[i]} : {name.count(name[i])}")
#         total += name[i]


# ##break and continue keyword
# for i in range(1,11):
#     if i==5 :
#         break
#     print(i)

# #continue
# for i in range(1,11):
#     if i == 5 :
#         continue
#     print(i)

##number game guess
# import random
# guess = 1
# game_over = False
# winning_number = random.randint(1,100)

# while not game_over :
#     number = int(input("Guess the number between 1 to 100 : "))
#     if number == winning_number :
#         print(f"You won the game you guessed it in {guess} times")
#         game_over = True
#     else :
#         if winning_number>number:
#             print("too low")
#         else  :
#             print("too high")
#     guess =+1
#     continue


##step arugument
# for i in range(1,10,2) : ##there will be gap of two : 1,3,5,7,9
#     print(i)

##reverse number
# for i in range(10,0,-1) : ##output 10,9,8,7,6,5,4,3,2,1
#     print(i)

##for loop & stringg
# for i in "lucifer":
#     print(i)

##sum "12345" short method
number = input("Enter a number : ")
total = 0
for i in number:
    total += int(i)
print("this i the shortest method", total)
