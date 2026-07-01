'''-------------------count prime numbers in a range----------------------------------------
#--------------------------------------------------------------------------------------------

Accept two integers representing the starting and ending values of a range. 
Display all prime numbers within the range and finally display the total number of prime 
numbers found.
'''

#--------------------------------------------------------------------------------------------
#------------coding--------------------------------------------------------------------------------

#taking input number from user
n1 = int(input("Enter the number:"))
#validating the number
if (n1 <= 0):
    exit("the number must be positive")
n2= int(input("Enter the number:"))
if (n2 <= 0):
    exit("the number must be positive")
for i in range (n1, n2+1)