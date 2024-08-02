'''
Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.
 
main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']
presence = [1, 0, 1, 0]
'''

def check_sub_string(string,sub):  # function to check howmany of them possess the sub string
    count = []
    for i in range(len(string)):
        if string[i].count(sub[i]) == 1:
            count.append(1)
        else:
            count.append(0)
    print("The presence of sub strings in the main strings is",count)
string_of_words = [string for string in input("Enter the strings to check if sub string is present or not (seperated with comma): ").split(',')]
sub_string = [sub for sub in input("Enter the sub strings to check (seperated with comma) : ").split(',')]
check_sub_string(string_of_words,sub_string)

