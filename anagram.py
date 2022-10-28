# program to find whether the string is anagram

# taking two string inputs
a = input("enter the first string")
b = input("enter the second string")

# check the length of two strings is equal
if len(a) == len(b):
    # sorting two string
    a = sorted(a)
    b = sorted(b)
    # check two string are equal
    # if equal, it is anagram
    if a == b:
        print("anagram")
    else:
        print("not anagram")
else:
    print("not anagram")

