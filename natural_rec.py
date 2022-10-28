# program to find sum of natural numbers using recursion
a = int(input("enter the limit"))

# initialise a function
def rec(a):
    # checking in case of zero or negative value
    if a < 1:
        print("please enter valid input")
    # checking in case value is 1
    elif a == 1:
        return a
    else:
        # find sum using recursion
        return(a+rec(a-1))

print(rec(a))



