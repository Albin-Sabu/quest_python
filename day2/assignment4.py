# Check if a number is Prime

number = int(input("Enter the number that you want to check Prime or not: "))
flag = False
for i in range(2,number//2):
    if number % i == 0:
        flag = True
        break
if flag == True:
    print(number, "is not prime")
else:
    print(number, "is prime")