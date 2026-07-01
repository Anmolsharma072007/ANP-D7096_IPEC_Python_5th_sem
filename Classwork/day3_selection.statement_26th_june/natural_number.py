'''-----------------natural number
write a program to check whether a number is naturnal number or not
---------------------------------------------------------------------------
'''

#input from user
num = int(input("Enter the number:"))
#validating the number
if (num <= 0):
    exit("number must be positive")
#validating for number
if (num > 0):
    print("given number is natural number")
else:
    print("given number is not natural number")

'''
output :
Enter the number:30
given number is natural number
'''