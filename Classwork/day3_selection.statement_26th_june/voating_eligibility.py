'''-----------voating_eligibility
write a program to check a person is eligible for voating or not.
a person will be eligible if age is 18 or above
--------------------------------------------------------
'''

#input form user
age = int(input("Enter the age:"))
#validating the age
if (age <= 0):
    exit("age must be positive")
#validating eligibility for voating
if (age >=18):
    print("person is eligible for voating")
else:
    print("age is not eligible for voating")


'''
output:
Enter the age:15
age is not eligible for voating
'''