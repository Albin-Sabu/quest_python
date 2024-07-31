# Print the Fibo series of n terms with 1st 2 terms as 1 and 2.
n_terms = int(input ("How many terms the user wants to print? "))  
   
n_1 = 1
n_2 = 2  
count = 0  
  
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid") 
elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n_terms:  
        print(n_1,end=" ")  
        nth = n_1 + n_2 
        n_1 = n_2  
        n_2 = nth  
        count += 1  
