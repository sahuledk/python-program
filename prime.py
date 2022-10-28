# checking whether the number is prime

# Taking a number as input
p = int(input("enter the number"))

# checking the number is greater than 1
if p > 1:
    for f in range(2,p):
        # checking whether the number have factors
        if p % f == 0:
            # display the number and it's factor
            print("{0} has a factor {1} so it is not a prime number".format(p, f))
            # break the loop
            break
    # display the number is prime
    else:
        print("{0} is a prime number".format(p))
# checking other values and displays not prime
else:
    print("it is not a prime number")





