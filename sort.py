# program to sort alphabetic order

my_str = input("enter the string ")

# sort the words
words = [word.lower() for word in my_str.split()]
print(words)

# print the words
print("The sorted words are:")
for word in words:
   print(word)
