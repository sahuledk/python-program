# program to show factors of a given number

a = int(input("enter the number"))
li = []

# iterating through 1 to input number
for i in range(1, a+1):
    # checking factors
    if a % i == 0:
        # if it is a factor, the value will be appended to list
        li.append(i)
print(f"factors of {a} are", li)
