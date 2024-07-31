#  Print an equi lateral triangle of n lines

lines = int(input("Enter the number of lines for Equi Triangle: "))
for i in range(1, lines + 1):
    for j in range(lines - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

