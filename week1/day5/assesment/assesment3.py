# Problem Name: Vasya & Birthday Present


def decending_order_sorting(test_cases):
    for i in range(test_cases):
        element = int(input())
        string_of_numbers = [int(num) for num in input(f'Enter the {element} numbers :').split(' ')]
        string_of_numbers.sort()
        list = string_of_numbers[::-1]
        for i in range(element):
            a = int(list[i])
            print(a, end=" ")

test_cases = int(input())
decending_order_sorting(test_cases)