# program to find factorial of a number
# Factorial of a number is the sum of multiplication of all the integers smaller than that positive integer

# Taking input values value from user
a = int(input("enter the number"))
p = 1
for i in range(1, a ):
    # finding factorial of a number
    p = a*i
print("The factorial of {0} is {1}".format(a, p))
