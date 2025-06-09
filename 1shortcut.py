##python as a calculator
# print(2+3)
# print(4/2) #float division 2.0 (use this)
# print(4//2) #integer division 2
# print(2//4) #integer division 0
# print(2**3) #find a power 8
# print(2**0.5) #gives under root because 1/2=0.5
# print(round(2**0.5),3) #rounds up till 3 after point
# print(3%2) #remainder value (modeulo) 1
# print((2+3)*2)
# print(2**3**2) #assosivity right to left 1st 3**2=9 than 2**9=512

# #variables
# a = 2 
# print(a)
# a = 5 #could be updated 
# print(a)

#naming rule
# #can't start with number 1a 
##can start with _a
# #a1 after string number can given 
 
# user_name_one = 123 #snake case writing (used in python)
# userNameOne = 'dkkd' #1st letter small (use in java)


# #string concate
# first_name = "nirav"
# last_name = "parmar"
# print(first_name + last_name) #cant do firstname + 3 (intger)
# print(first_name * 3) #prints 3 time

# #how to tak a input from a user 
# a = input("Enter your name : ") #input function always takes string value from user
# print("hello " + a )

# number_one = int(input("Enter a first number  : ")) #int(input("enter")) <-takes input into integer 
# number_two = int(input("Enter a second number : "))
# total = number_one + number_two
# print("total is " + str(total)) 
##str converts number into string 4-->"4"
##int converts str into number "4"--> 4
##float converts number into float 4-->4.0 
##int and float could be + final output will be in float

# a = int(2)
# b = float(3)
# c = str("a")

# print(a+b) #int + float output will be float

##variable
# a,b = "a", "4"
# print("hello "+a +"what u said "+ b)

##two input with split
# a,b=(input("enter your name and age ")).split(" ")
# print(a + b)
 
##formatting
# name = "lucifer"
# age = 4
# print("what's your {} and age {}".format(name,age))
# print(f"what's your {name} and age {age}")

# a,b,c = input("Enter number ").split(",")
# print(f"avera of three numbers is : {(int(a)+int(b)+int(3))/3}")

# # indexing
# lang = "python"
# print(lang[2]) #always use [] bractes for indexing
# print(lang[-2]) #negrative indexing starts from last and for that -1 is last character


# #slicing syntax lang[start argument : end argument]
# lang = "javascript"
# print(lang[1:4])
# print(lang[-4:-1])
# print(lang[:]) #prints full string
# print(lang[1:]) #print from index 1 to last index
# print(lang[:3]) #starts from 0 index and prints till 3rd index

##step arugument slicing
# print("Lucife"[0:4:2])
# print("hellowthere"[5::-1]) #prints reverse

##take input from use and print it reverse
# name = input("Enter your name : ")
# print(f"reverse of your name is : {name[::-1]}")

##print lenght of string len()
# print(len("Hei ")) #includes spaces too

# ##print string in lower case .lower()
# print(("LUCIFER IS MY NAME").lower())

# ##print string in upper case .upper()
# print(("hei there").upper())

# ##title() prints 1st character capital all other in small
# print(("how u doing").title()) #output : How U Doing

# ##count() counts how many times repeated ##count is case sensitive
# print(("hhhh how a person").count("h")) ##5 (output: h repeated 5 times)

##exercise #3
# name , char = input("Enter your name and single charcater : ").split(",")
# print(f"Lenght of name is : {len(name)} and the repeated count : {name.lower().count((char).lower())}")

# #strip() method
# name = "      Nirv      "
# dot = ".................."
# #lstrip() : removes space from left side only
# print(name.lstrip()+dot)
# #rstrip() : removes space from right side only
# print(name.rstrip()+dot)
# #strip() : removes space from both the sides
# print(name.strip()+dot)
# print(("hei                how").strip()) ##strip won't remove space from between
# #replace() 
# print(("hei                how").replace(" ",""))
# print(("hola how happy he's").replace("h","l"))

##replace() and find()
string = "is how is u doing today my boy with yourself   how how how"
# print(string.replace(" ","_"))
# print(string.replace("today","tomorrom"))
# print(string.replace("how","what",2)) #u can define how many of that u want to replace

##find() : to find index of any character or word from string
# print(string.find("how"))
# print(string.find("is",2)) #starts finding from index 2

##center() : to add a string 
name = "nirv"
print(name.center(6,"*")) #output *nirv*
surname = input("Enter yoour name here : ")
print((surname.center(len(surname)+4,"*")))