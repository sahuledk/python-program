# program to execute multiplication of two matrix
X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [1, 2, 2, 2],
    [3, 4, 5, 6],
    [7, 8, 9, 10]
]

result = [
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]
]

# multiplication take place
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

# display the result
for r in result:
   print(r)
