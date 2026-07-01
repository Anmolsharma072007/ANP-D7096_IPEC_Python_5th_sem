'''#----------------------------ATM Cash Withdrawal--------------------------------------

A customer can withdraw money only if the requested amount does not exceed the available
balance. 
Accept the account balance and withdrawal amount. 

• If withdrawal amount is less than or equal to balance, display: 
Transaction Successful 
• Otherwise display: 
Insufficient Balance 

#----------------------------------------------------------------------------
Sample Input 
5000 
4500 
#----------------------------------------------------------------------------
Sample Output 
Transaction Successful 
'''

#----------------------------------------------------------------------------
#-----------------------------coding-----------------------------------------

#taking input from user
balance = float(input("Enter the account balance: "))
withdrawal_amount= float(input("Enter the withdrawal_amount: "))
#validating the balance 
if (balance <= 0 or withdrawal_amount <= 0):
    exit("balance  or withdrawal_amount must be positive.")
#validating the withdeawal amount to balance
if (withdrawal_amount <= balance):
    print("Transaction Successful ")
else:
    print("Insufficient Balance ")