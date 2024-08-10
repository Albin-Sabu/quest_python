# find smallest and biggest elements in a list
def big_element(list_1):
    biggest = max(list_1)
    return biggest
def small_element(list_1):
    smallest = min(list_1)
    return smallest
list_1 = []
length = int(input("Enter the length of list:"))
print("Enter the list values")
for i in range(length):
    a = int(input())
    list_1.append(a)
biggest = big_element(list_1)
print("The biggest element is", biggest)
smallest = small_element(list_1)
print("The biggest element is", smallest)

'''
Algorithm
-------------------
step 1
Enter the length of the list and create an empty list

step 2
add elements to the list using append method and loop

step3
make function for biggest by passing the list

step4
using max function we can easiy find the biggest in list and return the biggest

step5
make function for smallest by passing the list

step6
using min function we can easiy find the smallest in list and return the smallest
'''