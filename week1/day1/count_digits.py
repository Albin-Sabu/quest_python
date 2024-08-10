# Program to count the number of digits in a number

number = int(input("Enter the number that you want to count the digits: "))
number_copy = number
digits = 0
while number>0:
    number = number // 10
    digits = digits + 1
print(number_copy, "contain", digits, "digits")