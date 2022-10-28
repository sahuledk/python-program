# program to flat sub lists

my_list = [[1], [2, 3], [4, 5, 6, 7]]
flat = []

# perform flat using append
for sub in my_list:
    for n in sub:
        flat.append(n)

print(flat)