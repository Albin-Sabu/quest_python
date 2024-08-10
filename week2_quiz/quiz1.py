"""
Write a code to demonstrate use of inheritance and polymorphism using below example:
1. Eatable
1.1 Vegetarian
1.2 Non-Vegetarian
properties to be used: carbs, fat, protein, isPeelable, isBoneless
Place appropriate properties in parent class or child class and assign the values in _init_

"""

class Eatable:
    def __init__(self, carbs, fat, protein, isPeelable, isBoneless):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
        self.isPeelable = isPeelable
        self.isBoneless = isBoneless

    def food_type(self):
        print("This is an eatable item.")

class Vegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isPeelable, isBoneless):
        super().__init__(carbs, fat, protein, isPeelable, isBoneless)

    def food_type(self):
        print("This is a vegetarian item.")

class NonVegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isPeelable, isBoneless):
        super().__init__(carbs, fat, protein, isPeelable, isBoneless)

    def food_type(self):
        print("This is a non-vegetarian item.")


vegetarian1 = Vegetarian(20, 1, 2, True, False)
nonVegetarian1 = NonVegetarian(0, 15, 25,False, True)


vegetarian1.food_type()
nonVegetarian1.food_type()
