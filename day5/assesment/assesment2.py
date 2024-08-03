# Problem Name:Riya was planning to invent a game of shifting

def shifting_matrix (input_rows,input_columns):


    matrix = []

    for i in range(input_rows):
        print(f'Enter {input_columns} elements of Row {i+1}: ')
        row_numbers = [] 
        for j in range(input_columns): 
            row_numbers.append(int(input()))
        matrix.append(row_numbers)
    print("The matrix that we are going to shift is: ")
    for rows in matrix:
        for number in rows:
            print('%-3s'%(number), end='')
        print()


    shifted_matrix = []
    for i in range(input_rows):
        row_numbers = []
        for j in range(input_columns):
            row_numbers.append(matrix[j][i]) # Matrix shifting
        shifted_matrix.append(row_numbers)
    print("Matrix after the shifting is:")
    for row in shifted_matrix:
        for number in row:
            print('%-3s'%(number), end='')
        print()



input_rows = int(input('Enter No. of rows of the matrix: '))
input_columns = int(input('Enter No. of columns of the matrix: '))

shifting_matrix (input_rows,input_columns)