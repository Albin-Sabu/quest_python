numbers = [23, 7, 19, 41, 29, 3, 47]
 
print('Max number = ', max(numbers))
print('Min number = ', min(numbers))
print('Number of elements = ', len(numbers))
print('Sorted numbers using sorted() method = ', sorted(numbers))
print('Numbers after sorted() method = ', numbers) # sorted() doesnot change/modify the actual list isted it will make a copy 
numbers.sort()
print('Numbers after sort() method = ', numbers)