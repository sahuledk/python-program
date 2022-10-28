# print fibonacci series up to a limit

a = int(input("enter the number of terms"))

# initialising a function to print fibonacci
def fibrec(a):
    # checking the number less than 1
    if a <= 1:
        return a
    else:
        # if terms greater than 1 recursively use function
       return (fibrec(a-1)+fibrec(a-2))

# iterate through loops to print fibonacci series
for i in range(a):
       print(fibrec(i))

fibrec(a)


