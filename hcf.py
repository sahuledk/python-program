# program to find hcf of two numbers

a = int(input("enter the number"))
b = int(input("enter the second number"))

# checking smallest  number
if a > b:
    la = b
elif b > a:
    la = a
else:
    pass

# iterating till smallest
for i in range(1, la+1):
    # checking hcf
    if a % i == 0 and b % i == 0:
        hcf = i

print('the hcf is', hcf)
