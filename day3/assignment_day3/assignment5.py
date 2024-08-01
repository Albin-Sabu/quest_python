# Demonstrate the different ways of adding elements to a list and different ways to delete elements from a list.

# Different ways of adding element

# append() method
my_list1 = [1, 2, 3]
my_list1.append(4)
print("After append:", my_list1)

# insert() method
my_list2 = [1, 2, 3]
my_list2.insert(1, 'a')
print("After insert:", my_list2)

# extend() method

my_list3 = [1, 2, 3]
my_list3.extend([4, 5])
print("After extend:", my_list3)

# + Operator
my_list4 = [1, 2, 3]
my_list4 = my_list4 + [4, 5]
print("After concatenation:", my_list4)

# list Comprehension
my_list5 = [i for i in range(5)]
print("After list comprehension:", my_list5)

# Deleting Elements from a List:

# remove()
my_list6 = [1, 2, 3, 2, 4]
my_list6.remove(2)
print("After remove:", my_list6)

# pop()
my_list7 = [1, 2, 3, 4]
element = my_list7.pop(1)
print("After pop:", my_list7) 
print("Popped element:", element)

# del
my_list8 = [1, 2, 3, 4]
del my_list8[1]
print("After del:", my_list8)

# clear
my_list9 = [1, 2, 3, 4]
my_list9.clear()
print("After clear:", my_list9)

# These are the methods for adding and removing from the list