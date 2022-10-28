# program to find sum of natural numbers
n = int(input("enter the limit"))
sum = 0

# find sum till limit
for i in range(1, n+1):
    sum = sum + i
print("sum up to {0} is {1}".format(n, sum))