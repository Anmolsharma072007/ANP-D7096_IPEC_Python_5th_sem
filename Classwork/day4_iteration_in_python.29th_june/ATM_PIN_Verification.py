'''------------------------------atm pin varification-----------------------------------------
An ATM allows a user to enter the correct PIN. The correct PIN is 4589. 
The user can keep entering the PIN until it matches the correct one. 
Display "Access Granted" when the correct PIN is entered. 
#--------------------------------------------------------------------------
Sample Output 
Enter PIN: 1234 
Incorrect PIN  
#--------------------------------------------------------------------------
Enter PIN: 9876 
Incorrect PIN 
#--------------------------------------------------------------------------
Enter PIN: 4589 
Access Granted
'''

#--------------------------------------------------------------------------
#--------------------------coding------------------------------------------

#taking input pin from user
pin = int(input("Enter the pin digits: "))

#---------------------------------------------------------------------

pin = "4589"
while pin <= 0:
    print("pin cannot be possible")

    print("Access granted")