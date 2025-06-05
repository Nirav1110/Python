#  
#python as a calculator
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
# can't start with number 1a 
#can start with _a
# a1 after string number can given 
 
# user_name_one = 123 #snake case writing (used in python)
# userNameOne = 'dkkd' #1st letter small (use in java)


# #string concate
# first_name = "nirav"
# last_name = "parmar"
# print(first_name + last_name) #cant do firstname + 3 (intger)
# print(first_name * 3) #prints 3 time

# how to tak a input from a user 

# a = input("Enter your name : ") #input function always takes string value from user
# print("hello " + a )

# number_one = int(input("Enter a first number  : ")) #int(input("enter")) <-takes input into integer 
# number_two = int(input("Enter a second number : "))
# total = number_one + number_two
# print("total is " + str(total)) 
#str converts number into string 4-->"4"
#int converts str into number "4"--> 4
#float converts number into float 4-->4.0 
#int and float could be + final output will be in float

# a = int(2)
# b = float(3)
# c = str("a")

# print(a+b) #int + float output will be float

#variable
# a,b = "a", "4"
# print("hello "+a +"what u said "+ b)

#two input
a,b=(input("enter your name and age ")).split()
print(a)
print(b)