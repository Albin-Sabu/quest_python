
#########################################################################
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\n")
occupation = input("Enter occupation: \nS. Student \nW. working\n")
residence = input("Enter Residence: \nH. Hosteler \nL. Localite\n")
#########################################################################


if age >= 45 and gender.lower() == "f" and residence.lower() == "h" and (occupation.lower() == "s" or occupation.lower() == "w"):
    print("15 percentage discount applied for everything and some grocery discount coupon also applied, thank you for shopping")

elif age > 60 and gender.lower() == "m" and residence.lower() == "h" and (occupation.lower() == "s" or occupation.lower() == "w"):
    print("15 percentage discount applied for everything and some grocery discount coupon also applied, thank you for shopping")
    
elif age >= 45 and gender.lower() == "f" and residence.lower() == "l" and (occupation.lower() == "s" or occupation.lower() == "w"):
    print("15 percentage discount applied, thank you for shopping")

elif age >= 60 and gender.lower() == "m" and residence.lower() == "l" and (occupation.lower() == "s" or occupation.lower() == "w"):
    print("15 percentage discount applied, thank you for shopping")

elif age < 45 and gender.lower() == "f" and residence.lower() == "h" and occupation.lower() == "w":
    print("Grocery discount and fastrack/nyka coupon added, thank you for shopping")
    
elif age < 45 and gender.lower() == "f" and residence.lower() == "h" and occupation.lower() == "s":
    print("Grocery discount and fastrack/nyka coupon added and a book discount coupon added, thank you for shopping")

elif age < 60 and gender.lower() == "m" and residence.lower() == "h" and occupation.lower() == "s":
    print("Grocery discount and fastrack/titan coupon added and a discount for book is also added, thank you for shopping")

elif age < 60 and gender.lower() == "m" and residence.lower() == "h" and occupation.lower() == "w":
    print("Grocery discount and fastrack/titan coupon added, , thank you for shopping")

elif age < 45 and gender.lower() == "f" and residence.lower() == "l" and occupation.lower() == "w":
    print("Fastrack/nyka cupon added, thank you for shopping")

elif age > 60 and gender.lower() == "m" and residence.lower() == "l" and occupation.lower() == "s":
    print("Grocery discount and fastrack/titan coupon added book discount also added, , thank you for shopping")

elif age < 60 and gender.lower() == "m" and residence.lower() == "l" and occupation.lower() == "w":
    print("Fastrack/Titan coupon added")

elif age < 60 and gender.lower() == "m" and residence.lower() == "l" and occupation.lower() == "s":
    print("Fastrack/Titan coupon added,  book dicount also added, thank you for shopping")

        
else:
    print("Thank you for shopping")


