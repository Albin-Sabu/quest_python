# Find the grade/class of the given Average Score

Average_Score = int(input("Enter the average score : "))
if Average_Score >= 0 and Average_Score <= 49:
    print(Average_Score, "is in failed category")
elif Average_Score >= 50 and Average_Score <=74:
     print(Average_Score, "is in second class category")
elif Average_Score >= 75 and Average_Score <=90:
     print(Average_Score, "is in First class category")
elif Average_Score >= 91 and Average_Score <=100:
     print(Average_Score, "is in Distinction category")
else:
     print("Please enter a valid score.")