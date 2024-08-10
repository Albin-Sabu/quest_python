# modifiying ssignment using class, function, object

class check_vacancy:
    def __init__(self):
        self.jobs = {"ECE":"MARKETING", "MECH":"SALES", "BCOM":"ACCOUNTS", }
        self.preference = {"MARKETING":{"ARTS","ENGLISH"}, "SALES":{"MATHS"}, "ACCOUNTS":{"MATHS, ENGLISH"}}
        self.branches = ["ECE", "MECH", "BCOM"]
        self.mark_list = { "MARKETING": [35, 90, 90], "SALES": [95, 35, 35], "ACCOUNTS": [90, 90, 35], }

    def available_job(self,branch):
        return self.jobs.get(branch, None)
    
    def available_preferences(self, job, user_preference):
        return self.preference[job].issubset(set(user_preference))
    
    def mark_criteria(self,job,marks):
        count = 0
        for i in range(3):
            if marks[i] > self.mark_list[job][i]:
                count += 1
        
        if count == 3:
            return True
    
class jobSelection(check_vacancy):
    def __init__(self):
        super().__init__()

    def available_vacancy(self):
        print("ENTER THE DETAILS BELOW")
        self.name = input("ENTER YOUR NAME: ")
        self.branch = input("ENTER YOUR BRANCH (BRANCHES ARE ECE, MECH, BCOM): ").upper()
        print("ENTER YOUR MARKS")
        self.maths = int(input("MATHS: "))
        self.english = int(input("ENGLISH: "))
        self.arts = int(input("ARTS: "))
        self.marks = [self.maths, self.english, self.arts]
        self.user_preference = input("ENTER YOUR PREFERENCE SEPERATED BY COMMA (MAXIMUM 3 PREFERENCE): ").upper().split(",")
        job = self.available_job(self.branch)
        if job and self.available_preferences(job,self.user_preference) and self.mark_criteria(job,self.marks):
            print("ELIGIBLE JOB: ", job)
        else:
            print("ELIGIBLE JOB: NONE")

obj = jobSelection()
obj.available_vacancy()