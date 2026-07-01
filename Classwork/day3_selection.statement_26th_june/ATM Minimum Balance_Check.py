'''#----------------ATM Minimum Balance Check---------------
A bank requires customers to maintain a minimum balance of ₹5,000 in their savings account.
Write a Python program that accepts the current account balance from the user. If the 
balance is less than ₹5,000, display a warning message indicating that the minimum balance 
requirement is not maintained. 
#---------------------------------------------------------------
Sample Input 
Enter Account Balance: 3200 
#-----------------------------------------------------------------
Sample Output 
Warning! Your account balance is below the minimum required balance of ₹5000.
#---------------------------------------------------------------- 
Sample Input 
Enter Account Balance: 8000 
#----------------------------------------------------------------
Sample Output 
(No output)'''

#input from user
account_balance = float(input("Enter a account balance:"))
#validating the account_balance
if (account_balance <= 0):
    exit("account_balance must be positive")
#validating the atm minimum balance
if (account_balance < 5000):
    print("Warning! Your account balance is below the minimum required balance of 5000")
else:
    print("Your account balance meets the minimum balance requirement.")
#--------------------------------------------------

'''output :
account_balance : 3000
warning! Your account balance is below the minimum required balance of 5000.
'''