#  Find biggest digit in a number
number = int(input("Enter the number that you want to find the biggest digit: "))
biggest_number =0
number_list = [int(char) for char in str(number)]
biggest_number = max(number_list)
print("Biggest digit in the number is : ",biggest_number)