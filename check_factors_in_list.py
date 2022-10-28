# program to check given number is a factor of a number in the list

# take the  number which have to be checked
d = (int(input("enter the number")))

# create a list
li = [1, 4, 5, 7, 9, 11]

# check the number is divisible
lis = filter(lambda x: x % d == 0, li)
print(list(lis))
