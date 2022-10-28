# program to find lcm

a = int(input("enter the first number"))
b = int(input("enter the first number"))

# find smallest and largest
if a > b:
    g, li = a, b
elif b > a:
    g, li = b, a
else:
    pass

# iterate till multiple of two numbers and check lcm
for i in range(g, (li*g)+1):
    if (i % li) == 0 and (i % g) == 0:
        print(f"lcm of {li} and {g} is ", i)
        break
