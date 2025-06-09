##while loop
# i = 1

# while i<=10 :
#     print(f"{i}")
#     i += 1

##sum 1 to 10 numbers
# total = 0
# while i<=10 :
#     total += i
#     i+=1   
# print(total)

##exercise 1 for while loop
# j = int(input("Enter a number : "))
# total = 0 
# while i<=j : 
#     total += i
#     i+=1
# print(f"Your total sum is {total}")

##exercise 2
# number = (input("Enter a digits"))
# total = 0 
# k = 0
# while k < len(number) :
#     total += int(number[k])
#     k+=1 
# print(total)
    

##exercise 3 . print which character is how many time is repeated
name = input("Enter your name : ")

i=0
temp_var = ""
while i< len(name) :
    if name[i].lower() not in temp_var:
        temp_var += name[i].lower()
        print(f"{name[i].lower()} : {name.lower().count(name[i].lower())}")
    i+=1
