# Print a hollow square of n line with the diagonals.
Lines = int(input("Enter the number of lines: "))
for i in range(Lines):
    for j in range(Lines):
        if i == j or i + j == Lines - 1 or j == 0 or j == Lines-1 or i == 0 or i == Lines-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()