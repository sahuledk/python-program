# find transpose of matrix

li = [
    [1, 2, 3],
    [5, 6, 4]
    ]

trans = [
        [0, 0],
        [0, 0],
        [0, 0]
        ]

# find transpose
for i in range(len(li)):
    for j in range(len(li[0])):
        trans[j][i] = li[i][j]

# display it
print("transpose is")
for r in trans:
    print(r)



