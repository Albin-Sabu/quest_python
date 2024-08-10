numbers = [2, 9, 7, 5, 3, 13, 19, 17, 29]
# print(numbers[:]) # we get the complete list

# Here, we have written nothing before the colon and hence it is treated as 0, which means start from the beginning of the list. Here also have not written anything after the colon, which means it is treated as UP TO END OF THE LIST. 

# print(numbers[:3]) # Start from index 0 and access elements up to index 3-1 which is 2.

# print(numbers[1:-1]) # Start from index 1 (2nd element) and access elements up to last but element, because -1 is the index of last element and we must not include it.

print(numbers[1:8:8]) # start from index 1 and access upto index 8-1 and increment each time by 2 elements. So o/p is [9, 5, 3, 19]