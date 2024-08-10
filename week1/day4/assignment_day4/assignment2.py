# Accpet a string of space seperated numbers and store them as a matrix (list of lists) of n rows. Now print the matrix row-wise

def matrix_row_wise(numbers,rows):  # function to split the given list of numbers into the given row and to print matrix row-wise
    list1 = []
    main_list = []
    column = len(numbers) // rows
    for i in range(0,len(numbers),column):
        for j in range(i,i+column):
            list1.append(numbers[j])
        main_list.append(list1)
    for row in main_list:
        for number in row:
            print('%3s'%(number), end='')
        print()

string_of_numbers = [string for string in input("Enter the numbers seperated with spaces :").split(' ')]
row_number = int(input("Enter the number of rows: "))

matrix_row_wise(string_of_numbers,row_number)