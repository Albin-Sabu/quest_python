# Company selection problem
######################################
class CountError(Exception):
    def __init__(self, message):
        self.message = message
######################################
job = { "ECE":"Marketing", "MECH":"Sales", "BCOM":"Accounts"} 
preference_li = { "Marketing" : {"ARTS", "ENGLISH"}, "Sales" : {"MATHS"}, "Accounts" : {"MATHS", "ENGLISH"} }
branches = ["ECE", "MECH", "BCOM"]
mark_list = { "Marketing": [35, 90, 90], "Sales": [95, 35, 35], "Accounts": [90, 90, 35], }

###################################### 
name = input("Enter your name : ")
branch = input("Enter you branch (Branches: ECE, MECH, BCOM ): ").upper()
maths = int(input("Enter your maths mark: "))
english = int(input("Enter your english mark: "))
arts = int(input("Enter your arts mark: "))
marks =[maths, english, arts] # making all the marks as a list
preference = input("Enter your preferd subjects using comma (like maths, arts, english): ").upper()
prefer_list = preference.split(",")
try:
    if len(prefer_list) <= 3:
        pass
    else:
        raise CountError("Only add upto 3 preference")
except CountError as e:
    print(e)
except :
    print("Something went wrong. Try again") 
#######################################

for i in branches:
    if branch == i: # we are selecting our branch from the branches
        choice = job[i]  # Selecting the vacancy for the course
        if preference_li[choice].issubset(set(prefer_list)):  # Checking is the users preference is equal to the preference of the job vacancy
            count =0
            for k in range(3):               
                if marks[k] > mark_list[choice][k]:
                    count += 1  # if all the Marks are greater than the prefered marks for job the the count will be 3
                else:
                    break 
            if count == 3:
                print("You are eligible for", choice, "job")
            else:
                print("You are not eligible for job")
        else:
            print("You are not eligible for job")
       
    else:
        continue