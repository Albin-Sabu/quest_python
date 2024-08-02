# Accept N strings and count the number of Palindromes in it.

def palindroms_or_not(string):  # function to check palindrome or not and to count how many of them are palindrome
    count = 0
    for i in string:
        if i[::-1] == i:
            count += 1
    print("Number of palindrome string is:",count)
string_of_words = [string for string in input("Enter the strings to check Palindrome or not seperated with spaces : ").split(' ')]
palindroms_or_not(string_of_words)
