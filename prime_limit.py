# Program to find prime numbers in an interval

# taking two interval values from user
p = int(input("enter the lower limit"))
n = int(input("enter the upper limit"))

print("prime numbers between {0},{1} are".format(p, n))

for i in range(p, n+1):
    # checking the limit greater than 1 up to upper limit
    if i > 1:
        for j in range(2, i):
            # checking the value have any factor
            if i % j == 0:
                # break the loop
                break
        else:
            # display the prime number
            print(i)













# if p ==1:
#     print("1 is not a prime number")
# elif p ==2:
#     print("1 is not a prime number")
#     print("2 is not a prime number")
# else:
#     print("1 is not a prime number")
#     print("2 is not a prime number")
#     for i in range(3, p + 1):
#         for f in range(2, i):
#             if i % f == 0:
#                 print("{0} is not a prime number".format(i))
#                 break
#         else:
#             print("{0} is a prime number".format(i))

