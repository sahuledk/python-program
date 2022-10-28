# program to find the sum of two matrices


li = [
     [1, 2, 3],
     [3, 4, 5],
]


k = [
    [1, 2, 3],
    [3, 4, 5],
]

result = [
          [0, 0, 0],
          [0, 0, 0],
]

# iterate through rows
for i in range(len(li)):
    # iterate through columns
    for j in range(len(li[0])):
        result[i][j] = li[i][j] + k[i][j]
for r in result:
    print(r)
