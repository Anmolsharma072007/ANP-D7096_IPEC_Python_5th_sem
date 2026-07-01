'''---------------Scholarship Eligibility-----------------------------------
A university provides a scholarship only to students who score 90 or above. Write a Python
 program to accept a student's percentage and determine whether the student is eligible. 
 • If percentage is 90 or above, display: 
 Scholarship Approved 
 • Otherwise display: 
 Scholarship Not Approved 
 Sample Input 
 92 
 Sample Output 
 Scholarship Approved
'''

#input the score from the user
student_score = float(input("Enter the student score:"))
#validating the score  
if (student_score <= 0):
    exit("student_score must be positive")
#validating the calculation of student score 
if (student_score >= 90 ):
    print(" Scholarship Approved")
else:
    print(" Scholarship not Approved ")



'''output :
'''