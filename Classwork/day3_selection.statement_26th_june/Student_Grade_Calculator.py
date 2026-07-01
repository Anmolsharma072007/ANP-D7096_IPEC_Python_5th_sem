#----------------Student Grade Calculator---------------------
'''A school assigns grades based on the marks obtained by students according to the following 
criteria:
* Marks 90 and above → Grade A
* Marks 75 to 89 → Grade B
* Marks 50 to 74 → Grade C
* Below 50 → Grade F
Write a Python program to accept marks from the user and display the corresponding grade.
#----------------------------------------------------
Sample Input
Enter Marks: 92
#----------------------------------------------------
Sample Output
Grade A
#----------------------------------------------------
Sample Input
Enter Marks: 80
#----------------------------------------------------
Sample Output
Grade B
#----------------------------------------------------
Sample Input
Enter Marks: 65
#----------------------------------------------------
Sample Output
Grade C
#----------------------------------------------------
Sample Input
Enter Marks: 35
#----------------------------------------------------
Sample Output
Grade F
#----------------------------------------------------
'''

#input from user
marks = float(input("Enter the marks:"))
#---------input validation----------------
if  (marks < 0):
    print("marks cannot be negative")
elif marks> 100:
    print("marks cannot be greater than 100")
#grade calculation
elif marks>=90:
    print ("grade A")
elif (marks >= 75):
    print ("grade B")
elif (marks >= 50):
    print("grade C")
else:
    print("grade F")

'''output :
marks : 40
grade F
'''