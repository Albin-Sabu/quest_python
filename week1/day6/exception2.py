capital_cities = { 560001 : 'Bengaluru', 110001 : "New Delhi", 330001 : "Kolkata"}

city_population = {"mysuru" : 2000000, "kochi" : "3500000", "coimbatore" : 4000000, "vishakapatnam" : 3500000, "vijayawada" : 4000000}

try:
    print('Kochi population is: ', city_population["kochi"])
    print('Mysuru population is: ', city_population["mysuru"])
    print('Madurai population is: ', city_population["madurai"])
except KeyError:
    print('The city\'s population you wish to print does\'t exist')
except: # generic except block. IT works for any type of error
    print('Some error occured')