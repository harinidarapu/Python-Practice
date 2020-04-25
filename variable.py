# example for variable

# declaring a variable
# f=1
# print(f)

# re-declaring variable also works
f = 12345


# print(f)

# Adding different types of variable

# print("harini ID =" + str(40070983))

# Global vs local varibles in functions

def some_function():
    #global f # this f gets effects the outside(global f)
    f = "def"
    print(f)


some_function()
print(f)
del f
