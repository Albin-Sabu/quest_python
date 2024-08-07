string1 = "9"
string2 = 9
try:
     
    if type(string1) == type(string2) == int:
        print(string1 + string2 )
    else:
            print(string1 + ' ' + string2 )
except TypeError:
        print("Both type should be same.")




