# program to checking reminder
a = int(input("enter the first number"))
b = int(input("enter the second number"))

# checking reminder using function
def rem(a,b):
    return a % b


c = rem(a,b)
print(c)