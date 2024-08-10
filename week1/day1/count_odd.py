# Program to count the number of digits in a number

number = int(input("Enter the number that you want to count the odd digits: "))
temp_number = number
odd_count = 0
while number > 0:
    digit = number % 10  
    if digit % 2 != 0:  
        odd_count += 1
    number //= 10 

print(temp_number, "It contain", odd_count, "odd digits")