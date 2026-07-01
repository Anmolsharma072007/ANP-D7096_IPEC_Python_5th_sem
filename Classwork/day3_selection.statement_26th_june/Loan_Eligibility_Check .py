'''----------------Loan Eligibility Check-----------------------------

A bank considers an applicant eligible for a personal loan only if their monthly salary is 
₹30,000 or more. Write a Python program to accept the applicant's monthly salary and display
 whether they are eligible to apply for the loan. 
 #-------------------------------------------------------
 Sample Input 1 
 Enter your monthly salary: 45000 
#-------------------------------------------------------
 Sample Output 1 
 Congratulations! You are eligible to apply for the loan.
#------------------------------------------------------- 
 Sample Input 2 
 Enter your monthly salary: 22000 
#-------------------------------------------------------
Sample Output 2 
 Sorry! You are not eligible to apply for the loan. 
#-------------------------------------------------------
 '''

#input from user
monthly_salary = float(input("Enter the monthly salary:"))
#validating the monthly_salary
if (monthly_salary <= 0):
    exit("monthly_salary must be positive")
if (monthly_salary >= 30,000):
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("sorry! You are not eligible to apply for the loan.")

'''output :
Enter the monthly salary:50000
Congratulations! You are eligible to apply for the loan.
'''
