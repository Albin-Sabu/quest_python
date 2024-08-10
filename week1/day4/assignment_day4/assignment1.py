'''
User gives the data like this:
kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
You have to separate the states and store in the list states[] and also the separated capitals must be stored in capitals[]

'''

def state_and_capital(strings):  # function to separate  State and Capital and to store in different list
    state = []
    capital = []
    temp = []
    for i in range(len(strings)):
        temp = [string for string in strings[i].split('-')]
        state.append(temp[0])
        capital.append(temp[1])
    return state,capital

state_and_capitals = [strings for strings in input("Enter the state and capital in the given format (ie. kerala-thiruvananthapuram karnataka-bengaluru) :").split(' ')]

state,capital = state_and_capital(state_and_capitals)
print("The States in the given strings are", state)
print("The Capitals in the given strings are", capital)