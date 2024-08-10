numbers = [3, 2, 5, 4]

numbers.sort()
print(numbers)

# fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# fruits.sort()
# print(fruits)
a = [1, 2, 3, 4]
x = 6
a.insert(len(a), x)
print(a)
a.append(x)
print(a)

a[len(a):] = ["8"]
print(a)

a[len(a):] = "albin"
print(a)

a[len(a):] = ["albin"]
print(a)
a[len(a):] = [8, 3, 4, 5, 6, 7, 2, 1]
print(a)
a[len(a):] = "9087654321"
print(a)

a.insert(-1, "98765")

print(a)
#Below is an error
# numbers[len(numbers):] = 3