# find number of customers who got discount (They get discount if the bill amount is perfect square)
import math
number_of_customers = int(input("Enter the number of customers: "))
bill_amounts = []
count_of_perfect_square = 0
print(f'Enter bill amounts of {number_of_customers} customers: ')
for i in range(0,number_of_customers):
    bill_amounts.append(int(input()))
for i in bill_amounts:
    root_number = int(math.sqrt(i))
    root_number_square = root_number * root_number
    if root_number_square == i:
        count_of_perfect_square += 1
print("The number of customers selected for discount is:",count_of_perfect_square)   
