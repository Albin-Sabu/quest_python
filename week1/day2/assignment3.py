#  Find 2nd smallest digit in a number
number = int(input("Enter the number that you want to find the 2nd Smallest digit: "))
list1 = []
number_list = [int(char) for char in str(number)]
for i in range(len(number_list)):
    if number_list[i] not in list1:
        list1.append(number_list[i])
second_smallest = sorted(list1)
print("Second smallest digit in the number is : ",second_smallest[1])