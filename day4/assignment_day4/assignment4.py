# Accept N strings, and check howmany of them possess the string X


def check_sub_string(string,sub): # function to check howmany of them possess the sub string
    count = 0
    for i in string:
        if i.count(sub) == 1:
            count += 1
    print("Count of string that possess sub string", sub, "is: " ,count)
string_of_words = [string for string in input("Enter the strings to check if sub string is present or not (seperated with spaces): ").split(' ')]
sub_string = input("Enter the Sub string for checking: ")
check_sub_string(string_of_words,sub_string)
