# Find sum of Even placed digits in a number

number = int(input("Enter the number that you want to count the Even placed digits: "))
evenplaced_sum =0
number_list = [int(char) for char in str(number)]
for i in range(1,len(number_list),2):
    evenplaced_sum = evenplaced_sum + number_list[i]
print("Sum of Even placed numbers is : ",evenplaced_sum)
