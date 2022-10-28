# program to implement simple calculator
a = int(input(" enter your choice\n 1)addition\n 2)subtraction\n 3)multiplication\n 4)division"))

# defining addition function
def add(a, b):
    return a+b

# defining subtraction function
def sub(a, b):
    return a-b

# defining multiplication function
def mul(a, b):
    return a*b

# defining division function
def div(a, b):
    return a/b


match a:
    case 1:
        m = int(input("enter first  number"))
        n = int(input("enter second number"))
        c = add(m, n)
        print(c)
    case 2:
        m = int(input("enter first  number"))
        n = int(input("enter second number"))
        c = sub(m, n)
        print(c)
    case 3:
        m = int(input("enter first  number"))
        n = int(input("enter second number"))
        c = mul(m, n)
        print(c)
    case 4:
        m = int(input("enter first  number"))
        n = int(input("enter second number"))
        c = div(m, n)
        print(c)
