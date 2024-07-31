# Program to count the number of digits in a number

number = int(input("Enter the number that you want to count the odd digits: "))
number_copy = number
digits = 0
check = 0
while number>0:
    check = number % 10
    number = number // 10
    if check // 2 != 0:
        digits = digits + 1
    
print(number_copy, "contain", digits, "odd digits")