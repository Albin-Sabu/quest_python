# Print X shape made up of stars of n lines

Lines = int(input("Enter the number of lines: "))
for i in range(Lines):
    for j in range(Lines):
        if i == j or i + j == Lines - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


