import math
input_number = int(input("Enter a number to check if it is perfect square or not: "))
root_number = int(math.sqrt(input_number))
root_number_square = root_number * root_number
if root_number_square == input_number:
    print(f'{input_number} is perfect square') 
else:
    print(f'{input_number} is not a perfect square') 