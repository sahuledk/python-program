# program to check whether the number is positive negative or zero.

# Taking input value
a = int(input("enter the number"))


if a > 0:     # checking the value greater than zero
    print(f'{a} is positive')
elif a < 0:   # checking the value less than zero
    print("{0} is negative".format(a))
else:         # checking the value is zero
    print("number is zero")