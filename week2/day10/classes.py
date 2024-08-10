class person:
    def __init__(self, age, gender, pincode):
        self.age = age
        self.gender = gender
        self.pincode = pincode
    
class student(person):
    def __init__(self, age, gender, pincode, residence):
        self.residence = residence
        super().__init__(age,gender,pincode)

class employee(person):
    def __init__(self, age, gender, pincode):
        super().__init__(age,gender,pincode)
    
s1 = student(22,"male",111111,"hostler")
e1 = employee(22,"male",111111)