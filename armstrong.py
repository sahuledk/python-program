a = int(input("enter the number"))
s = 0
m = a
while m >= 1:
    d = m % 10
    m = int(m / 10)
    s = s + d ** 3
    if s == a:
        print("{0} is an armstrong number".format(a))
        c = 0
    else:
        c = 1

if c == 1:
    print("it is not an armstrong number")