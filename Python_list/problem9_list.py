# Program to add two matrices using nested loop

X = [[12,7,3, 4, 5],
    [4 ,5, 6, 7, 8], 
    [7 ,8,9, 10, 11]]

Y = [[5,8,1, 1, 2],
    [6,7,3, 3, 4],
    [4,5,9, 5, 6]]

result = [[0,0,0, 0, 0],
         [0,0,0, 0, 0],
         [0,0,0, 0, 0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)