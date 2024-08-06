string1 = 9
string2 = "9"
if type(string1) == type(string2) == int:
    print(string1 + string2 )
elif type(string1) == type(string2) == str:
        print(string1 + ' ' + string2 )
else:
    try:
        print(string1 + string2)
    except TypeError:
        print("Both type should be same.")




