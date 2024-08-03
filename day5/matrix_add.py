# Program to create 2D Array, that is, a Matrix(using List) and add it to another Matrix and print the sum Matrix.
 
rows = int(input('Enter number of rows of the Matrix: '))
columns = int(input('Enter number of columns of the Matrix: '))
 
matrix1 = []
matrix2 = []
for k in range(1,3):
    for i in range(rows):
        print(f'Enter {columns} numbers of Row-{i+1} for Matrix number {k}')
        row_numbers = [] # List that stores numbers of a specific row
        for j in range(columns): # To read numbers of a row
            row_numbers.append(int(input()))
        if k ==1:
            matrix1.append(row_numbers)
        else:
            matrix2.append(row_numbers)

print("Matrix1 :")
for row in matrix1:
    for number in row:
        print('%3s'%(number), end='')
    print()


print("Matrix2 :")
for row in matrix2:
    for number in row:
        print('%3s'%(number), end='')
    print()

for i in range(rows):  
    sum = [] 
    result = []
    for j in range(columns):
        sum.append(matrix1[i][j] + matrix2[i][j])
    result.append(sum)
print("Added matrix:")
for row in result:
    for number in row:
        print('%3s'%(number), end='')
    print()