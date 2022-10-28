# program to perform file operation

# opening anagram.py as f in read mode.
with open("anagram.py", "r")as f:
    x = f.read()

print(x)

# opening new.py file and write to it
m = open("new.py", "w")
m.write('print("enter the number")')
m.close()
