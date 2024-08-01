# Accept N numbers from the user and swap the consecutive elements in the list
def swap_elements(numbers):
    for i in range(0, len(numbers) - 1, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers

limit = int(input("Enter the number of elements: "))

numbers = []
for i in range(limit):
    number = int(input("Enter a number: "))
    numbers.append(number)

swapped_numbers = swap_elements(numbers)

print("List after swapping consecutive elements:", swapped_numbers)

'''
Algorithm
-----------
step 1
Enter the length of the list and create an empty list

step 2
add elements to the list using append method and loop

step3
make function for swapping the consecutive numbers in list
ie, for i in range(0, len(numbers) - 1, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    (interchanging the numbers)

step4
print the result by calling the function


'''