# find largest among three numbers

a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))

# checking largest among first and second number
if a > b:
    # checking largest among first and third number
    if a > c:
        # display first number if it is largest
        print("{0} is largest".format(a))
    else:
        # display third number if it is largest
        print("{0} is largest ".format(c))

# checking largest among first and second number
if b > a:
    # checking largest among second and third number
    if b > c:
        # display first number if it is largest
        print("{0} is largest".format(b))
    else:
        # display third number if it is largest
        print("{0} is largest".format(c))

