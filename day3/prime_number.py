# Check if a number is Prime
import math
number = int(input("Enter the number that you want to check Prime or not: "))
flag = False
if number > 1:
    for i in range(2,math.ceil(math.sqrt(number) + 1)):
        if number % i == 0:
            flag = True
            break
    if flag == True:
        print(number, "is not prime")
    else:
        print(number, "is prime")
else:
    print(number, "is not prime")
