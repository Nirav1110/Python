##any and all function
n1 = [2, 4, 6, 8, 10]
n2 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(all(i%2==0 for i in n1)) ##all checks if all values True
# print(all(i%2==0 for i in n2)) ##false n2 all values aren't even

####any if any is true
# print(any(i%2==0 for i in n1)) ##True
# print(any(i%2==0 for i in n2)) ##True


###practice :
##exercise:
def my_sum(*args):
    total = 0
    if all(type(arg) == float or type(arg) == int for arg in args):
        for i in args:
            total += i
        return total
    else:
        return "wrong input"


print(my_sum(1, 2, 3, 4, 5, 1, "jkddkfd"))
