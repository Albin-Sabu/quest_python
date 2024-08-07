# Main assignment:
# E commerce discount program.
#########################################################################
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\n")
occupation = input("Enter occupation: \nS. Student \nW. working\n")
residence = input("Enter Residence: \nH. Hosteler \nL. Localite\n")
residencePin = int(input("Enter your pin:"))
pin = [100011, 100234, 100254, 100001]
#########################################################################


if age >= 45 and gender.lower() == "f" and (residence.lower() == "h" or residence.lower() == "h") and (occupation.lower() == "s" or occupation.lower() == "w"):
    print("15 percentage discount applied for everything, thank you for shopping")

elif age > 60 and gender.lower() == "m" and (residence.lower() == "h" or residence.lower() == "h") and (occupation.lower() == "s" or occupation.lower() == "w"):
    print("15 percentage discount applied for everything , thank you for shopping")

elif age < 45 and gender.lower() == "f" and residence.lower() == "h" and occupation.lower() == "w":
    print("Grocery discount and fastrack/nyka coupon added, thank you for shopping")
    
elif age < 45 and gender.lower() == "f" and residence.lower() == "h" and occupation.lower() == "s":
    if residencePin in pin:
        print("Grocery discount and fastrack/nyka coupon added and a book discount coupon added, thank you for shopping")
    else:
        print("Grocery discount and fastrack/nyka coupon added, thank you for shopping")

elif age < 60 and gender.lower() == "m" and residence.lower() == "h" and occupation.lower() == "s":
    if residencePin in pin:
        print("Grocery discount and fastrack/titan coupon added and a discount for book is also added, thank you for shopping")
    else:
        print("Grocery discount and fastrack/Titan coupon added , thank you for shopping")

elif age < 60 and gender.lower() == "m" and residence.lower() == "h" and occupation.lower() == "w":
    print("Grocery discount and fastrack/titan coupon added, , thank you for shopping")

elif age < 45 and gender.lower() == "f" and residence.lower() == "l" and occupation.lower() == "w":
    print("Fastrack/nyka coupon added, thank you for shopping")

elif age < 45 and gender.lower() == "f" and residence.lower() == "l" and occupation.lower() == "s":
    if residencePin in pin:
        print("fastrack/nyka coupon added book discount also added, , thank you for shopping")
    else:
        print("Fastrack/nyka coupon added , thank you for shopping")
    

elif age < 60 and gender.lower() == "m" and residence.lower() == "l" and occupation.lower() == "w":
    print("Fastrack/Titan coupon added")

elif age < 60 and gender.lower() == "m" and residence.lower() == "l" and occupation.lower() == "s":
    if residencePin in pin:
        print("fastrack/Titan coupon added book discount also added, , thank you for shopping")
    else:
        print("Fastrack/Titan coupon added , thank you for shopping")

        
else:
    print("Thank you for shopping")


