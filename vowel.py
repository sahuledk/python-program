# program to find number of vowels in a word

a = input("enter the string")

# initialise count variable
count_of_a = 0
count_of_e = 0
count_of_i = 0
count_of_o = 0
count_of_u = 0

# iterating through each alphabet
# update the count of vowel in each occurrence
for w in a:
    if 'a' == w:
        count_of_a = count_of_a+1
    elif 'e' == w:
        count_of_e = count_of_e+1
    elif 'i' == w:
        count_of_i = count_of_i+1
    elif 'o' == w:
        count_of_o = count_of_o+1
    elif 'u' == w:
        count_of_u = count_of_u+1

# display the count of each vowel
print("count_of_a is",count_of_a)
print("count_of_e is",count_of_e)
print("count_of_i",count_of_i)
print("count_of_o",count_of_o)
print("count_of_a",count_of_u)