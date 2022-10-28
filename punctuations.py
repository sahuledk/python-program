# program to remove punctuations

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
a = input("enter the string")

no = ''

# removing punctuations
for char in a:
    if char not in punctuations:
        no = no + char

print(no)


