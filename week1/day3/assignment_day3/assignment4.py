# Remove the negative numbers from a list of N numbers
list_1 = []
length = int(input("Enter the length of list:"))
print("Enter the list values")
for i in range(length):
    a = int(input())
    list_1.append(a)
for i in list_1:
    if i < 0:
        list_1.remove(i)
print("The list after removing negative numbers: ",list_1)


# Here we are using the remove method to remove the element with the help of a loop
