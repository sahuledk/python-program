# program to print multiplication table

# take the input value from user
a = int(input("enter the number"))

# printing multiplication table
for i in range(1, a):
    b = a * i
    print("{0} * {1} = {2}".format(i, a, b))
    if i > 9:
        break
