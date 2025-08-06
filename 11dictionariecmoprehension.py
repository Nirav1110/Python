##Dictionarie comprehension
# square = {i:i**2 for i in range(1,11)}
# print(square)
# print({f"square of {i} : {i**2}" for i in range(1,11)})

##------------------------------------------------------------------------------------------------------
##count string is how many times
# string = "NiravvvVVVV"
# print({char:{string.count(char)} for char in string})
##------------------------------------------------------------------------------------------------------
##if else statement : if number even mutiply by 2 and if odd number negative
# print({i:(i*2  if i%2==0 else -i) for i in range(1,11)})


##--------------------------------------------------set comprehension
##we use set comprehension less
print({i**2 for i in range(1, 11)})
print({i[0] for i in ["kanan", "nirav", "mihal", "dixant"]})
