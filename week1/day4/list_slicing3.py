numbers = [2, 9, 7, 5, 3, 13, 19, 17, 29]
print(numbers[::3]) # start from biginning and go up to end of the list with increment of 3

print(numbers[-1:-11:-1])   #Start from index 8, go up to index 2 with decrement of 2 (or increment of -2)
print(numbers[0:12]) 
print(numbers[::]) # Since the increment is negative, we understand that we have to move in reverse (meaning from the end to towards the start). The area within the list we have to access is all the elements, because nothing is specified before and after the 1st colon 
print(numbers[::-1]) # Reversing list
print(numbers[8::-2])