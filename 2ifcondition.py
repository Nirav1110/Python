##if condition 
# age = int(input("Enter your age: "))

# if age >= 18 :
#     print("You're eligible to play a game")

# ##pass statement 
# if age <= 50 :
#     pass    #checks the statement but write pass if u dont want to write anything in conditon 
# ##else statement
# else: #else statement wont be alone it always written with else
#     print("you are minor")

import random
##game exercise
winning_number = random.randint(1,10)
guess_number = int(input("Guess the number between 1 to 10 : ")) 
if guess_number == winning_number : 
    print("You won the game")
else : #nested if else 
    if  guess_number > winning_number: 
        print("To High")
    else : 
        print("To low")

##and or operator
# name = 'nirv'
# age = 18
# if name == 'nirv' and age == 18 : #only true if both true ##or : true if both true and also true if one of them is true 
#     print(True)
# else : 
#     print(False)

##exercis : watch coco
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# if (name[0] == "a" or name[0]=="A")  and age >= 10 : 
#     print("You can watch the movie")
# else : 
#     print("You can't watch a movie")

##if elif statemment
##ex : show ticket price
# age = int(input("Enter your age : "))
# if 0<age<=3 :
#     print("Entry is Free") 
# elif 3 < age <=10 :
#     print("You have to pay 150rs")
# elif  10 < age <=60 :
#     print("You have to pay 250rs")
# elif age<=0:
#     print("Get Born First")
# else: 
#     print("200")

##in keyword in if condn
# name = input("Enter your name : ")
# present = input("Enter a character u want to check ")
# if present.lower() in name.lower() : 
#     print("Yes presents")
# else : 
#     print("Not present")

# ##empty or not 
# name = input("Enter your name : ")
# if name == "":
#     print("Empty")
# else :
#     print(f"Your Name is {name}")