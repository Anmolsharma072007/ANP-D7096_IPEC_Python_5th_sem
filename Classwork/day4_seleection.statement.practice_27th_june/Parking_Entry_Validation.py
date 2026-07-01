'''---------------------- Parking Entry Validation-----------------------------

Only vehicles having a valid parking pass are allowed to enter a private parking area. 
Accept either 1 (Valid Pass) or 0 (No Pass). 
#-------------------------------------------------------------------------
• If the input is 1, display: 
Entry Allowed 
#------------------------------------------------------------------------
• Otherwise display: 
Entry Denied 
#---------------------------------------------------------------------
Sample Input 
0 
#-------------------------------------------------------------------------
Sample Output 
Entry Denied
'''


#----------------------------------------------------------------------------
#-----------------------coding----------------------------------------------------------


#taking input from user

parking_pass = int(input("Enter a private parking area"))

#-------------------------------------------------------------------------

#validating the parking pass

if (parking_pass < 0 or parking_pass > 1):
    exit("invalid input")

#validating the valid parking pass are allowed to enter in private parking area

if (parking_pass == 1):
    print ("Entry Allowed ")
else:
    print ("Entry Denied")


'''
output :
'''