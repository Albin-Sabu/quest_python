#  Count the number of Prime digits in a number

number = int(input("Enter the number that you want to Count the number of Prime digits in a numbers: "))
list1 = []
number_list = [int(char) for char in str(number)]
count =0
for i in range(len(number_list)):
    if (number_list[i] == 2 or number_list[i] == 3 or number_list[i] == 5 or number_list[i] == 7):
        count += 1

print(count)        