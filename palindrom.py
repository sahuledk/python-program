# program to check given string is palindrome

a = input("enter the string")

# check the revers of string and the string is equal
# if equal,it is palindrome
if a[::-1] == a:
    print("palindrome")
else:
    print("not palindrome")





