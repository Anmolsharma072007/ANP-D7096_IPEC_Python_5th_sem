'''-----------------------exam hall entry-------------------------------------------

Students are allowed to enter the examination hall only if they are carrying their 
admit card. 
Accept input as: 

• 1 → Admit Card Available  
• 0 → Admit Card Not Available  
#---------------------------------------------------------

If the input is 1, display: 
Enter Examination Hall 
Otherwise, do not display anything. 
#----------------------------------------------------------
Sample Input 
1 
#----------------------------------------------------------
Sample Output 
Enter Examination Hall 
#----------------------------------------------------------
'''

#-----------------------------------------------------------------------------
#-----------------------coding------------------------------------------------
 
#taking input from user

Admit_card = int(input("Enter the admit card input:"))

#-------------------------------------------------------------------------------

#validating the input of admit card to enter in examination hall

if (Admit_card == 1):
    print("enter examination hall")


#----------------------------------------------------------------------------------



'''
output:
'''