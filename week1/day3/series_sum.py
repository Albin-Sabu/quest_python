# Find sum of the series: 1 - n + n(2) - n(3) - ..... m terms 

series_number = int(input("Enter the value of the number n in the series: "))
term_limit = int(input("Enter the number of terms: "))

# Initialize the sum of the series
sum_series = 0

# Calculate the sum of the series
for i in range(term_limit):
    term = (series_number ** i) * ((-1) ** (i+2))
    sum_series += term
    print(term)

# Print the sum of the series
print(f"The sum of the series 1 - n + n^2 - n^3 - ... for {term_limit} terms is: {sum_series}")