# print fibonacci series up to n terms

a, b = 0, 1

# taking limit from user
limit = int(input("enter the number of terms"))

# iterating up to n terms
for i in range(limit):
    print(a)
    # swapping values and adding
    a, b = b, b+a

