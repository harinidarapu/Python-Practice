# Funcitons

# Defining simple funtions
def func1():
    print("This is a Funtion")

# functions with arguments
def func2(arg1,arg2):
    print(arg1," ",arg2)
# function with return value
def func3(x):
    return x+x+x
# function with default value as argument
def power (num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
# function with variable no of arguments
def mutli_add(*arg):
    result = 0
    for a in arg:
        result = result+a
    return result

# Defining a functione
### calling the function
#func1()
#print(func1()) #  the print value returns "none" because the function doesnt return any value
#print(func1) # it prints the vaule at which the func is, kind of addresss
#func2(1,2)
#print(func2(1,2))
#print(func3(2))
#print(power(2))
#print(power(2,3))
#print(power(x=3,num=2)) # i can reverse the order it will take correct as long as o give correct variable
print(mutli_add(1,2,3))